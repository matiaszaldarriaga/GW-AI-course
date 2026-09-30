# Análisis alternativo de la relación carga–masa

## Resultado principal

Se analizaron los videos `15_07_04` y `15_08_05`, correspondientes a los grupos 1 y 2 del informe. La identificación se verificó por el número de trazas, la geometría de la nube y la reproducción de los valores publicados al usar sus centros.

| Grupo | Trazas automáticas | Parámetro c alternativo | Q/m alternativo [C/kg] | Q/m del informe [C/kg] | Diferencia |
|---|---:|---:|---:|---:|---:|
| 1 | 80 | 0,539 ± 0,020 | (8,99 ± 1,08)×10⁻⁴ | (8,7 ± 1,0)×10⁻⁴ | +3,3 % |
| 2 | 132 | 0,535 ± 0,020 | (8,91 ± 1,07)×10⁻⁴ | (8,5 ± 1,0)×10⁻⁴ | +4,8 % |

Los intervalos son estimaciones de una desviación estándar. Un promedio de ambos grupos ponderado por varianza da `(8,95 ± 0,76)×10⁻⁴ C/kg`, aunque no debe interpretarse como una nueva medición independiente: ambos resultados comparten `r0`, tensión y parte del procedimiento óptico.

Las diferencias con el informe son menores que la incertidumbre combinada. Por lo tanto, no hay discrepancia estadísticamente significativa.

## Método alternativo

El informe reduce cada mancha a un esqueleto de un píxel y recorre ese esqueleto. Aquí cada estela se modeló como una cápsula tubular, posiblemente curva. Si `A` es el área de su silueta y `P` su perímetro, la longitud de su eje es

`L = 1/2 sqrt(P² - 4πA)`.

Esta identidad elimina algebraicamente el ancho de la estela. La estimación usa solamente el contorno y no necesita esqueletización, búsqueda de extremos ni recorrido de un grafo de píxeles. Una simulación de cápsulas rasterizadas con longitudes, anchos y orientaciones comparables dio un factor de escala `L_real/L_estimado = 1,004`; la mediana de `L_estimado/L_real` fue 0,994 y el intervalo percentil 16–84 %, 0,975–1,008. No se aplicó una corrección, porque es menor que las demás incertidumbres.

El procesamiento fue:

1. Muestreo determinista de 80 frames repartidos sobre cada video.
2. Segmentación del canal rojo en cinco umbrales: 32, 36, 40, 44 y 48.
3. Extracción automática de contornos y cálculo de `A`, `P`, centroide, brillo y tensor de segundo momento.
4. Longitud final igual a la mediana de las cinco longitudes área–perímetro.
5. Control de calidad reproducible: área mayor que 500 px², elongación mayor que 6, sensibilidad relativa al umbral menor que 30 %, distancia al centro mayor que 35 px y `0,1 < L/R < 0,908`.
6. Estimador de grupo: mediana de `c_i=L_i/R_i`, más resistente que la media a trazas fragmentadas o fusionadas.
7. Conversión mediante `Q/m = c r0² (2πf)²/(4V)`.

### Centro de la trampa

La longitud área–perímetro es independiente del método original, pero este análisis usa como calibración geométrica los centros publicados: `(281,4; 80,9) px` y `(292,3; 71,2) px`. Sus incertidumbres anisótropas de bootstrap, también informadas, se propagaron: `(5,8; 9,6) px` y `(3,3; 9,9) px`.

Esto es deliberado. Al intentar inferir simultáneamente centro y pendiente con los videos crudos aparece una degeneración fuerte debido al abanico angular incompleto: centros alejados con pendientes distintas producen residuos similares. Usar el centro ya validado aísla la pregunta relevante: cuánto cambia `Q/m` al medir `L` con otra geometría. En consecuencia, el resultado es una validación independiente de la medición de longitud, no una determinación completamente independiente de toda la cadena de análisis.

## Incertidumbre

Se remuestrearon frames completos, no trazas individuales, para conservar las correlaciones entre objetos del mismo cuadro. En cada una de 4000 réplicas se sorteó además el centro según sus incertidumbres en `x` e `y`. La variación común debida al umbral se obtuvo repitiendo el estimador para los cinco umbrales y se añadió como término sistemático. Finalmente se propagaron por Monte Carlo

- `r0 = (8,90 ± 0,50) mm`;
- `V = (1175 ± 24) V`;
- `f = 50 Hz`, tratada como exacta frente a las fuentes anteriores.

La sensibilidad al umbral aportó `σc=0,0076` y `0,0099`. La incertidumbre total de `c`, con centro y remuestreo, fue aproximadamente 0,020 en ambos grupos. En `Q/m` domina el radio: como la expresión contiene `r0²`, su aporte relativo es aproximadamente `2σr0/r0 = 11,2 %`. Por eso una mejora sustancial exige medir mejor la geometría de la trampa, no sólo procesar más frames.

## Comparación crítica

### Ventajas del enfoque área–perímetro

- Es automático: no hay aceptación o corrección manual de cada estela.
- No sufre retracción de extremos por esqueletización.
- Para una estela tubular ideal, el ancho se cancela exactamente.
- Emplea cinco umbrales y cuantifica el cambio, en lugar de depender de un único valor 40.
- Usa una mediana robusta y bootstrap por frames, evitando tratar como independientes todas las trazas de un mismo cuadro.
- Procesa 80 cuadros por video y deja una tabla auditable de cada detección.

### Limitaciones

- La fórmula supone una única banda tubular. Cruces, fusiones, ramificaciones o cortes por bajo brillo violan el modelo.
- Perímetros digitales son sensibles a rugosidad y pixelado; la validación sintética indica un sesgo pequeño para cápsulas limpias, no necesariamente para estelas complejas.
- Los criterios `área > 500 px²` y `elongación > 6` son objetivos y reproducibles, pero introducen selección: favorecen estelas largas y bien enfocadas.
- Los centros no se redeterminaron de forma independiente. Una medición externa del nulo de RF sería preferible.
- Una misma partícula aparece en múltiples frames. El bootstrap por frame maneja correlación intra-frame, pero sin seguimiento de identidad no elimina completamente la pseudorreplicación temporal.
- La cámara registra aproximadamente 21,45 fps, no 30 fps como afirma el informe. Esto no cambia `L/R`, pero sí invalida cualquier argumento de independencia temporal que use 30 fps sin consultar las marcas temporales reales.

### Dispersión intrínseca

Las desviaciones estándar crudas de `c_i` obtenidas aquí son 0,093 y 0,141; las MAD robustas equivalentes son 0,044 y 0,082. La gran diferencia entre desviación estándar y MAD, y la sensibilidad a los cortes geométricos, muestran colas debidas a segmentación imperfecta. Esto debilita la interpretación del informe de que `σ_observada²-σ_medición²` mide directamente diversidad física.

Además, el “error de medición” sistemático de un valor de grupo no debe restarse necesariamente, como si fuera ruido independiente de cada partícula, de la varianza traza a traza. Para demostrar dispersión física hace falta identificar cada espora y ajustar un modelo jerárquico con: error por observación, efectos comunes de centro/umbral y variación entre partículas. Con los videos actuales, la tendencia es compatible con heterogeneidad, pero no queda separada de forma concluyente de fragmentación, fusiones y repetición de partículas.

## Archivos reproducibles

- `analisis_alternativo.py`: extracción de contornos, longitud área–perímetro y utilidades generales.
- `ejecutar_analisis_final.py`: análisis final de los dos grupos, bootstrap y figuras.
- `resultado_final/resultados.csv`: resultados numéricos completos.
- `resultado_final/trazas_grupo_1.csv` y `trazas_grupo_2.csv`: auditoría traza por traza.
- `resultado_final/figura_grupo_1.png` y `figura_grupo_2.png`: figuras principales.

Para reproducir: `python ejecutar_analisis_final.py`. Requiere Python con OpenCV, NumPy, SciPy, pandas y Matplotlib.
