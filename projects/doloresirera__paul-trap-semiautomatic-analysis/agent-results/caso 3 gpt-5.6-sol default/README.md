# Caso 3 — reanálisis exploratorio automático

Este caso contiene una implementación independiente del análisis de
micromoción, construida a partir del método escrito y de los videos crudos.

## Resultado

Se analizaron 11 videos y se detectaron 519 trazas. Ningún video superó
simultáneamente los criterios de calidad para informar una estimación final de
`Q/m`; por eso los valores individuales se presentan como diagnósticos.

## Archivos principales

- `analisis_qm.py`: análisis reproducible.
- `generar_informe_final.py`: generación del informe HTML.
- `resultados_qm/informe_resultados.html`: informe visual completo.
- `resultados_qm/resumen_videos.csv`: resumen por video.
- `resultados_qm/trazas_detectadas.csv`: detecciones individuales.
- `resultados_qm/figuras/`: ajustes e histogramas diagnósticos.
- `contexto_fisico.pdf` y `readme_metodo.pdf`: material metodológico de entrada.

El caso se trasladó a `agent-results/` para mantener la misma organización que
los demás análisis del repositorio. Las rutas internas del informe HTML se
mantuvieron relativas y continúan funcionando.
