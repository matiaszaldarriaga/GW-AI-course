# Reproducción y auditoría

Dependencias exactas en `requirements.txt`. Entorno comprobado: Python 3.14 en Windows y MiKTeX con `pdflatex`. Para generar el PDF hace falta una distribución LaTeX, como MiKTeX o TeX Live. Las rutas se resuelven desde cada script, sin depender de una carpeta personal. La reproducción del ajuste usa decisiones y tiempos congelados; las decisiones humanas no se regeneran automáticamente.

```powershell
python -X utf8 scripts/reproduce.py
python -m unittest discover -s tests
python -X utf8 scripts/build_report.py
python -X utf8 scripts/audit_delivery.py
```

La auditoría comprueba hashes de entradas, 847 identidades, 525 eventos, pesos unitarios, fondo cero, ausencia de corridas previas, normalización individual y coincidencia con el ajuste adoptado. El paquete incluye todos los estados, no solo los aceptados. Las tablas comprimidas preservan decisiones de las corridas previas y metadatos de exclusión por 300 muestras.

## Verificar el original y repetir simulaciones

```powershell
python -X utf8 scripts/reproduce.py --txt "RUTA_AL_RESPALDO/Datos/Med_con_Decaimientos/decaimientos.txt" --simulate
```

La opción `--txt` verifica el SHA-256, los 847 bloques, eje temporal, clasificación automática de todas las semillas y los 525 tiempos contra las muestras originales. No modifica el TXT ni suma eventos anteriores. La opción `--simulate` repite las 3000 realizaciones condicionales con la semilla registrada y comprueba que coincide la validación conservada. Sin esa opción se reutiliza la validación exacta existente; no se presenta como una ejecución nueva.

`build_report.py` genera el único HTML y PDF conjunto (cinco páginas). El PDF se compila dos veces con `pdflatex` desde `output/latex/proyecto_muones.tex`; las figuras relativas acompañan al fuente y permiten compilarlo en Overleaf. Los archivos auxiliares quedan en `tmp/latex/`. El HTML usa otra organización, lleva cuatro imágenes incorporadas y ofrece un selector con siete comparaciones de ventana ya calculadas; no necesita internet para mostrar el informe. Los enlaces bibliográficos sí son externos. `--prepare-only` prepara HTML, figuras y LaTeX sin compilar; `--finalize-only` registra hashes después de una compilación externa.

El componente CCD procede de la rama `identificador`, commit `fd262213fcaab221b771617b49f47769f9e1c83c`. `data/ccd_inputs_manifest.json` protege por separado las diez fuentes conservadas y su resumen. El constructor comprueba esos hashes y reproduce la figura de composición a partir de los conteos documentados; no vuelve a calibrar imágenes, entrenar la red ni calcular métricas de clasificación porque faltan los originales y las tablas completas de validación. Los resultados de composición, validación neuronal y comparación híbrida conservan sus denominadores distintos. [La integración](INTEGRACION_DOS_ANALISIS.md) describe este alcance.

Para comprobar cambios de presentación, renderizar las páginas del PDF con Poppler y revisar visualmente textos, tablas y figuras. La auditoría estructural comprueba cantidad de páginas, texto, autoría, enlaces locales, normalización del histograma y ausencia de informes duplicados; no reemplaza esa revisión visual. `results/visual_qa.json` documenta la inspección de las cinco páginas y del HTML en Chrome, incluidos el diseño estrecho y las siete opciones del selector. Si se modifican los entregables, repetir esa inspección y actualizar sus hashes antes de auditar.

El respaldo conserva el árbol previo íntegro, incluyendo informes y archivos fuente de referencia. Un manifiesto local verifica su contenido antes y después de ordenar. La ubicación personal se guarda solo en `.local_backup.json`, ignorado por Git; no es dependencia del repositorio.
