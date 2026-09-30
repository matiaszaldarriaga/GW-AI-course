# Caso 2 — reanálisis GPT-6-Luna medium

Análisis autónomo de los 21 videos de licopodio del Caso 2 mediante un modelo
eficiente basado en momentos de imagen/PCA. El informe visual principal es
[informe_reanalisis.html](informe_reanalisis.html).

## Resultado

El modelo estima, usando los seis videos que superaron los controles
geométricos objetivos,

```text
Q/m = (6,5 ± 1,9) × 10⁻⁴ C/kg
```

El resultado es exploratorio. La incertidumbre está dominada por la dispersión
entre videos y es mayor que la del análisis área–perímetro del Caso 4.

## Archivos

- `analisis_reproducible.py`: segmentación, medición PCA, ajuste robusto y bootstrap.
- `resultados_videos.csv` y `resultados_videos.json`: resultados por video.
- `detecciones.csv`: detecciones individuales.
- `fig_resumen_qm.png`: resumen de `Q/m` por video.
- `WIN_*.png`: figuras diagnósticas individuales.
- `informe_reanalisis.html`: metodología, comparación y límites de interpretación.

## Método

Se usó una sola umbralización del canal rojo. Para cada componente alargada se
calculó `L_PCA = sqrt(12 lambda_1)`, donde `lambda_1` es el autovalor principal
de la covarianza de sus píxeles. Se ajustó `L_PCA = cR` junto con el centro y
se convirtió `c` a `Q/m`. El procedimiento evita esqueletización, contornos,
perímetros y múltiples umbrales; por eso es más eficiente computacionalmente,
pero pierde información de curvatura.

Los videos originales no se incluyen en este directorio.
