# Caso 4 — reanálisis GPT-6-Luna medium

Análisis full-frame de los 21 videos de licopodio de este caso, presentado con el formato del caso 1 GPT-6-Luna. El informe visual principal es [informe_reanalisis.html](informe_reanalisis.html).

## Resultado

Se analizaron 15.710 frames y se detectaron 176.526 componentes. Se conservaron 79.243 trazas de alta confianza para estadística descriptiva. La longitud mediana fue 68,60 px (P05–P95: 23,00–187,31 px).

El procesamiento espectral produjo 1.036 candidatos preliminares, pero ningún track superó simultáneamente los controles conservadores de duración, ajuste sinusoidal y resolución. Por eso los valores de q, Q/m, carga, rigidez y temperatura no se presentan como mediciones confirmadas. El informe HTML documenta las ecuaciones, decisiones y límites.

## Archivos

- `analisis_reproducible.py`: prepara los archivos compactos y genera el informe HTML.
- `analisis_video_completo.py`: copia del pipeline full-frame de detección, tracking y análisis.
- `auditoria_resultados.py`: auditoría de calidad aplicada a los resultados.
- `resultados_videos.csv` y `resultados_videos.json`: tabla y resumen por video.
- `fig_*.png`: resumen, detecciones, espectros y diagnósticos.
- `contact_sheet.jpg`: hoja de cuadros representativos.
- `informe_reanalisis.html`: informe estructurado en el formato del caso 1.

## Parámetros clave

Se procesaron todos los frames con canal rojo, fondo gaussiano σ=15 px, umbral 20 cuentas, cierre morfológico 3×3 px y área mínima 35 px. La máscara de alta confianza exige área ≥100 px², longitud ≥20 px, pico ≥60 y relación de aspecto ≥1,5. El tracking usa asignación húngara, distancia máxima 70 px y tolerancia de 2 frames.

Se usaron V_AC=1175 V, f_RF=50 Hz, r₀=8,9 mm y diámetro aproximado 30 µm únicamente en conversiones condicionales. Los videos no incluyen escala métrica ni tiempo de exposición; la excitación RF de 50 Hz tampoco se resuelve con la frecuencia de cámara (~21,46 Hz).

Los MP4 originales no se incluyen en esta carpeta. Las detecciones completas y los resultados de gran tamaño permanecen en el directorio `results/` del workspace de análisis.
