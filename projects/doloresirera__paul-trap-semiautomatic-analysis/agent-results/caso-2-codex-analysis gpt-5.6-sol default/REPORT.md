# Análisis cuantitativo de micromoción en una trampa de Paul

## Resumen ejecutivo

Se analizaron **21 videos**, **15710 cuadros** y **732.2 s** de registro. La tasa media fue 21.4625 ± 0.0207 fps. El análisis geométrico de las trazas da un parámetro de Mathieu

**q = 0.200 (IC 95% bootstrap entre videos: 0.193–0.235)**,

y, bajo el modelo cuadrupolar ideal y tomando 1175 V como amplitud (no pico-a-pico),

**|Q|/m = 6.646e-04 C kg⁻¹ (IC 95%: 6.418e-04–7.825e-04 C kg⁻¹)**.

La frecuencia secular de pequeña amplitud predicha es **3.53 Hz**. Estas magnitudes son *estimaciones dependientes del modelo*: la geometría exacta, convención de voltaje, tiempo de exposición y proyección 3D no están documentados en los archivos.

## Datos y resultados observables

- Resolución: 640×480 px; codec H.264.
- Duración por video: 6.54–98.35 s.
- El nulo de RF se ajustó por separado en cada video para absorber desplazamientos de cámara. El residuo perpendicular mediano entre videos es 44.6 px. El ajuste global mostrado sólo como diagnóstico queda en x=291.9 px, y=331.3 px.
- Ancho transversal mediano de las trazas: 8.51 px (IC bootstrap entre videos 8.36–8.85 px).
- Si se fuerza el diámetro nominal de 30 µm como regla, la escala resulta 3.53 µm/px. Es sólo orientativa: desenfoque, PSF y profundidad de campo ensanchan la imagen.
- Se obtuvieron 80 picos de tracks (SNR≥5; 78 con SNR≥8). Sólo 1 cae a ±0.4 Hz de la predicción geométrica; la mayoría está por debajo de 1 Hz y es compatible con deriva/no estacionariedad. No se identifica una frecuencia secular independiente y robusta.

![Resumen cuantitativo](quantitative_summary.png)

![Espectros de tracks](track_spectra.png)

## Modelo y ecuaciones

Para un cuadrupolo ideal sin componente DC se usa la ecuación de Mathieu. Con Ω=2πf_RF,

`q = 2 Q V_RF / (m r0² Ω²)`.

En la aproximación |q|≪1, `x(t) ≈ u(t)[1 − (q/2) cos(Ωt)]`. La excursión pico-a-pico de micromovimiento es entonces `L ≈ |q| |u|`; por eso cada detección entrega `q_i = L_i/r_i`. Se corrigió el ancho óptico mediante `L_i = sqrt(major_i² − minor_i²)`. Sólo se aceptaron trazas alargadas, con r≥20 px, desalineación radial ≤30° y 0.01<q<1.2. La mediana se calculó primero por video y el IC remuestreando videos completos, para no tratar miles de cuadros correlacionados como observaciones independientes.

La conversión es `|Q|/m = q r0² Ω²/(2 V_RF)`. La frecuencia secular aproximada es `f_sec ≈ |q| f_RF/(2 sqrt(2))`.

## Procesamiento y decisiones metodológicas

1. Se tomó el canal rojo, se restó un fondo gaussiano local (σ=15 px) y se aplicó umbral adaptativo.
2. Los componentes conexos se describieron por centroide ponderado por intensidad y PCA ponderado; los percentiles 2–98% sobre el eje mayor definen la longitud robusta.
3. El nulo se ajustó minimizando las distancias perpendiculares a los ejes mayores de trazas alargadas.
4. Los centroides se enlazaron con asignación húngara (máximo 30 px/cuadro, hueco máximo 2 cuadros). Los espectros usan Welch y excluyen ±0.35 Hz alrededor del alias esperado de 50 Hz, situado cerca de 7.1 Hz por el muestreo de ~21.45 fps.

## Limitaciones e incertidumbres no incluidas en el IC estadístico

- **Voltaje:** si 1175 V es pico-a-pico y no amplitud, |Q|/m se duplica. Si es RMS, cambia por 1/√2 respecto de la convención adoptada.
- **Exposición:** `q=L/r` supone que la exposición cubre al menos un período RF (20 ms). Sin metadata de shutter, una exposición menor subestima L y q.
- **Geometría:** se asumió el factor de campo cuadrupolar ideal asociado a r0=8.9 mm. Electrodos anulares reales requieren un factor geométrico obtenido por simulación/calibración.
- **Proyección:** la cámara mide 2D; movimiento fuera del plano y perspectiva sesgan longitudes y radios.
- **Escala espacial:** no hay patrón métrico visible. No se reportan velocidades o amplitudes absolutas como mediciones; la escala basada en 30 µm es nominal.
- **Carga individual:** los videos permiten Q/m, no Q y m por separado. Para convertir habría que conocer densidad/masa de cada espora; además la dispersión de tamaño domina el error.
- **Conversión paramétrica a carga:** para una esfera de 30 µm, `m = 1.414e-14 ρ kg` (ρ en kg/m³) y el resultado central implica `|Q| = 9.396e-18 ρ C = 58.6 ρ cargas elementales`. Por ejemplo, si ρ=1000 kg/m³: m≈14.1 ng, |Q|≈9.40 fC≈5.86e+04 e. Este ejemplo no es una medición porque no se conoce la densidad efectiva de cada espora.
- **Signo:** la dinámica observada da |Q|/m, no el signo de Q.

## Archivos reproducibles

- `analyze_experiment.py`: pipeline completo.
- `video_metadata.csv`: metadatos derivados incluidos en el repositorio.
- `detections.csv` y `trace_measurements.csv`: datos cuadro a cuadro generados
  por el script, no versionados porque en conjunto ocupan más de 50 MB.
- `q_by_video.csv`, `rf_null_by_video.csv`, `track_frequencies.csv`, `summary.json`: resultados numéricos.
- `contact_sheet.png` y `sequence_*.png`: inspección visual.

Ejecutar con Python 3.12 y `numpy scipy pandas matplotlib opencv-python-headless`: `python analyze_experiment.py`.
