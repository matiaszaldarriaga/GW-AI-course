"""Quantitative analysis of the lycopodium Paul-trap videos.

The videos contain luminous streaks rather than resolved point particles.  This
script detects each connected streak, estimates its centerline geometry, links
centroids between frames, and produces pixel-level and conditional physical
estimates.  Absolute length calibration is deliberately explicit: r0 is used
only in a separately labelled assumption-based calibration because no ruler or
electrode diameter is visible in the supplied frames.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from scipy.signal import periodogram

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
VIDEO_DIR = ROOT / "drive-download-20260926T014040Z-1-001"
OUT = ROOT / "results"
FIG = OUT / "figures"
OUT.mkdir(parents=True, exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)

# Experimental information supplied in contexto.txt.
V_AC = 1175.0           # V; convention (peak vs RMS) is not specified
F_RF = 50.0             # Hz
R0_M = 8.9e-3           # m
DIAMETER_M = 30e-6      # m, approximate lycopodium diameter
RHO_DEFAULT = 1000.0    # kg/m^3, conditional reference density
E_CHARGE = 1.602176634e-19

# Image-processing choices. They are recorded in metadata.json and report.md.
BG_SIGMA_PX = 15.0
HP_THRESHOLD = 20       # red-channel high-pass counts
MIN_AREA_PX = 35
MORPH_CLOSE = 3
MAX_LINK_PX = 70.0
MAX_GAP_FRAMES = 2
MIN_TRACK_POINTS = 12


def enhance_red(frame: np.ndarray) -> np.ndarray:
    """Return a background-subtracted red-channel image in 8-bit counts."""
    red = frame[:, :, 2].astype(np.float32)
    background = cv2.GaussianBlur(red, (0, 0), BG_SIGMA_PX)
    return np.clip(red - background, 0, 255).astype(np.uint8)


def weighted_centerline(xs: np.ndarray, ys: np.ndarray, weights: np.ndarray):
    """Estimate a centerline by binning pixels along the principal axis."""
    pts = np.column_stack([xs, ys]).astype(float)
    w = np.asarray(weights, dtype=float) + 1.0
    center = np.average(pts, axis=0, weights=w)
    d = pts - center
    cov = (d * w[:, None]).T @ d / w.sum()
    eigval, eigvec = np.linalg.eigh(cov)
    order = np.argsort(eigval)
    eigval = eigval[order]
    axis = eigvec[:, order[-1]]
    if axis[0] < 0:
        axis = -axis
    perp = np.array([-axis[1], axis[0]])
    p = d @ axis
    q = d @ perp

    extent = float(p.max() - p.min())
    nbins = int(np.clip(round(extent / 4.0), 6, 32))
    edges = np.linspace(p.min(), p.max(), nbins + 1)
    cp, cq = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (p >= lo) & (p <= hi if hi == edges[-1] else p < hi)
        if sel.sum() == 0:
            continue
        ww = w[sel]
        cp.append(np.average(p[sel], weights=ww))
        cq.append(np.average(q[sel], weights=ww))
    cp = np.asarray(cp)
    cq = np.asarray(cq)
    order2 = np.argsort(cp)
    cp, cq = cp[order2], cq[order2]
    centerline = center + cp[:, None] * axis + cq[:, None] * perp
    path_length = float(np.linalg.norm(np.diff(centerline, axis=0), axis=1).sum()) if len(centerline) > 1 else extent
    chord = float(np.linalg.norm(centerline[-1] - centerline[0])) if len(centerline) > 1 else extent
    # A quadratic transverse displacement gives a compact curvature descriptor.
    curvature = np.nan
    if len(cp) >= 5 and extent > 10:
        try:
            coef = np.polyfit(cp - cp.mean(), cq, 2, w=np.interp(cp, cp, np.ones_like(cp)))
            slope = 2 * coef[0] * (cp - cp.mean()) + coef[1]
            curv = 2 * coef[0] / np.power(1 + slope * slope, 1.5)
            curvature = float(np.median(curv))
        except (np.linalg.LinAlgError, ValueError):
            pass
    p0, p1 = centerline[0], centerline[-1]
    angle = float(np.degrees(np.arctan2(axis[1], axis[0])))
    return {
        "cx_px": float(center[0]),
        "cy_px": float(center[1]),
        "angle_deg": angle,
        "major_std_px": float(np.sqrt(max(eigval[-1], 0))),
        "minor_std_px": float(np.sqrt(max(eigval[0], 0))),
        "extent_px": extent,
        "chord_px": chord,
        "path_length_px": path_length,
        "curvature_px_inv": curvature,
        "x0_px": float(p0[0]), "y0_px": float(p0[1]),
        "x1_px": float(p1[0]), "y1_px": float(p1[1]),
    }


def detect_frame(frame: np.ndarray) -> list[dict]:
    hp = enhance_red(frame)
    mask = (hp >= HP_THRESHOLD).astype(np.uint8) * 255
    kernel = np.ones((MORPH_CLOSE, MORPH_CLOSE), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    n, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
    detections = []
    for label in range(1, n):
        x, y, width, height, area = [int(v) for v in stats[label]]
        if area < MIN_AREA_PX:
            continue
        ys, xs = np.where(labels == label)
        values = hp[ys, xs].astype(float)
        feature = weighted_centerline(xs, ys, values)
        feature.update({
            "bbox_x_px": x, "bbox_y_px": y,
            "bbox_w_px": width, "bbox_h_px": height,
            "area_px": area,
            "peak_hp": int(values.max()),
            "integrated_hp": float(values.sum()),
        })
        feature["aspect_ratio"] = feature["major_std_px"] / max(feature["minor_std_px"], 1e-6)
        detections.append(feature)
    return detections


def read_videos() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Detect streaks in all frames and return metadata and detections."""
    metadata = []
    records = []
    videos = sorted(VIDEO_DIR.glob("*.mp4"))
    for video_id, path in enumerate(videos):
        cap = cv2.VideoCapture(str(path))
        nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = float(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        metadata.append({
            "video_id": video_id, "name": path.name, "frames": nframes,
            "fps": fps, "width": width, "height": height,
            "duration_s": nframes / fps if fps else np.nan,
        })
        print(f"[{video_id+1:02d}/{len(videos)}] {path.name}: {nframes} frames")
        frame_i = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            for det_i, det in enumerate(detect_frame(frame)):
                row = {"video_id": video_id, "video": path.name, "frame": frame_i,
                       "time_s": frame_i / fps if fps else np.nan, "detection_i": det_i}
                row.update(det)
                records.append(row)
            frame_i += 1
            if frame_i % 500 == 0:
                print(f"  frame {frame_i}/{nframes}")
        cap.release()
    return pd.DataFrame(metadata), pd.DataFrame(records)


def track_detections(detections: pd.DataFrame) -> pd.DataFrame:
    """Link centroid detections with a conservative nearest-neighbour assignment."""
    if detections.empty:
        detections["track_id"] = pd.Series(dtype=int)
        return detections
    detections = detections.copy()
    detections["track_id"] = -1
    next_id = 0
    for video_id, video_df in detections.groupby("video_id", sort=True):
        active: dict[int, tuple[int, int]] = {}  # id -> (row index, missed frames)
        for frame, group in video_df.groupby("frame", sort=True):
            row_indices = group.index.to_numpy()
            points = group[["cx_px", "cy_px"]].to_numpy(float)
            active_ids = list(active)
            assigned_rows: set[int] = set()
            assigned_tracks: set[int] = set()
            if active_ids and len(row_indices):
                prev = np.array([detections.loc[active[t][0], ["cx_px", "cy_px"]].to_numpy(float) for t in active_ids])
                dist = np.linalg.norm(prev[:, None, :] - points[None, :, :], axis=2)
                rr, cc = linear_sum_assignment(dist)
                for r, c in zip(rr, cc):
                    if dist[r, c] <= MAX_LINK_PX:
                        tid = active_ids[r]
                        ridx = int(row_indices[c])
                        detections.at[ridx, "track_id"] = tid
                        active[tid] = (ridx, 0)
                        assigned_rows.add(ridx)
                        assigned_tracks.add(tid)
            # Tracks that did not match can survive a short gap.
            for tid in list(active):
                if tid not in assigned_tracks:
                    missed = active[tid][1] + 1
                    if missed > MAX_GAP_FRAMES:
                        del active[tid]
                    else:
                        active[tid] = (active[tid][0], missed)
            # Every unmatched detection starts a new track.
            for ridx in row_indices:
                ridx = int(ridx)
                if ridx not in assigned_rows:
                    detections.at[ridx, "track_id"] = next_id
                    active[next_id] = (ridx, 0)
                    next_id += 1
    return detections


def fit_trap_center(df: pd.DataFrame) -> tuple[float, float, float, int]:
    """Fit a common point to elongated streak axes, with robust reweighting."""
    use = df[(df["aspect_ratio"] > 1.35) & (df["path_length_px"] > 15)].copy()
    if len(use) < 20:
        return float(df["cx_px"].median()), float(df["cy_px"].median()), np.nan, len(use)
    theta = np.deg2rad(use["angle_deg"].to_numpy(float))
    normals = np.column_stack([-np.sin(theta), np.cos(theta)])
    points = use[["cx_px", "cy_px"]].to_numpy(float)
    weights = np.clip(use["path_length_px"].to_numpy(float), 10, 200)
    center = np.array([points[:, 0].mean(), points[:, 1].mean()])
    for _ in range(12):
        A = np.einsum("i,ij,ik->jk", weights, normals, normals)
        b = np.einsum("i,ij,ij->j", weights, normals, np.einsum("ij,ij->ij", normals, points))
        try:
            center = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            break
        residual = np.abs(np.sum(normals * (center - points), axis=1))
        scale = max(10.0, float(np.median(residual)) * 1.4826)
        weights = np.clip(use["path_length_px"].to_numpy(float), 10, 200) / (1 + (residual / (2 * scale)) ** 2)
    residual = np.abs(np.sum(normals * (center - points), axis=1))
    return float(center[0]), float(center[1]), float(np.median(residual)), len(use)


def add_geometry(detections: pd.DataFrame, metadata: pd.DataFrame):
    detections = detections.copy()
    centers = []
    for video_id, group in detections.groupby("video_id", sort=True):
        cx, cy, residual, n = fit_trap_center(group)
        centers.append({"video_id": video_id, "center_x_px": cx, "center_y_px": cy,
                        "center_fit_median_residual_px": residual, "center_fit_n": n})
    centers_df = pd.DataFrame(centers)
    detections = detections.merge(centers_df, on="video_id", how="left")
    dx = detections["cx_px"] - detections["center_x_px"]
    dy = detections["cy_px"] - detections["center_y_px"]
    detections["radius_px"] = np.hypot(dx, dy)
    detections["azimuth_deg"] = np.degrees(np.arctan2(dy, dx))
    # The orientation is axial, so compare it modulo 180 degrees with the radial direction.
    diff = (detections["angle_deg"] - detections["azimuth_deg"] + 90) % 180 - 90
    detections["radial_alignment_deg"] = diff.abs()
    ep0 = np.hypot(detections["x0_px"] - detections["center_x_px"], detections["y0_px"] - detections["center_y_px"])
    ep1 = np.hypot(detections["x1_px"] - detections["center_x_px"], detections["y1_px"] - detections["center_y_px"])
    detections["endpoint_radius_max_px"] = np.maximum(ep0, ep1)
    return detections, centers_df


def dominant_frequency(track: pd.DataFrame, fps: float) -> dict:
    """Estimate the strongest sub-Nyquist centroid oscillation in x/y."""
    track = track.sort_values("frame")
    frames = track["frame"].to_numpy(int)
    if len(frames) < MIN_TRACK_POINTS or frames[-1] - frames[0] < 48:
        return {"f_peak_hz": np.nan, "f_resolution_hz": np.nan, "amp_px": np.nan,
                "amp_x_px": np.nan, "amp_y_px": np.nan, "psd_peak": np.nan,
                "rms_residual_px": np.nan, "n_track": len(frames),
                "duration_track_s": (frames[-1] - frames[0]) / fps if len(frames) else 0}
    full = np.arange(frames[0], frames[-1] + 1)
    x = np.interp(full, frames, track["cx_px"].to_numpy(float))
    y = np.interp(full, frames, track["cy_px"].to_numpy(float))
    x = x - np.polyval(np.polyfit(full, x, 1), full)
    y = y - np.polyval(np.polyfit(full, y, 1), full)
    freq, px = periodogram(x, fs=fps, window="hann", detrend=False)
    _, py = periodogram(y, fs=fps, window="hann", detrend=False)
    power = px + py
    valid = (freq >= 0.10) & (freq <= min(8.0, fps / 2 - 0.1))
    if not valid.any() or not np.isfinite(power[valid]).any():
        return {"f_peak_hz": np.nan, "f_resolution_hz": fps / len(full), "amp_px": np.nan,
                "amp_x_px": np.nan, "amp_y_px": np.nan, "psd_peak": np.nan,
                "rms_residual_px": np.nan, "n_track": len(frames),
                "duration_track_s": (frames[-1] - frames[0]) / fps}
    masked_power = np.where(valid, power, -np.inf)
    idx = int(np.argmax(masked_power))
    f0 = float(freq[idx])
    omega = 2 * np.pi * f0 / fps
    design = np.column_stack([np.cos(omega * full), np.sin(omega * full), np.ones(len(full))])
    cx, *_ = np.linalg.lstsq(design, x, rcond=None)
    cy, *_ = np.linalg.lstsq(design, y, rcond=None)
    fit_x = design @ cx
    fit_y = design @ cy
    amp_x = float(np.hypot(cx[0], cx[1]))
    amp_y = float(np.hypot(cy[0], cy[1]))
    return {"f_peak_hz": f0, "f_resolution_hz": fps / len(full),
            "amp_px": float(np.hypot(amp_x, amp_y)), "amp_x_px": amp_x,
            "amp_y_px": amp_y, "psd_peak": float(power[idx]),
            "rms_residual_px": float(np.sqrt(np.mean((x-fit_x)**2 + (y-fit_y)**2))),
            "n_track": len(frames), "duration_track_s": (frames[-1] - frames[0]) / fps}


def analyze_tracks(detections: pd.DataFrame, metadata: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (video_id, track_id), group in detections.groupby(["video_id", "track_id"], sort=True):
        fps = float(metadata.loc[metadata.video_id == video_id, "fps"].iloc[0])
        out = {"video_id": video_id, "video": group["video"].iloc[0], "track_id": int(track_id),
               "start_frame": int(group.frame.min()), "end_frame": int(group.frame.max()),
               "n_detections": len(group), "mean_path_length_px": group.path_length_px.mean(),
               "median_path_length_px": group.path_length_px.median(),
               "mean_radius_px": group.radius_px.mean(), "median_alignment_deg": group.radial_alignment_deg.median()}
        out.update(dominant_frequency(group, fps))
        rows.append(out)
    return pd.DataFrame(rows)


def conditional_physics(tracks: pd.DataFrame, detections: pd.DataFrame, metadata: pd.DataFrame):
    """Compute Mathieu-model values conditional on an assumed scale and density."""
    # The image has no visible metric marker. The assumption-based scale uses the
    # 95th percentile of the maximum endpoint radius as the supplied r0.
    r95_px = float(detections["endpoint_radius_max_px"].quantile(0.95)) if len(detections) else np.nan
    mm_per_px = 1000 * R0_M / r95_px if np.isfinite(r95_px) and r95_px > 0 else np.nan
    omega_rf = 2 * np.pi * F_RF
    qm_per_q = R0_M**2 * omega_rf**2 / (2 * V_AC)
    mass_ref = RHO_DEFAULT * (np.pi / 6) * DIAMETER_M**3
    physical = tracks.copy()
    physical["scale_assumption"] = "r0 / q95(endpoint radius)"
    physical["r95_endpoint_px"] = r95_px
    physical["mm_per_px_assumed"] = mm_per_px
    physical["f_error_resolution_hz"] = physical["f_resolution_hz"] / 2
    physical["mathieu_q_abs"] = 2 * np.sqrt(2) * physical["f_peak_hz"] / F_RF
    physical["charge_to_mass_C_per_kg"] = qm_per_q * physical["mathieu_q_abs"]
    physical["mass_ref_kg_rho1000"] = mass_ref
    physical["charge_ref_C_rho1000"] = physical["charge_to_mass_C_per_kg"] * mass_ref
    physical["charge_ref_e_rho1000"] = physical["charge_ref_C_rho1000"] / E_CHARGE
    physical["stiffness_ref_N_per_m_rho1000"] = mass_ref * (2*np.pi*physical["f_peak_hz"])**2
    physical["amplitude_um_assumed"] = physical["amp_px"] * mm_per_px
    physical["mean_speed_um_per_frame_exposure"] = physical["median_path_length_px"] * mm_per_px * 1000
    return physical, {"r95_endpoint_px": r95_px, "mm_per_px_assumed": mm_per_px,
                      "qm_per_mathieu_q_C_per_kg": qm_per_q, "mass_ref_kg": mass_ref}


def save_examples(metadata: pd.DataFrame, detections: pd.DataFrame, centers: pd.DataFrame):
    selected = []
    for video_id in metadata.video_id:
        sub = detections[detections.video_id == video_id]
        if len(sub):
            # Frame with a near-median count of valid detections.
            counts = sub.groupby("frame").size()
            frame = int((counts - counts.median()).abs().idxmin())
            selected.append((int(video_id), frame))
    selected = selected[::max(1, len(selected)//6)][:6]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8), constrained_layout=True)
    for ax, (video_id, frame_no) in zip(axes.ravel(), selected):
        path = VIDEO_DIR / metadata.loc[metadata.video_id == video_id, "name"].iloc[0]
        cap = cv2.VideoCapture(str(path)); cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no); ok, frame = cap.read(); cap.release()
        if not ok:
            ax.axis("off"); continue
        hp = enhance_red(frame)
        ax.imshow(hp, cmap="inferno", vmin=0, vmax=max(60, np.percentile(hp, 99.9)))
        sub = detections[(detections.video_id == video_id) & (detections.frame == frame_no)]
        for _, d in sub.iterrows():
            ax.plot([d.x0_px, d.x1_px], [d.y0_px, d.y1_px], "c-", lw=1)
            ax.plot(d.cx_px, d.cy_px, "wo", ms=2)
        c = centers[centers.video_id == video_id].iloc[0]
        ax.plot(c.center_x_px, c.center_y_px, "r+", ms=10, mew=2)
        ax.set_title(f"video {video_id}, frame {frame_no}")
        ax.set_xlim(0, 640); ax.set_ylim(480, 0); ax.set_xlabel("x [px]"); ax.set_ylabel("y [px]")
    for ax in axes.ravel()[len(selected):]: ax.axis("off")
    fig.savefig(FIG / "detections_examples.png", dpi=180); plt.close(fig)


def make_figures(metadata, detections, centers, tracks, physical):
    # 1. Counts and streak-length distributions.
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.5), constrained_layout=True)
    counts = detections.groupby(["video_id", "frame"]).size().groupby("video_id").agg(["mean", "median", "max"])
    ax[0].bar(counts.index.astype(str), counts["mean"], color="tab:red", alpha=.8)
    ax[0].set(xlabel="video id", ylabel="mean streaks/frame", title="Detected luminous streaks")
    ax[0].grid(alpha=.25)
    ax[1].hist(detections.path_length_px, bins=50, color="tab:blue", alpha=.8)
    ax[1].set(xlabel="centerline length [px]", ylabel="detections", title="Streak length distribution")
    ax[1].grid(alpha=.25)
    fig.savefig(FIG / "detection_summary.png", dpi=180); plt.close(fig)

    # 2. All centroids and fitted common point per video.
    fig, ax = plt.subplots(figsize=(8, 6))
    for video_id, g in detections.groupby("video_id"):
        ax.scatter(g.cx_px, g.cy_px, s=2, alpha=.12, label=f"{video_id}")
        c = centers[centers.video_id == video_id].iloc[0]
        ax.plot(c.center_x_px, c.center_y_px, "kx", ms=8)
    ax.set(xlim=(0,640), ylim=(480,0), xlabel="x [px]", ylabel="y [px]", title="Detected centroids and fitted RF-null projection")
    ax.legend(ncol=4, fontsize=7, loc="upper right", markerscale=3)
    ax.grid(alpha=.2)
    fig.savefig(FIG / "centroids_and_centers.png", dpi=180); plt.close(fig)

    # 3. Radius versus streak-axis alignment.
    fig, ax = plt.subplots(figsize=(8, 5))
    sample = detections.sample(min(30000, len(detections)), random_state=2) if len(detections) else detections
    for video_id, g in sample.groupby("video_id"):
        ax.scatter(g.radius_px, g.radial_alignment_deg, s=3, alpha=.12, label=str(video_id))
    ax.set(xlabel="centroid radius from fitted center [px]", ylabel="axis vs radial direction [deg]",
           title="Geometry of the streaks")
    ax.axhline(45, color="k", lw=.7, ls="--"); ax.grid(alpha=.25)
    fig.savefig(FIG / "radial_alignment.png", dpi=180); plt.close(fig)

    # 4. Representative track spectra.
    fig, ax = plt.subplots(figsize=(9, 5))
    good = tracks[np.isfinite(tracks.f_peak_hz)].sort_values("n_detections", ascending=False).head(12)
    for _, tr in good.iterrows():
        g = detections[(detections.video_id == tr.video_id) & (detections.track_id == tr.track_id)].sort_values("frame")
        fps = float(metadata.loc[metadata.video_id == tr.video_id, "fps"].iloc[0])
        full = np.arange(int(g.frame.min()), int(g.frame.max()) + 1)
        x = np.interp(full, g.frame, g.cx_px); y = np.interp(full, g.frame, g.cy_px)
        f, px = periodogram(x - np.polyval(np.polyfit(full, x, 1), full), fs=fps, window="hann")
        _, py = periodogram(y - np.polyval(np.polyfit(full, y, 1), full), fs=fps, window="hann")
        ax.plot(f, px+py, alpha=.55, lw=1, label=f"v{int(tr.video_id)} t{int(tr.track_id)}: {tr.f_peak_hz:.2f} Hz")
    ax.set(xlim=(0,8), yscale="log", xlabel="frequency [Hz]", ylabel="x/y centroid PSD [px²/Hz]", title="Representative sub-Nyquist spectra")
    ax.grid(alpha=.25, which="both")
    if len(good): ax.legend(fontsize=7, ncol=2)
    fig.savefig(FIG / "track_spectra.png", dpi=180); plt.close(fig)

    # 5. Conditional physical estimates.
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.5), constrained_layout=True)
    p = physical[np.isfinite(physical.f_peak_hz)]
    if len(p):
        ax[0].errorbar(p.f_peak_hz, p.charge_to_mass_C_per_kg, xerr=p.f_error_resolution_hz,
                       fmt="o", alpha=.65, ms=4)
        ax[0].set(xlabel="dominant secular frequency [Hz]", ylabel="Q/m [C/kg]",
                  title="Mathieu-model estimate (conditional)")
        ax[1].hist(p.charge_ref_e_rho1000, bins=min(30, max(5, len(p)//2)), color="tab:green", alpha=.8)
        ax[1].set(xlabel="charge [elementary charges]", ylabel="tracks", title="Conditional charge distribution")
    for a in ax: a.grid(alpha=.25)
    fig.savefig(FIG / "physical_estimates.png", dpi=180); plt.close(fig)


def write_report(metadata, detections, centers, tracks, physical, constants):
    nframes = int(metadata.frames.sum())
    ndet = len(detections)
    ntracks = len(tracks)
    good = physical[np.isfinite(physical.f_peak_hz)]
    freq_text = "No hubo seguimientos suficientemente largos para una frecuencia espectral." if not len(good) else (
        f"Se obtuvieron {len(good)} estimaciones de frecuencia en tracks largos: "
        f"mediana {good.f_peak_hz.median():.3g} Hz, rango {good.f_peak_hz.min():.3g}–{good.f_peak_hz.max():.3g} Hz. "
        f"La resolución espectral mediana fue {good.f_resolution_hz.median():.3g} Hz."
    )
    md = rf"""# Análisis de micromoción en trampa de Paul anular

## Resumen

Se analizaron **{len(metadata)} videos**, **{nframes:,} frames** ({metadata.duration_s.sum():.1f} s nominales), con resolución {int(metadata.width.median())}×{int(metadata.height.median())} px y frecuencia de video mediana {metadata.fps.median():.4f} Hz. El detector encontró **{ndet:,} trazas luminosas** y construyó **{ntracks:,} seguimientos** de centroides. {freq_text}

Resultados visuales principales: [ejemplos de detección](figures/detections_examples.png), [resumen de detecciones](figures/detection_summary.png), [centroides y centros ajustados](figures/centroids_and_centers.png), [alineamiento radial](figures/radial_alignment.png), [espectros](figures/track_spectra.png) y [estimaciones físicas condicionales](figures/physical_estimates.png).

## Qué se hizo

1. Se leyó cada frame con OpenCV y se midió la frecuencia efectiva declarada por el contenedor. La media fue {metadata.fps.mean():.4f} Hz y la desviación entre videos {metadata.fps.std():.4f} Hz.
2. Se usó el canal rojo, donde están las marcas luminosas, y se restó un fondo gaussiano de escala σ={BG_SIGMA_PX:g} px. Se umbraló el residuo en {HP_THRESHOLD} cuentas, se cerraron pequeños huecos y se descartaron componentes con menos de {MIN_AREA_PX} px.
3. Para cada componente se calculó centroide ponderado por intensidad, PCA (eje principal, anchura, orientación), longitud de cuerda y una longitud de línea central obtenida por binning a lo largo del eje principal. También se ajustó una curvatura cuadrática local.
4. Los centroides se asociaron entre frames mediante asignación húngara, con distancia máxima {MAX_LINK_PX:g} px y tolerancia de {MAX_GAP_FRAMES} frames sin detección. Los seguimientos no se interpretan como identidad perfecta cuando hay cruces o componentes fusionadas.
5. Se ajustó un punto común a los ejes de las trazas largas. Ese punto es una estimación geométrica de la proyección del nulo de RF; el residuo mediano por video está en `centers.csv`.

## Magnitudes directamente observables

Los archivos CSV contienen todas las detecciones (`detections.csv`), seguimientos (`tracks.csv`) y metadatos (`video_metadata.csv`). La longitud de traza, el área, el ángulo, la curvatura, el radio respecto del centro ajustado y la posición del centroide están en píxeles. La escala temporal es la del video; la micromoción de 50 Hz no puede resolverse temporalmente porque la frecuencia de Nyquist de la cámara es aproximadamente {metadata.fps.median()/2:.2f} Hz. Las trazas integradas durante la exposición son, por eso, una observación complementaria de la dinámica sub-frame.

La velocidad media durante una exposición, si la exposición es τ, es

\[
    \bar v \simeq \frac{{L_{{img}}\,s}}{{\tau}},
\]

donde `L_img` es la longitud de línea central en píxeles y `s` la escala lineal. Como τ no está en los metadatos de los videos, se reporta `L_img·s` (distancia recorrida durante la exposición) y no una velocidad absoluta.

## Modelo físico usado para estimaciones

Para una coordenada radial idealizada de una trampa de Paul:

\[
\ddot x + \frac{{Q V_{{AC}}}}{{m r_0^2}}\cos(\Omega t)x=0,
\qquad
q=\frac{{2 Q V_{{AC}}}}{{m r_0^2\Omega^2}},
\]

que se escribe como ecuación de Mathieu. En el régimen de q pequeño y sin término DC, la frecuencia secular satisface

\[
\omega_{{sec}}\simeq\frac{{|q|\Omega}}{{2\sqrt 2}},
\qquad
\left|\frac Qm\right|=\frac{{|q|r_0^2\Omega^2}}{{2V_{{AC}}}},
\qquad
|q|=2\sqrt2\frac{{f_{{sec}}}}{{f_{{RF}}}}.
\]

Para cada track suficientemente largo se obtuvo la frecuencia de mayor potencia conjunta en x e y entre 0.1 y 8 Hz mediante periodograma, con un ajuste sinusoidal en esa frecuencia. Es una estimación espectral: el error tabulado es media resolución de bin y no incluye sesgos de tracking o un posible movimiento no sinusoidal.

## Valores físicos y sus incertidumbres

Los valores de `physical_estimates.csv` son **condicionales**, no una calibración metrológica. Al no haber una escala de imagen/régua visible, se adoptó únicamente para traducir unidades la hipótesis:

\[
 s = r_0 / P_{{95}},
\]

donde `P95` es el percentil 95 del radio máximo de los extremos de las trazas. Esto da `r95={constants['r95_endpoint_px']:.2f} px` y `s={constants['mm_per_px_assumed']:.5f} mm/px`. Si esta hipótesis no representa el borde físico de la trampa, todas las longitudes, amplitudes y rigideces absolutas deben reescalarse; las frecuencias y Q/m derivadas del modelo no dependen de s, aunque sí dependen de V_AC, r0 y de la convención peak/RMS.

Para convertir Q/m a carga se usó como referencia ρ={RHO_DEFAULT:g} kg/m³ y una esfera de diámetro {DIAMETER_M*1e6:g} µm:

\[
 m_{{ref}}=\rho\frac{{\pi d^3}}{{6}}={constants['mass_ref_kg']:.4e}\;kg,
\quad Q_{{ref}}=(Q/m)m_{{ref}}.
\]

En realidad, las esporas pueden no ser esféricas, su densidad no está medida y V_AC puede ser RMS o amplitud de pico. Por eso el informe debe leerse como `Q ∝ ρ d³` y como una estimación de orden de magnitud. Para cada frecuencia se incluye la incertidumbre de resolución; no se inventó una incertidumbre instrumental para magnitudes que no fueron calibradas.

## Limitaciones y controles de interpretación

- El frame rate (~{metadata.fps.median():.2f} Hz) no permite medir directamente la portadora RF de 50 Hz; cualquier afirmación sobre esa oscilación viene solo del modelo y de la longitud integrada de las trazas.
- Una componente conectada puede contener dos partículas que se cruzan; se conserva como una única detección para no introducir separación artificial. Es una fuente de sesgo en longitud y tracking.
- La cámara no proporciona aquí tiempo de exposición, escala de píxel, orientación 3D, densidad de la espora ni carga. Esas cantidades no se pueden recuperar de forma única de los MP4.
- Las estimaciones de Q/m requieren identificar inequívocamente la frecuencia secular y que la aproximación de Mathieu, el campo ideal y q pequeño sean válidos. Los CSV permiten filtrar tracks por duración, residuo sinusoidal y alineamiento radial.

## Reproducibilidad

El código ejecutable está en `scripts/analyze_trap.py`; la inspección inicial está en `scripts/inspect_media.py`. Para repetir:

```powershell
python scripts/analyze_trap.py
```

Constantes de entrada: `V_AC={V_AC:g} V`, `f_RF={F_RF:g} Hz`, `r0={R0_M*1e3:g} mm`, diámetro aproximado `{DIAMETER_M*1e6:g} µm`. Las decisiones de detección y tracking quedan declaradas al inicio del script.
"""
    (OUT / "report.md").write_text(md, encoding="utf-8")


def main():
    metadata, detections = read_videos()
    if detections.empty:
        raise RuntimeError("No se detectaron componentes; revise HP_THRESHOLD y MIN_AREA_PX")
    detections = track_detections(detections)
    detections, centers = add_geometry(detections, metadata)
    tracks = analyze_tracks(detections, metadata)
    physical, constants = conditional_physics(tracks, detections, metadata)

    metadata.to_csv(OUT / "video_metadata.csv", index=False)
    detections.to_csv(OUT / "detections.csv", index=False)
    centers.to_csv(OUT / "centers.csv", index=False)
    tracks.to_csv(OUT / "tracks.csv", index=False)
    physical.to_csv(OUT / "physical_estimates.csv", index=False)
    params = {
        "V_AC_V": V_AC, "f_RF_Hz": F_RF, "r0_m": R0_M, "diameter_m": DIAMETER_M,
        "rho_reference_kg_m3": RHO_DEFAULT, "bg_sigma_px": BG_SIGMA_PX,
        "hp_threshold": HP_THRESHOLD, "min_area_px": MIN_AREA_PX,
        "max_link_px": MAX_LINK_PX, "max_gap_frames": MAX_GAP_FRAMES,
        "mathieu_qm_per_q_C_per_kg": constants["qm_per_mathieu_q_C_per_kg"],
        "scale_assumption": "r0 divided by 95th percentile of maximum streak-endpoint radius",
        **constants,
    }
    (OUT / "analysis_parameters.json").write_text(json.dumps(params, indent=2), encoding="utf-8")
    save_examples(metadata, detections, centers)
    make_figures(metadata, detections, centers, tracks, physical)
    write_report(metadata, detections, centers, tracks, physical, constants)
    good = physical[np.isfinite(physical.f_peak_hz)]
    print(f"detections={len(detections)} tracks={len(tracks)} spectral_tracks={len(good)}")
    print(f"assumed_scale_mm_per_px={constants['mm_per_px_assumed']:.6g} r95_px={constants['r95_endpoint_px']:.4g}")
    if len(good):
        print(good[["f_peak_hz", "f_resolution_hz", "mathieu_q_abs", "charge_to_mass_C_per_kg"]].describe().to_string())


if __name__ == "__main__":
    main()
