# Revisión y reproducción del proyecto

Estado: 28/09/2026. Esta actualización resume resultados existentes; no ejecuta
nuevas simulaciones, entrenamiento ni validaciones de la red.

## Revisar sin ejecutar

1. Leer `docs/report/index.pdf` (5 páginas) o `docs/report/index.html`.
2. Consultar los resultados numéricos en `verification/` y las decisiones en
   `docs/sessions/`. Los nombres de los scripts y figuras permiten relacionarlos.
3. Para RIXS, consultar `data/rixs_library/mlp_checkpoint_meta.json`, `train_run.log`
   y `generate_run.log`. La biblioteca contiene 5000 archivos `sample_*.npy`;
   `params_table.csv` describe parámetros y `x_grid.npy` el eje de pérdidas.

Las figuras de origen son datos digitalizados, no mediciones numéricas originales.
Para CaMnO3 hubo calibración de ejes confirmada por el usuario; no debe presentarse
la extracción como totalmente automática. Las bitácoras guardan las decisiones.

## Entorno científico

El entorno usado en las sesiones es conda `Claude_AIOG`, Python 3.10. Dependencias
registradas: brixs (incluido brixs.multiplet), numpy, scipy, matplotlib, lmfit,
h5py, scikit-learn y joblib. El código resuelve `quanty_win/Quanty.exe` respecto del
repositorio. Se necesita Windows para ese binario. Las versiones exactas no estaban
fijadas en la documentación original; por eso no se certifica reproducción desde
un entorno limpio. Un modelo joblib puede depender de la versión de scikit-learn
usada al guardarlo.

Todos los comandos siguientes se ejecutan desde la raíz. Los scripts científicos
pueden sobrescribir sus salidas existentes: para repetir experimentos conservando
la evidencia original, trabajar en una copia independiente del repositorio.

## Regenerar solamente el informe

Requiere `reportlab`; no importa los módulos científicos ni ejecuta Quanty.
Para generar y verificar el PDF sin modificar el entorno científico, se pueden
instalar las herramientas en la carpeta local ignorada por Git:

```powershell
python -m pip install --target .report_tools -r docs/report/requirements.txt
```

El generador y el verificador reconocen esa carpeta automáticamente.

```powershell
python code/build_report.py
python code/verify_report.py
```

Fuente editorial: `docs/report/report_content.json`. Salidas: `index.html`,
`index.pdf` y `build_manifest.json`. La generación comprueba que el contenido cabe
en cinco páginas y registra SHA-256 de fuentes, figuras y salidas. Las dos figuras
se reutilizan de resultados guardados; no se recalculan ni alteran los datos.
El historial Git conserva la versión extensa anterior del HTML.
El verificador comprueba el número de páginas, la presencia de cada párrafo, los
enlaces locales, los checksums y el inventario de espectros; también renderiza las
páginas para inspección visual. Sus resultados y las versiones instaladas al
momento de esta revisión quedan en `verification/report_delivery/checks.json`.
Ese inventario de versiones no prueba cuáles se usaron al entrenar originalmente.

## Puntos de entrada XAS

```powershell
python verification/grid_nlls_self_test/self_consistency_test.py
python verification/grid_nlls_self_test/self_consistency_test_v2.py
python verification/grid_nlls_self_test/grid3d_MnO_v2.py
python verification/grid_nlls_self_test/grid_LiMnO2_wide.py
python verification/grid_nlls_self_test/forward_check_Mn2O3.py
```

La herramienta configurable para otros casos es `code/grid_fit_spyder_template.py`;
el ejemplo `code/grid_fit_example_black.py` y su salida en
`verification/digitize_spectra/spyder_fit_output/` documentan una ejecución previa.
Los tests sintéticos verifican consistencia interna. Los casos experimentales
requieren además evaluar límites de parámetros, residuos y supuestos físicos.

## RIXS: generación, entrenamiento y prueba pendiente

```powershell
python code/rixs_generate_library.py
python code/rixs_train_nn.py
python code/rixs_test_predictions.py
```

- Generación: Latin Hypercube, semilla 42, energía incidente fija 643,8 eV. La tabla
  de parámetros y el manifiesto permiten retomar. Ya terminó: no es necesario
  repetirla para leer el informe. Los archivos de calibración de resonancia son
  antecedentes y no se utilizan en el flujo final.
- Entrenamiento: recorte de pérdidas >=1 eV, normalización al máximo recortado,
  objetivos escalados a sus rangos, partición 90/10 con semilla 0. Reanuda desde
  `mlp_checkpoint.joblib` y `mlp_checkpoint_meta.json`. Como ya hay 60 bloques,
  volver a invocarlo no inicia un entrenamiento nuevo. Un nuevo entrenamiento
  debe prepararse en una copia sin esos checkpoints, conservando los originales.
- Prueba pendiente: el script actual genera 30 espectros nuevos con semilla 999
  y una condición de ruido Poisson de 2000 cuentas. Produce métricas por parámetro
  y gráficos de paridad. Aunque su docstring menciona reconstrucciones espectrales,
  el código actual no las implementa; eso deberá añadirse en la próxima etapa.

No se ejecutó esa prueba durante esta actualización. La evaluación consultada
en cada bloque del entrenamiento no reemplaza una prueba independiente.

## Lectura crítica de los resultados

- MnO muestra buen acuerdo, pero las grillas fueron guiadas por exploraciones
  previas: no se presenta como una prueba ciega independiente.
- El mejor 5 % de una grilla no define por sí mismo intervalos de confianza.
- LiMnO2 tiene límites activos; Mn2O3 usa una aproximación geométrica y no recupera
  las proporciones publicadas. Una forma total correcta no valida su descomposición.
- Para la curva verde, LMCT mejora SSE con anchos aún en el tope y V en un borde.
- Los barridos LMCT originales de la curva negra requieren repetición con límites
  consistentes antes de comparar SSE bajo el criterio de 0,9 eV.
- Dos referencias reales de Mn4+ no justifican una afirmación universal sobre
  todos los óxidos; el intento de forzar Mn4+ en una muestra de valencia incierta
  tampoco cuenta como un tercer compuesto de Mn4+ confirmado.

## Publicación

Destino configurado: `https://github.com/joaquingajst/mn-xas-multiplet-fit`.
Se incluyen el informe, sus fuentes, el código, los datos y resultados guardados,
incluido el checkpoint RIXS y sus métricas. El historial conserva la procedencia
y las versiones previas. La autorización para publicar esta entrega no implica
haber ejecutado las tareas científicas pendientes.
