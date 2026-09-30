# Fórmula de β óptimo para crossbars memristivos

Proyecto final del curso. El problema elegido: **encontrar una fórmula barata (sin
grid-search) para estimar el β óptimo** de la no linealidad `softmax(β·I)` de una crossbar
memristiva, y usarla para acelerar el método de búsqueda existente (`search_best_beta()`).

**Lo que se presenta** (los dos artefactos "para personas" que pide la consigna del curso):

- 📄 [`reporte_final_beta_optimo/index.html`](reporte_final_beta_optimo/index.html) — página
  única con la síntesis completa del hilo de trabajo.
- 📄 [`reporte_final_beta_optimo/reporte_final_beta_optimo.pdf`](reporte_final_beta_optimo/reporte_final_beta_optimo.pdf)
  — el mismo contenido en PDF.

El resto de este repositorio es el material "para una máquina": el código, los datos
derivados y los reportes intermedios de cada paso del hilo, con su procedencia documentada.

## El hilo central, en orden

Cada carpeta corresponde a un paso de la investigación. El orden importa: cada reporte
retoma explícitamente el anterior (qué asumía, qué corrigió, qué queda sin resolver).

| # | Carpeta | Qué hizo | Resultado |
|---|---|---|---|
| 1 | `papers/Reporte_beta_optimo_analitico.pdf` | Deriva la fórmula candidata `β ~ κ/(√N·σ_W·V_rms)` (argumento CLT, vía Prezioso et al./LeCun et al.) | Punto de partida teórico |
| 2 | `analisis_beta_optimo.py` (raíz) | Exploración original: histogramas de pesos y corriente Monte Carlo | Idea inicial, con sesgos sin diagnosticar |
| 3 | `analisis_corrientes_beta_optimo/` | Diagnostica 2 sesgos del script anterior (muestreo combinatorio de pesos; voltajes equipesados en vez de píxeles reales de MNIST) | Corrección identificada |
| 4 | `validacion_formula_beta_optimo/` | Valida la fórmula analítica contra **6 grid-searches reales completos** (100 épocas) | Acierta orden de magnitud y dirección con INL; **no** explica la dependencia con el número de pulsos `p` |
| 5 | `formula_beta_optimo_propuesta/` | Combina `σ_W` con el "paso medio" de la curva P/D, con el Monte Carlo ya corregido | R²=0.947 sobre los 6 puntos (vs. 0.68 usando solo `σ_W`) |
| 6 | `reconstruccion_beta_optimo_18curvas/` → `reconstruccion_beta_optimo_30curvas/` | Reconfirma la fórmula al escalar de 6 a 18 y luego 30 curvas reales | R²=0.938→0.930, coeficientes casi idénticos; **30/30 curvas alcanzan ≥99% de su accuracy pico** con la β predicha, sin ninguna búsqueda |
| 7 | `mejora_search_best_beta/` | Usa la fórmula para centrar `search_best_beta()` en vez de una grilla ciega de 40 puntos | Regret medido: 0.08pp (mejorado) vs. 10.19pp (método original tal como se usa hoy) |
| 8 | `validacion_rango_conductancia/`, `mejora_estimacion_beta_INL_2e1_a_1e3/`, `reconstruccion_logits_val_INL_1e-2_p_100_beta1/` | Chequeos de robustez adicionales (ratio de conductancia, zona de transición de INL, sanity check reconstruyendo logits reales) | Ver reportes de cada carpeta |
| 9 | `MemCrossbarClass_beta_por_capa.py` (`search_best_beta_mejorado()`, integración a producción) | Una vez validada en el punto 7 como parche aparte (`MemDNNMejorado`), la mejora se integró directamente en la clase base `MemDNN` — mismas fórmulas y correcciones (common random numbers, grilla centrada en la predicción, meseta 1-SE), ya sin necesidad de una subclase separada | `Crossbar_train_experimento_beta_por_capa.py` la usa por defecto cuando `optimize_beta=True` |

`reporte_beta_optimo_soporte/` son experimentos de soporte más tempranos (2 de septiembre),
anteriores a que la fórmula tomara la forma de arriba.

Cada una de estas carpetas contiene su propio reporte (`.md`/`.tex`/`.pdf`) con una sección
final de **"registro de códigos usados"**: qué script es nuevo, qué función se importó sin
modificar y de dónde, y qué archivo de datos se usó — esa es la procedencia detallada de cada
resultado. `reporte_final_beta_optimo/` es la síntesis de todo eso; no reemplaza esos reportes,
los enlaza.

### Fuera del hilo central

El resto del repositorio (`exploracion_beta_capa_oculta_100/`, `Fuerza_bruta/`,
`MLP_test_SP/`, `analisis_epochs_series_minimos/`, `dataset_cluster/`, etc.) es exploración
relacionada pero **no** forma parte de esta entrega — queda en el repo como contexto, no como
la narrativa presentada.

## Código base

- `MemCrossbarClass_beta_por_capa.py` — clase `MemDNN`, `generar_curvas_pot_dep()`,
  `G0_initialization()`, `search_best_beta()`.
- `Crossbar_train_experimento_beta_por_capa.py` — script de entrenamiento que usa lo anterior
  y generó los datos de `data_beta_grid_search_SP/` (corrido en el cluster, ver más abajo).

Ninguno de los reportes de los pasos 1–8 modifica estos dos archivos: todo el código de esos
pasos vive en las carpetas de la tabla de arriba e importa de estos dos sin alterarlos
(`sys.path.insert` hacia la raíz del repo — ver nota de estructura más abajo). La única
excepción, y es intencional (paso 9 de la tabla): una vez que `mejora_search_best_beta/`
validó la búsqueda mejorada como un parche aparte (`MemDNNMejorado`, sin tocar la clase
base), esa misma mejora se integró directamente en `MemCrossbarClass_beta_por_capa.py`
(`MemDNN.search_best_beta_mejorado()`) para volverla el método de producción — el
`search_best_beta()` original queda en el archivo, sin usarse por defecto.

## Cómo reproducir

### 1. Entorno

```bash
pip install -r requirements.txt
```

### 2. Datos: MNIST / Fashion-MNIST

Los archivos `X_train_mnist.npy`, `y_train_mnist.npy`, `X_train_mnist_fashion.npy`,
`y_train_mnist_fashion.npy` (raíz del repo) **no están versionados** (ver `.gitignore`) porque
son ~1 GB de un dataset público — no tiene sentido re-almacenarlos en git. Formato esperado
exacto (confirmado leyendo el header de los `.npy` actuales de este proyecto):

| archivo | dtype | shape |
|---|---|---|
| `X_train_mnist.npy` | `float64` | `(60000, 784)`, valores en `[0, 1]` |
| `y_train_mnist.npy` | `int64` | `(60000,)` |
| `X_train_mnist_fashion.npy` | `float32` | `(60000, 784)`, valores en `[0, 1]` |
| `y_train_mnist_fashion.npy` | `uint8` | `(60000,)` |

Snippet para regenerarlos con `torchvision` (**no ejecutado en esta sesión** — no había un
intérprete de Python accesible en la máquina donde se armó esta reestructuración; verificar
`X.shape`, `X.dtype` y `X.max() <= 1.0` contra la tabla de arriba antes de confiar en él):

```python
import numpy as np
from torchvision.datasets import MNIST, FashionMNIST

def guardar(dataset_cls, sufijo, dtype):
    ds = dataset_cls(root="./_mnist_raw", train=True, download=True)
    X = (ds.data.numpy().reshape(len(ds), -1) / 255.0).astype(dtype)
    y = ds.targets.numpy()
    np.save(f"X_train_{sufijo}.npy", X)
    np.save(f"y_train_{sufijo}.npy", y)

guardar(MNIST, "mnist", np.float64)
guardar(FashionMNIST, "mnist_fashion", np.float32)
```

### 3. Reportes del hilo central (baratos, sin cluster)

Cada script de las carpetas 3–8 de la tabla de arriba es barato (segundos a minutos: Monte
Carlo, regresiones, reconstrucción de logits ya guardados) y se corre standalone, por ejemplo:

```bash
cd validacion_formula_beta_optimo
python validar_beta_optimo.py
```

Regenera exactamente las figuras/CSV ya versionados en esa carpeta.

### 4. Los grid-searches completos (`data_beta_grid_search_SP/`, ~34 GB, no versionados)

Esos datos **no** se pueden reproducir en una laptop: son 30 combinaciones de configuración ×
100 épocas × 20 series × 5 folds, corridas en el cluster HPC Habrok. La procedencia de cómo se
generaron está en `jobs_cluster_habrok/` (scripts de instalación de entorno y envío de jobs
SLURM, incluido `train_job.sh` y sus variantes por INL); los comandos de uso están anotados
en `comandos.txt`. Los resúmenes
derivados que sí importan para el hilo central (`resumen_por_INL/resumen_optimos.csv`, y los
`resultados_*curvas.csv` de cada carpeta) están commiteados — son la evidencia ya verificada,
aunque los `.npz` crudos que los produjeron no se rehospedan aquí.

## Qué se excluyó del repo y por qué

Ver `.gitignore`. En resumen: datos crudos regenerables (MNIST/.npy), salidas crudas del
grid-search de cluster (`.npz`, no regenerables sin el cluster pero documentadas más arriba),
los `.npz` crudos de los estudios laterales fuera del hilo central
(`analisis_distribucion_softmax_INL_*/`, `mejora_estimacion_beta_INL_2e1_a_1e3/chequeo_batch_number/`
— se mantienen sus figuras/reportes, no los snapshots que los generaron), y 2 PDFs de terceros
(`prezioso2015.pdf`, `ncomms3072.pdf`) que se citan en los reportes pero no se redistribuyen por
licencia — se mantienen en el repo los papers propios del proyecto (`APLED_2026.pdf`,
`Reporte_beta_optimo_analitico.pdf`).
