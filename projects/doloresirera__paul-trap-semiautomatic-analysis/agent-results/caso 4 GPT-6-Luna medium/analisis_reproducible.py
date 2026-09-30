"""Empaquetado reproducible del análisis del caso 4.

El procesamiento full-frame está implementado en ``analisis_video_completo.py``
(copia del pipeline usado sobre los MP4). Este script reúne sus CSV/JSON/figuras
y genera el informe HTML con el mismo formato editorial del caso 1 GPT-6-Luna.
"""

from __future__ import annotations

import csv
import html
import json
import shutil
from pathlib import Path


CASE = Path(__file__).resolve().parent
TASK_ROOT = CASE.parents[2]
SOURCE = TASK_ROOT / "results"
if not (SOURCE / "final_summary.json").exists():
    SOURCE = CASE


def copy_file(source: Path, target: Path):
    if source.exists() and source.resolve() != target.resolve():
        shutil.copy2(source, target)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fmt(x, digits=3):
    if x is None or x == "" or x != x:
        return "—"
    if isinstance(x, str):
        return x
    return f"{x:.{digits}g}"


def prepare_artifacts():
    # Compact tables used by the HTML, preserving the large full detections file
    # outside this presentation folder.
    for name in [
        "final_summary.json", "analysis_parameters.json", "video_metadata.csv",
        "per_video_summary.csv", "centers.csv", "tracks.csv",
        "spectral_candidates.csv", "accepted_physical_tracks.csv",
    ]:
        copy_file(SOURCE / name, CASE / name)

    if (SOURCE / "contexto.txt").exists():
        copy_file(SOURCE / "contexto.txt", CASE / "contexto.txt")
    elif (TASK_ROOT / "contexto.txt").exists():
        copy_file(TASK_ROOT / "contexto.txt", CASE / "contexto.txt")

    image_map = {
        "final_quantitative_summary.png": "fig_resumen_trazas.png",
        "detections_examples.png": "fig_detecciones_ejemplos.png",
        "track_spectra.png": "fig_espectros.png",
        "candidate_track_paths.png": "fig_candidatos.png",
        "centroids_and_centers.png": "fig_centroides_centros.png",
        "radial_alignment.png": "fig_alineamiento_radial.png",
        "physical_estimates.png": "fig_estimaciones_condicionales.png",
    }
    for source_name, target_name in image_map.items():
        copy_file(SOURCE / "figures" / source_name, CASE / target_name)

    # The case-1 folder uses a JPG contact sheet.
    contact_png = TASK_ROOT / "results" / "inspection" / "contact_sheet.png"
    try:
        from PIL import Image
        if contact_png.exists():
            Image.open(contact_png).convert("RGB").save(CASE / "contact_sheet.jpg", quality=92)
    except Exception:
        copy_file(contact_png, CASE / "contact_sheet.png")

    # The complete video pipeline is included under the case folder for auditability.
    copy_file(TASK_ROOT / "scripts" / "analyze_trap.py", CASE / "analisis_video_completo.py")
    copy_file(TASK_ROOT / "scripts" / "finalize_report.py", CASE / "auditoria_resultados.py")


def build_compact_csv(summary_rows):
    fields = [
        "video_id", "video", "frames", "fps", "duration_s",
        "high_conf_detections", "high_conf_mean_streaks_per_frame",
        "high_conf_median_streaks_per_frame", "path_median_px",
        "path_p05_px", "path_p95_px", "area_median_px", "peak_median_hp",
    ]
    with (CASE / "resultados_videos.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: row.get(k, "") for k in fields} for row in summary_rows)


def table_rows(summary_rows):
    out = []
    for row in summary_rows:
        out.append(
            "<tr>"
            f"<td>{html.escape(str(row.get('video', '')))}</td>"
            f"<td>{row.get('high_conf_detections', 0)}</td>"
            f"<td>{fmt(row.get('path_median_px'))} px<br><span class='small'>P05–P95: {fmt(row.get('path_p05_px'))}–{fmt(row.get('path_p95_px'))} px</span></td>"
            f"<td>{fmt(row.get('high_conf_mean_streaks_per_frame'))}</td>"
            f"<td>{fmt(row.get('area_median_px'), 4)} px²</td>"
            "<td>Descriptivo; no es una medición de carga</td>"
            "</tr>"
        )
    return "".join(out)


def make_html(stats, summary_rows):
    accepted = int(stats["spectral_tracks_accepted"])
    image_gallery = [
        ("fig_resumen_trazas.png", "Resumen de longitudes y ocupación por video."),
        ("fig_detecciones_ejemplos.png", "Detecciones sobre cuadros representativos."),
        ("fig_espectros.png", "Espectros sub-Nyquist; predominan picos de baja resolución."),
        ("fig_candidatos.png", "Trayectorias largas candidatas y sus cambios de componente."),
        ("fig_centroides_centros.png", "Centroides y ajuste exploratorio de centros."),
        ("fig_alineamiento_radial.png", "Diagnóstico de alineamiento radial."),
        ("fig_estimaciones_condicionales.png", "Estimaciones Mathieu del primer pase, explícitamente condicionales."),
    ]
    gallery = "".join(
        f"<figure><img src='{name}' loading='lazy' alt='{html.escape(caption)}'><figcaption>{html.escape(caption)}</figcaption></figure>"
        for name, caption in image_gallery if (CASE / name).exists()
    )
    table = table_rows(summary_rows)
    s = stats
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Caso 4 — reanálisis GPT-6-Luna</title>
<style>
:root{{--ink:#1f2933;--muted:#52606d;--paper:#f6f7f9;--card:#fff;--accent:#176b68;--line:#d9e2ec}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 system-ui,Segoe UI,sans-serif}}
main{{max-width:1200px;margin:auto;padding:30px 22px 64px}}h1,h2{{line-height:1.2}}h1{{font-size:2rem}}h2{{margin-top:2.1rem;color:var(--accent)}}
.lead{{font-size:1.12rem;color:var(--muted)}}.callout{{background:#fff8e7;border-left:5px solid #cf8b22;padding:15px 18px;margin:18px 0}}
.card{{background:var(--card);padding:18px;border:1px solid var(--line);border-radius:10px;margin:18px 0}}
table{{border-collapse:collapse;width:100%;font-size:.9rem;background:white}}th,td{{padding:9px 8px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}
th{{background:#edf3f4;position:sticky;top:0}}td:first-child{{min-width:275px}}.scroll{{overflow:auto}}img{{max-width:100%;height:auto}}
figure{{margin:0;background:white;border:1px solid var(--line);border-radius:8px;padding:10px}}figcaption{{font-size:.88rem;color:var(--muted)}}
.gallery{{display:grid;grid-template-columns:repeat(auto-fit,minmax(440px,1fr));gap:14px}}code{{background:#edf2f7;padding:2px 5px;border-radius:4px}}.small{{font-size:.9rem;color:var(--muted)}}
</style></head><body><main>
<h1>Caso 4 — reanálisis de videos de micromoción</h1>
<p class="lead">Trampa de Paul anular · licopodio · análisis full-frame reproducible con el formato GPT-6-Luna</p>
<div class="callout"><strong>Resultado principal:</strong> se procesaron {s['n_videos']} videos y {s['n_frames']:,} frames. Se obtuvieron {s['detections_high_confidence']:,} trazas de alta confianza, pero ningún track superó simultáneamente los controles conservadores de duración, ajuste sinusoidal y resolución espectral. Por ello no se reportan valores confirmados de frecuencia secular, q, Q/m ni carga.</div>
<h2>Resumen cuantitativo</h2>
<div class="card"><ul>
<li>Duración nominal total: <strong>{s['duration_s']:.1f} s</strong>; frecuencia de video: <strong>{s['fps_median']:.4f} ± {s['fps_sd_between_videos']:.4f} Hz</strong>.</li>
<li>Detecciones totales: <strong>{s['detections_all']:,}</strong>; alta confianza: <strong>{s['detections_high_confidence']:,}</strong> ({100*s['high_conf_fraction']:.1f}%).</li>
<li>Longitud mediana: <strong>{s['path_median_px']:.2f} px</strong>; P05–P95: {s['path_p05_px']:.2f}–{s['path_p95_px']:.2f} px.</li>
<li>Tracks: <strong>{s['tracks_all']:,}</strong>; candidatos espectrales preliminares: {s['spectral_candidates_raw']:,}; aceptados físicamente: <strong>{accepted}</strong>.</li>
</ul></div>
<h2>Comparación por video</h2>
<p>Las trazas de la tabla son componentes detectadas y filtradas por calidad. Pueden corresponder a la misma partícula en cuadros sucesivos; no son observaciones independientes.</p>
<div class="scroll"><table><thead><tr><th>Video</th><th>Trazas alta confianza</th><th>Longitud mediana</th><th>Media trazas/frame</th><th>Área mediana</th><th>Estado físico</th></tr></thead><tbody>{table}</tbody></table></div>
<h2>Qué hice</h2><div class="card"><ol>
<li>Leí los 21 MP4 con OpenCV y usé la frecuencia declarada por cada contenedor.</li>
<li>Extraje el canal rojo, sustraje un fondo gaussiano de σ=15 px, umbralé a 20 cuentas y cerré huecos de 3×3 px.</li>
<li>Calculé centroide ponderado, PCA, orientación, área, cuerda, longitud de línea central y curvatura por componente.</li>
<li>Asocié centroides con asignación húngara, distancia máxima 70 px y tolerancia de 2 frames.</li>
<li>Usé como alta confianza área ≥100 px², longitud ≥20 px, pico ≥60 y aspect ratio ≥1,5.</li>
<li>Calculé periodogramas de las trayectorias largas. El criterio final exige duración ≥5 s, residuo relativo ≤0,70 y un pico separado al menos 3 bins de resolución.</li>
</ol></div>
<h2>Modelo físico y límites</h2><div class="card">
<p>El modelo ideal de Mathieu usado como referencia es:</p>
<p><code>x¨ + [Q V_AC/(m r₀²)] cos(Ωt) x = 0</code><br><code>q = 2 Q V_AC/(m r₀² Ω²)</code></p>
<p>En q pequeño, <code>ω_sec ≈ |q|Ω/(2√2)</code> y <code>|Q/m| = |q|r₀²Ω²/(2V_AC)</code>.</p>
<p>Con V_AC=1175 V, f_RF=50 Hz y r₀=8,9 mm, la conversión condicional sería <code>Q/m = 0,00332669·q C/kg</code>. Sin una frecuencia secular aceptada, no se puede convertir de manera defendible a q, Q/m, carga, rigidez, energía o temperatura.</p>
<p>La escala condicional r₀/P95 da {s['scale_assumed_mm_px']:.5f} mm/px y una longitud mediana de {s['path_median_assumed_mm']:.3f} mm por exposición. El tiempo de exposición no está en los MP4; si se fuerza τ=1/fps, la velocidad mínima equivalente sería {s['speed_median_if_exposure_frame_mm_s']:.1f} mm/s.</p>
</div>
<h2>Decisiones y limitaciones</h2><div class="card"><ul>
<li>La cámara muestrea a ~21,46 Hz, por debajo de Nyquist para la excitación RF de 50 Hz.</li>
<li>Los centros geométricos exploratorios tienen residuos de {s['center_fit_residual_min_px']:.1f}–{s['center_fit_residual_max_px']:.1f} px; no se interpretan como un nulo RF confiable.</li>
<li>No se conocen escala métrica, exposición, densidad, forma, carga ni orientación 3D de las esporas.</li>
<li>Las trazas fusionadas, cruces, reflejos y background residual pueden sesgar la longitud y el tracking.</li>
</ul></div>
<h2>Figuras</h2><div class="gallery">{gallery}</div>
<h2>Archivos reproducibles</h2><p><a href="analisis_reproducible.py">Empaquetado y generación del informe</a> · <a href="analisis_video_completo.py">Pipeline full-frame</a> · <a href="resultados_videos.csv">Tabla CSV</a> · <a href="resultados_videos.json">Resumen JSON</a> · <a href="contact_sheet.jpg">Hoja de cuadros</a></p>
<p class="small">Los MP4 originales no se incluyen en esta carpeta. Los CSV detallados generados en el workspace permanecen en <code>results/</code>; aquí se conserva el formato compacto de presentación equivalente al caso 1.</p>
</main></body></html>"""


def main():
    CASE.mkdir(parents=True, exist_ok=True)
    prepare_artifacts()
    stats = load_json(CASE / "final_summary.json")
    summary_rows = list(csv.DictReader((CASE / "per_video_summary.csv").open(encoding="utf-8")))
    numeric = [
        "video_id", "frames", "fps", "duration_s", "high_conf_detections",
        "high_conf_mean_streaks_per_frame", "high_conf_median_streaks_per_frame",
        "path_median_px", "path_p05_px", "path_p95_px", "area_median_px", "peak_median_hp",
    ]
    for row in summary_rows:
        for key in numeric:
            if key in row and row[key] != "":
                row[key] = float(row[key])
    build_compact_csv(summary_rows)
    payload = {"resumen_global": stats, "por_video": summary_rows}
    (CASE / "resultados_videos.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (CASE / "informe_reanalisis.html").write_text(make_html(stats, summary_rows), encoding="utf-8")
    print(f"Generado {CASE / 'informe_reanalisis.html'} con {len(summary_rows)} videos")


if __name__ == "__main__":
    main()
