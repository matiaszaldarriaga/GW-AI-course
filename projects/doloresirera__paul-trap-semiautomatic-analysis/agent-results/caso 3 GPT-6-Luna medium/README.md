# Caso 3 — reanálisis GPT-6-Luna medium

Reanálisis reproducible de los 21 videos de esporas de licopodio. El informe visual principal es [`informe_reanalisis.html`](informe_reanalisis.html).

## Resultado

El procesamiento automático produjo estimaciones exploratorias, pero ningún video superó conjuntamente los controles de estabilidad del centro, cantidad mínima de trazas y límite de estabilidad `c < 0,908`. Por eso no se presenta ningún `Q/m` como medición confirmada. La tabla contiene todos los diagnósticos para auditar el análisis.

## Archivos

- `analisis_reproducible.py`: detección, ajuste, bootstrap y conversión a Q/m.
- `resultados_videos.csv`: resultados y diagnósticos por video.
- `decisiones.csv`: criterio aplicado a cada video.
- `informe_reanalisis.html`: informe con tabla, decisiones y galería de figuras.
- `figuras/`: para cada video, ajuste `L=cR` e histograma de `c_i`.
- `parametros.json`: parámetros numéricos.

## Parámetros clave

Se tomó un cuadro cada 30 frames, se usó el canal rojo y un umbral fijo 20. Se filtraron componentes con área 18–2200 px², bounding box menor que 20000 px² y elongación mínima 2. Se implementó esqueletización Zhang–Suen y longitud de arco de 8-conectividad. El centro y `c` se ajustaron simultáneamente con mínimos cuadrados robustos y se usaron 250 remuestras bootstrap.

La conversión condicional usa `VAC=1175 V`, `f=50 Hz` y `r0=8,9 mm`, dando `Q/m = 1,663e-3 c C/kg`.
