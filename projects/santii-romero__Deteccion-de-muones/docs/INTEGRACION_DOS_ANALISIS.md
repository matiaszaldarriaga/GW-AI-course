# Integración de los dos análisis

Orden del usuario del 28-09-2026: producir un PDF y un HTML conjuntos y aplicar las preferencias editoriales guardadas. El usuario confirmó que no dispone de los datos originales ni de las tablas completas de validación del CCD; para el montaje docente pidió usar solo disposición y datos confirmados.

## Fuentes y alcance

- Aclaración posterior del usuario: el Laboratorio Lambda proporcionó los datos del detector. No se afirma que se adquirieron allí. La identificación con Atucha-II del análisis histórico permanece en las fuentes conservadas como inferencia; en el relato actual su bibliografía se usa como referencia instrumental, sin certificar el detector de origen.
- Etapa temporal: configuración y evidencia congeladas de `main`, base publicada `18e44169c37e157adf04c5205da9a860dae36a02`. Solo los 525 retardos de la adquisición independiente; pesos uno, fondo cero, límite inferior 120 ns y final individual menos 10 ns. No se agregan las corridas previas ni datos de 300 puntos.
- Etapa espacial: `identificador`, commit `fd262213fcaab221b771617b49f47769f9e1c83c`. Se preservaron diez fuentes documentales y de código con hashes en `data/reference/ccd/`, y se extrajo su síntesis en `data/derived/ccd_summary.json`. Su integridad se protege separadamente en `data/ccd_inputs_manifest.json`; no se altera el manifiesto temporal ni su comprobación original.
- El CCD corresponde a la identificación instrumental inferida por el análisis previo mediante geometría y bibliografía. No se certifica nuevamente la procedencia de las imágenes. No se volvieron a calibrar imágenes, entrenar la red ni calcular métricas sobre datos ausentes.

## Denominadores separados

| Producto conservado del CCD | Muestra | Interpretación |
| --- | --- | --- |
| Composición y resumen energético | 30 imágenes, 6251 trazas | Etiquetas y depósitos del subconjunto conservado; versión exacta de generación no verificada nuevamente |
| Validación de la red v2 | 300 imágenes, 15434 trazas de referencia | Métricas contra etiquetas automáticas |
| Comparación híbrida | 75 archivos, 15554 trazas | Acuerdo con las reglas; distinto producto de evaluación |
| Controles sin agrupamiento de columnas | Nueve imágenes en FITS/ROOT equivalentes | Los formatos no duplican la muestra experimental |

La clase alfa no aparece en el resumen de 30 imágenes; en la validación de la red tiene nueve ejemplos. No se confunden esos conteos. Las 300 lecturas por píxel del CCD no son las formas de onda de 300 puntos excluidas del análisis con centelladores. La exposición de 32-37 minutos y la discrepancia de flujo quedan como inferencias y limitaciones anteriores, no como nueva medición de eficiencia.

## Cambios de presentación

- Revisión vigente: se retira «Laboratorio 5» de la portada y de la referencia docente en ambos formatos. El PDF tiene título de 16 pt, nombres con separación normal y los dos correos sin enlaces en una línea debajo: `theo.del.compare@gmail.com` y `romerosantiago545@gmail.com`. El HTML conserva su presentación. Esta revisión no cambia resultados, gráficos ni secciones.
- Revisión posterior: cuatro secciones principales en el PDF, dedicadas al objetivo y comparación esperada, centelladores, detector con datos proporcionados por Lambda y discusión conjunta. Subapartados agrupan método y resultados dentro de cada análisis. El HTML mantiene su navegación detallada propia.
- Se retiró la fecha de emisión de ambos entregables. Los nombres enlazan a los correos indicados por los autores y se reconoce la ayuda de Claude (Anthropic) y Codex (OpenAI). Las fechas de adquisición y de referencias siguen describiendo datos y fuentes, sin actuar como fecha del informe.
- Un informe académico de cinco páginas compilado con LaTeX y un HTML autónomo de estructura distinta. Ambos conservan los integrantes Theo Del Compare y Santiago Romero.
- Montaje docente descrito en texto, con barra de plomo; dimensiones no disponibles. Ningún esquema experimental se incorpora.
- Relato y gráficos sin nombres de mediciones ni claves individuales; los registros técnicos conservan sus identificadores.
- Nuevo histograma en intervalos uniformes de 80 ns, con predicción integrada por ventana individual y leyenda exterior. La suma de datos y predicción es 525; no se reajusta por los bins.
- El gráfico anterior se conserva byte por byte en `data/reference/temporal/lifetime_previous.png`. `data/report_changes_manifest.json` enlaza su hash original con el gráfico reconstruido; el manifiesto temporal de migración y la verificación contra los datos permanecen intactos.
- Nuevas figuras de formas de onda por categoría y composición del CCD. La ilustración espacial anterior se reutiliza sin alterar sus píxeles; la gráfica espectral antigua no se redibuja sin datos numéricos.
- La vida media y sus intervalos no cambian. La discusión distingue escala temporal condicionada, captura posible en materiales y clasificación morfológica sin pureza calibrada.

## Reproducción

`scripts/build_report.py` usa `report_joint.py`, `report_html.py` y `templates/report.tex`. La carpeta `output/latex/` contiene un fuente portable y sus figuras, compilables también en Overleaf. No depende de rutas personales ni de la copia de Git usada para descargar el detector.

La auditoría verifica ambas cadenas de procedencia, los conteos del CCD, la conservación del ajuste temporal, los cuatro gráficos incorporados, ausencia de esquema e identificadores en el relato, productor LaTeX del PDF y cinco páginas. La inspección visual final y la comprobación del HTML quedan en `results/visual_qa.json`.

Los originales permanecen intactos y fuera de la entrega. Los entregables anteriores tienen su versión conservada en el commit de publicación y en la preparación local; solo los entregables conjuntos vigentes se mantienen como PDF/HTML activos.
