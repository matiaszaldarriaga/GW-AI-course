#!/usr/bin/env python
"""Agent2: QUBIC TD intensity quick-look using the QubicAcquisition + PCG solver.

The electrical-power input is not an optical-power calibration. Resulting values
are model-equivalent microkelvin, NOT calibrated sky temperature or polarization.
"""
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
os.environ['MPLCONFIGDIR'] = str(HERE / '.cache/matplotlib')
os.environ['PYOPERATORS_PATH'] = str(HERE / '.cache/pyoperators')

import argparse
import json
import time
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.time import Time
from pyoperators import Operator, DiagonalOperator, pcg
from qubicpack.qubicfp import qubicfp
from qubicpack.pixel_translation import make_id_focalplane
from qubic.lib.Qdictionary import qubicDict
from qubic.lib.Qsamplings import QubicSampling
from qubic.lib.Qscene import QubicScene
from qubic.lib.Instrument.Qinstrument import QubicInstrument
from qubic.lib.Instrument.Qacquisition import QubicAcquisition

DEFAULT_DATA_ROOT = Path('/home/iqueirolo/Documentos/Doctorado/Data/QUBIC/galactic_plane/2026-03-24')
DEFAULT_DATASET = '2026-03-24_07.25.31__galactic_plane_right_center_el50.0_52.0'


def output_directory(path):
    """Honor the task's requirement that Agent2 outputs stay in Agent2 Version."""
    path = Path(path).resolve()
    if not path.is_relative_to(HERE):
        raise ValueError(f'Output directory must be within {HERE}')
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')


def resolve_dataset_path(name_or_path, data_root=DEFAULT_DATA_ROOT):
    p = Path(name_or_path).expanduser()
    if not p.is_dir():
        p = Path(data_root) / p
    if not p.is_dir():
        raise FileNotFoundError(f'Dataset not found: {name_or_path}')
    return p.resolve()


def td_dictionary(nside=32):
    if nside < 1 or nside & (nside - 1):
        raise ValueError('nside must be a positive power of two')
    d = qubicDict()
    d.read_from_file('td.dict')
    d.update(nside=nside, kind='I', nf_sub=1, nf_recon=1,
             filter_nu=150e9, effective_duration=None, interp_projection=False,
             photon_noise=False, use_synthbeam_fits_file=False)
    return d


def sampling(t, az, el, period=None):
    t = np.asarray(t)
    if len(t) < 2 or not np.all(np.diff(t) > 0):
        raise ValueError('Pointing timestamps must increase strictly')
    p = QubicSampling(len(t), date_obs=Time(t[0], format='unix').isot,
                      time=t-t[0], period=period or float(np.median(np.diff(t))),
                      latitude=-(24+11/60), longitude=-(66+28/60))
    p.azimuth, p.elevation = az, el
    p.pitch, p.angle_hwp, p.fix_az = 0, 0, False
    return p


def verify_detector_order(inst):
    ids = make_id_focalplane()
    rows, cols = np.unravel_index(inst.detector.index, (34, 34))
    actual = []
    for row, col in zip(rows, cols):
        match = ids[(ids.row == 33-row) & (ids.col == col)]
        if len(match) != 1:
            raise ValueError('Detector identity lookup is ambiguous')
        actual.append(int(match.quadrant_QSindex[0]))
    if not np.array_equal(actual, np.arange(len(inst))):
        raise ValueError('QS detector rows do not match this instrument calibration')
    return len(actual)


def load_real_tod(dataset):
    """Recompute electrical power in SI locally; never patch installed qubicpack.

    This install's ADU2I returns microamps, but bias_phase passes those values to
    Vbias2Vtes (which requires amperes) and multiplies them to form timeline_Ptes.
    Fix units on the in-memory objects, then retain qubicpack's QS interpolation.
    Unknown current offsets, optical responsivity and gain/sign remain uncalibrated.
    """
    fp = qubicfp()
    fp.verbosity = 0
    fp.read_qubicstudio_dataset(str(dataset))
    ranges, rates, electrical = [], [], []
    for a in fp.asic_list:
        if a is None:
            continue
        tt = np.asarray(a.timeaxis(datatype='sci', axistype='pps'))
        if not np.all(np.isfinite(tt)) or not np.all(np.diff(tt) > 0):
            raise ValueError(f'Invalid native timestamps on ASIC {a.asic}')
        ranges.append((float(tt[0]), float(tt[-1])))
        rates.append(float(1/np.median(np.diff(tt))))
        current_A = a.ADU2I(a.timeline_array(), flip=False) * 1e-6
        if a.timeline_vbias is None:
            raise ValueError('No bias telemetry: cannot estimate electrical power')
        bias_V = np.asarray(a.timeline_vbias) * a.bias_factor
        voltage_V = a.Vbias2Vtes(bias_V, current_A)
        original = np.asarray(a.timeline_Ptes)
        corrected = current_A * voltage_V
        electrical.append(dict(asic=int(a.asic), bias_factor=float(a.bias_factor),
                               original_power_percentiles=np.percentile(original,[1,50,99]).tolist(),
                               corrected_power_W_percentiles=np.percentile(corrected,[1,50,99]).tolist()))
        a.timeline_Ptes = corrected
    t, y, *_ = fp.tod(units='Watt', indextype='QS')
    pt, az, el = (np.asarray(x, dtype=float) for x in
                  (fp.pointing_timeaxis(), fp.azimuth(), fp.elevation()))
    valid = np.isfinite(pt) & np.isfinite(az) & np.isfinite(el)
    pt, az, el = pt[valid], az[valid], el[valid]
    order = np.argsort(pt)
    pt, az, el = pt[order], az[order], el[order]
    pt, unique = np.unique(pt, return_index=True)
    az, el = az[unique], el[unique]
    if len(pt) < 2 or np.any((el < -90) | (el > 90)):
        raise ValueError('Missing or invalid pointing telemetry')
    # np.interp would silently extend endpoints; clip to real common support.
    low = max(pt[0], *(v[0] for v in ranges))
    high = min(pt[-1], *(v[1] for v in ranges))
    keep = (t >= low) & (t <= high)
    # Exclude long housekeeping gaps rather than interpolating across them.
    right = np.clip(np.searchsorted(pt, t), 1, len(pt)-1)
    keep &= (pt[right]-pt[right-1]) <= 5*np.median(np.diff(pt))
    az_unwrapped = np.rad2deg(np.unwrap(np.deg2rad(az)))
    info = dict(dataset=str(dataset), native_rates_Hz=rates,
                interpolated_rate_Hz=float(1/np.median(np.diff(t))),
                input_samples=int(len(t)), clipped_samples=int((~keep).sum()),
                hwp_available=fp.hwp_position() is not None,
                electrical_power_audit=electrical)
    return t, y, keep, pt, az_unwrapped, el, info


def average_blocks(t, y, valid, factor):
    """Boxcar low-pass then decimate; reject any block with invalid support.

    This finite boxcar has limited stop-band attenuation. It improves on taking
    every Nth sample but is not a precision anti-aliasing or map integration model.
    """
    if factor < 1 or int(factor) != factor:
        raise ValueError('time_bin must be a positive integer')
    n = len(t)//factor
    if n < 2:
        raise ValueError('Too few samples after averaging')
    tb = t[:n*factor].reshape(n,factor).mean(axis=1)
    good = valid[:n*factor].reshape(n,factor).all(axis=1)
    # Detector-by-detector calculation avoids a second full-size TOD allocation.
    yb = np.empty((y.shape[0], n))
    for k in range(y.shape[0]):
        yb[k] = y[k,:n*factor].reshape(n,factor).mean(axis=1)
    return tb[good], yb[:,good], dict(time_bin=factor,
        discarded_tail_samples=int(len(t)-n*factor), rejected_blocks=int((~good).sum()))


def solve_map(acq, tod, tol=1e-4, maxiter=500, remove_offsets=False,
              mask_fraction=0., verbose=False):
    if not 0 < tol < 1 or maxiter < 1:
        raise ValueError('Require 0 < tol < 1 and maxiter >= 1')
    if not np.all(np.isfinite(tod)):
        raise ValueError('Non-finite TOD cannot enter PCG')
    H = acq.get_operator()
    if H.shapeout != tod.shape:
        raise ValueError(f'TOD shape {tod.shape} != operator output {H.shapeout}')
    cov = acq.get_coverage()
    seen = cov > max(0., mask_fraction*cov.max())
    if not np.any(seen):
        raise ValueError('Empty observed map')
    # Packing removes zero-coverage null rows from the normal equations.
    shape = H.shapein
    packed_shape = (int(seen.sum()),) + shape[1:]
    def unpack(x, out):
        out[...] = 0
        out[seen] = x
    def pack(x, out):
        out[...] = x[seen]
    U = Operator(direct=unpack, transpose=pack, shapein=packed_shape,
                 shapeout=shape, dtype=float, flags={'linear': True})
    G = H * U
    data = np.array(tod, copy=True, order='C')
    if remove_offsets:
        if np.any(acq.instrument.detector.fknee != 0) or acq.psd is not None:
            raise ValueError('Constant-offset projection currently requires white temporal noise')
        def demean(x, out):
            out[...] = x - np.mean(x, axis=-1, keepdims=True)
        F = Operator(direct=demean, transpose=demean, shapein=tod.shape,
                     shapeout=tod.shape, dtype=float, flags={'linear': True})
        G = F * G
        data -= data.mean(axis=-1, keepdims=True)
    invn = acq.get_invntt_operator(det_noise=True, photon_noise=False)
    A = G.T * invn * G
    b = G.T * invn * data
    preconditioner = DiagonalOperator(1/cov[seen], broadcast='rightward')
    norm_b = np.linalg.norm(b)
    if norm_b == 0:
        result = dict(x=np.zeros(packed_shape),success=True,nit=0,error=0.,
                      message='Zero normal-equation RHS; zero map is a solution')
    else:
        result = pcg(A, b, M=preconditioner, tol=tol, maxiter=maxiter, disp=verbose)
    out = U(result['x'])
    # Compute residual explicitly as well as trusting the iterative estimate.
    relative = float(np.linalg.norm(A(result['x'])-b)/norm_b) if norm_b else 0.
    converged = bool(result['success'] and relative <= tol*1.05)
    info = dict(iterations=int(result['nit']), error=float(result['error']),
                recomputed_relative_residual=relative, converged=converged,
                message=str(result.get('message','')), tolerance=tol, maxiter=maxiter,
                fit_detector_offsets=remove_offsets, solved_pixels=int(seen.sum()),
                coverage_mask_fraction=mask_fraction,
                relative_TOD_fit_residual=float(np.linalg.norm(G(result['x'])-data)/np.linalg.norm(data))
                    if np.linalg.norm(data) else 0.)
    return out, cov, info


def plot_map(sky, cov, filename, title, unit='model-equivalent µK'):
    seen = cov > .15*cov.max()
    v = np.array(sky if sky.ndim == 1 else sky[:,0], copy=True)
    v[~seen] = hp.UNSEEN
    vectors = np.asarray(hp.pix2vec(hp.npix2nside(len(cov)),np.flatnonzero(seen))).T
    direction = np.average(vectors,axis=0,weights=cov[seen])
    direction /= np.linalg.norm(direction)
    lon,lat = hp.vec2ang(direction,lonlat=True)
    center = (float(lon[0]),float(lat[0]))
    radius = np.rad2deg(np.max(np.arccos(np.clip(vectors @ direction,-1,1))))
    field_degrees = min(90.,max(10.,2.5*radius))
    lo, hi = np.percentile(v[seen], [1,99])
    if lo == hi:
        lo, hi = lo-1, hi+1
    plt.figure(figsize=(10,6))
    hp.gnomview(v, rot=center, reso=field_degrees*60/500, xsize=500, min=lo, max=hi,
                title=title, unit=unit, cmap='coolwarm', sub=111)
    plt.savefig(filename, dpi=130, bbox_inches='tight')
    plt.close()


def real_data_to_map(dataset_dir, nside=32, time_bin=40, tol=1e-4, maxiter=500,
                     fit_offsets=True, verbose=False):
    start = time.monotonic()
    dataset = resolve_dataset_path(dataset_dir)
    d = td_dictionary(nside)
    t, y, keep, pt, az, el, info = load_real_tod(dataset)
    t, y, binfo = average_blocks(t, y, keep, time_bin)
    finite = np.all(np.isfinite(y), axis=1)
    varying = np.std(y, axis=1) > 0
    good = finite & varying
    if not np.any(good):
        raise ValueError('No valid, varying detectors')
    inst = QubicInstrument(d)
    info['verified_QS_detectors'] = verify_detector_order(inst)
    if len(inst) != len(y):
        raise ValueError('Dataset does not match the 248-detector TD')
    inst = inst[good]
    y = y[good]
    p = sampling(t, np.interp(t,pt,az)%360, np.interp(t,pt,el),
                 period=time_bin/info['interpolated_rate_Hz'])
    d.update(npointings=len(t), period=p.period, tol=tol, maxiter=maxiter)
    acq = QubicAcquisition(inst,p,QubicScene(d),d)
    sky, cov, solver = solve_map(acq,y,tol,maxiter,remove_offsets=fit_offsets,
                                mask_fraction=0.,verbose=verbose)
    info.update(binfo)
    info.update(nside=nside, n_samples_used=len(t), n_detectors=int(good.sum()),
                excluded_QS_detectors=np.flatnonzero(~good).tolist(),
                map_kind='I', filter_nu_Hz=150e9, solver=solver,
                map_units='model-equivalent uK, not calibrated optical sky temperature',
                TOD_units='estimated electrical power W with local SI correction',
                assumptions=['Q=U=0; no polarization inference', 'pitch=0 (unverified)',
                  'analytical TD beam; nominal equal detector noise',
                  'boxcar-averaged samples represented at their mean pointing',
                  'no optical responsivity, gain/sign, current-offset calibration or glitch removal',
                  'fitted constant per detector removes offset information; large-scale modes uncertain'],
                elapsed_seconds=time.monotonic()-start)
    return sky, cov, info


def save_real_result(sky, cov, info, outdir):
    outdir = output_directory(outdir)
    name = Path(info['dataset']).name
    np.save(outdir/f'{name}_map.npy',sky)
    np.save(outdir/f'{name}_cov.npy',cov)
    save_json(outdir/f'{name}_info.json',info)
    plot_map(sky,cov,outdir/f'{name}_map.png',
             'Real TD data: intensity quick-look\nElectrical power input; no optical calibration')
    return outdir/f'{name}_map.png'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('dataset', help='Full dataset path or directory name in the default data root')
    p.add_argument('--nside', type=int, default=32)
    p.add_argument('--time-bin', type=int, default=40, help='Average consecutive samples (default 40)')
    p.add_argument('--tol', type=float, default=1e-4)
    p.add_argument('--maxiter', type=int, default=500)
    p.add_argument('--keep-offsets', action='store_true', help='Diagnostic: do not fit per-detector constants')
    p.add_argument('--outdir', type=Path, default=HERE/'real_data_output')
    p.add_argument('--verbose', action='store_true')
    args = p.parse_args()
    outdir = output_directory(args.outdir)
    if args.time_bin < 1:
        p.error('--time-bin must be positive')
    sky,cov,info = real_data_to_map(args.dataset,args.nside,args.time_bin,args.tol,
                                  args.maxiter,not args.keep_offsets,args.verbose)
    png = save_real_result(sky,cov,info,outdir)
    print(json.dumps(info['solver'],indent=2))
    print(f'Saved map, coverage, metadata and PNG: {png}')
    if not info['solver']['converged']:
        print('WARNING: PCG did not converge; diagnostic outputs retained.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
