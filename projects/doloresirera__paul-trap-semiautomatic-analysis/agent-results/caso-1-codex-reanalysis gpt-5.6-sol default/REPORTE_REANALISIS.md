# Caso 1 — Reanálisis de la micromoción en la trampa de Paul

## Resultado principal

Reanalicé los 11 videos adjuntos. Los dos archivos que mejor se pueden asociar con los grupos del informe son:

| Archivo | Trazas aceptadas | c | Q/m (C/kg) | Informe |
|---|---:|---:|---:|---:|
| 8.32.44 PM | 151 | 0,528 ± 0,022 | (8,78 ± 1,07) 10⁻⁴ | grupo 1: c = 0,533 ± 0,069; Q/m = (8,7 ± 1,0) 10⁻⁴ |
| 8.34.49 PM | 192 | 0,529 ± 0,035 | (8,80 ± 1,16) 10⁻⁴ | grupo 2: c = 0,524 ± 0,060; Q/m = (8,5 ± 1,0) 10⁻⁴ |

La asociación no es completamente demostrable porque el informe no registra los nombres de archivo. Sin embargo, `8.34.49 PM`, frame 460, es exactamente la imagen de la Figura 5 del informe (diferencia cuadrática media de sólo 0,77 niveles RGB después de reducir ambas imágenes). `8.32.44 PM` es el otro video con resultado y geometría más compatibles.

## Resultados de todos los videos

| Video | N | c | Q/m [10⁻⁴ C/kg] |
|---|---:|---:|---:|
| 8.32.19 | 142 | 0,404 ± 0,041 | 6,72 ± 1,03 |
| 8.32.33 | 205 | 0,512 ± 0,020 | 8,52 ± 1,03 |
| 8.32.44 | 151 | 0,528 ± 0,022 | 8,78 ± 1,07 |
| 8.33.20 | 68 | 0,493 ± 0,026 | 8,21 ± 1,03 |
| 8.33.30 | 47 | 0,390 ± 0,021 | 6,49 ± 0,82 |
| 8.33.50 | 79 | 0,436 ± 0,045 | 7,25 ± 1,11 |
| 8.34.13 | 70 | 0,378 ± 0,048 | 6,28 ± 1,08 |
| 8.34.22 | 57 | 0,458 ± 0,042 | 7,62 ± 1,12 |
| 8.34.34 | 108 | 0,474 ± 0,035 | 7,89 ± 1,07 |
| 8.34.49 | 192 | 0,529 ± 0,035 | 8,80 ± 1,16 |
| 8.34.58 | 165 | 0,586 ± 0,031 | 9,74 ± 1,23 |

Estos resultados usan una regla idéntica para todos los archivos. En los videos de baja calidad el valor debe interpretarse como diagnóstico del conjunto visible, no como una medición final equivalente a los dos grupos validados. Todos quedan por debajo del límite de estabilidad c = 0,908.

## Método reproducido y cambios

Se tomaron 40 frames mediante muestreo aleatorio estratificado: se dividió el video en 40 intervalos y se tomó aleatoriamente un frame de cada uno, con semilla fija. Esto hace precisa y reproducible la indicación algo ambigua del informe de elegir frames “espaciados” y “de forma aleatoria”.

El umbral rojo 40 descrito en el informe no produce por sí solo las trazas que luego aparecen en sus figuras. En el frame 460 de `8.34.49 PM`, la traza verde continua de la Figura 6 queda separada en al menos seis componentes a umbral 40. La interfaz manual evidentemente los conectó. Para sustituir esa decisión subjetiva utilicé:

1. Canal rojo y umbral auxiliar 26, elegido porque conserva como un solo objeto la traza publicada sin incorporar el fondo masivo.
2. Área entre 250 y 8000 px y elongación mínima 2,5. El mínimo sube de 150 a 250 porque el umbral menor aumenta el área de todos los componentes.
3. Línea media cuadrática: ajuste de una curva de segundo grado en los ejes principales del objeto. Es más estable que sumar todos los píxeles de un esqueleto ruidoso y no necesita correcciones manuales.
4. Centro común `(286,85; 76,05)` px, promedio de los dos centros publicados. Por esto la reproducción de `c` es **condicional al centro del informe**, no una determinación completamente ciega del centro. Sin las selecciones/correcciones manuales originales, el ajuste simultáneo libre posee mínimos espurios y no reproduce de manera estable los centros.
5. Estimador central: mediana de `c_i=L_i/R_i`. La mediana evita que fragmentos residuales de trazas reduzcan artificialmente el resultado; el informe emplea la media después de selección manual.

Se calculó

`Q/m = c r0² Ω² / (4 V)`, con `r0 = (8,90 ± 0,50) mm`, `Ω = 2π 50 s⁻¹` y `V = (1175 ± 24) V`.

## Incertidumbres

La incertidumbre de `c` combina en cuadratura:

- bootstrap por frame, no por traza;
- mitad del rango obtenido con umbrales 24, 26 y 28;
- propagación Monte Carlo de una incertidumbre del centro de 5 px en x y 10 px en y, coherente con las nubes publicadas.

La incertidumbre de `Q/m` incluye además `r0` y `V`. El término instrumental relativo es 11,4 %, dominado por `r0` porque aparece al cuadrado.

Ésta es una diferencia importante con el informe: sus errores publicados de `Q/m` (aproximadamente 11–12 %) no parecen incluir simultáneamente el error informado de `c` y el de `r0`; propagarlos todos daría una incertidumbre mayor. En este reanálisis sí se propagaron juntos.

## Limitaciones y observaciones estadísticas

- Los 11 archivos duran entre 21 y 50 s y tienen una tasa real cercana a 21,45 fps, no 30 fps. El dato de 30 fps del informe parece ser nominal o anterior a la compresión/exportación de WhatsApp.
- El informe menciona 20 videos, pero se adjuntaron 11.
- Varias trazas pertenecen a la misma partícula observada en distintos frames. Por eso no son réplicas independientes. El bootstrap por frame es más conservador que remuestrear trazas sueltas, aunque el tratamiento ideal sería identificar y remuestrear partículas mediante tracking.
- La desviación estándar cruda de los `c_i` es grande porque todavía mezcla dispersión física, fragmentación residual y repetición de partículas. No considero justificado inferir una “dispersión intrínseca” mediante `sqrt(σ_obs²-σ_med²)` sin un modelo jerárquico por partícula.
- Un `R²` moderado no demuestra por sí solo dispersión física: también puede reflejar error en ambas variables, selección de trazas y centro incierto.

## Archivos producidos

- `resultados_por_video.csv`: valores completos y desglose de errores.
- `resultados_por_video.png`: comparación de `c` y `Q/m` para los 11 videos.
- `diagnostico_dos_videos.png`: histogramas y gráficos `L` contra `R` de los dos archivos comparados con el informe.
- `overview_videos.png`: tres frames de cada video.
- `analyze_trap.py`: análisis reproducible con semilla fija.
