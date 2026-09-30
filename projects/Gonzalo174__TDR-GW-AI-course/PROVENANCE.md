# Procedencia

De dónde viene cada resultado de este repositorio: qué archivo y qué función lo
produjo, qué entró, qué se escribió acá y qué se llamó de una librería, y qué
alternativa defendible se descartó en cada bifurcación.

El criterio para incluir algo acá es que tenga una alternativa razonable. Lo que
no tiene alternativa es implementación, y se lee en el código.

---

## 1. La cadena de datos

```
base real (privada)                    este repositorio
/data1/.../gon3/DB                     DB/
  UniProt, InterPro, OrthoMCL,   ──►     solo enteros, 260 MB
  ids internos, 2 396 103                831 175 compuestos
  compuestos
        │                                     │
        │  acondicionarDB/acondicionar.py     │  comun/tdr.py::cargar_db
        │  (fuera de este repo)               ▼
        │                              analiceDB/ genome_prioritization/ huerfanas/
        ▼                                     │
  mapeos/ (privado, no se publica)            ▼
                                       resultados/<analisis>_out/
                                         tablas + NN_meta.json
                                              │
                                              │  comun/figuras.py (sin tocar la base)
                                              ▼
                                       resultados/<analisis>_out/figuras/
                                              │
                                              ▼
                                       verificacion/10_equivalencia.ipynb
                                         contra oraculo_v4/
```

Cada corrida deja un `NN_meta.json` al lado de sus tablas con la fecha, el
notebook de origen, los parámetros, la fecha de cada tabla de `DB/` y las
versiones de python y pandas. Lo escribe `tdr.escribir_meta`.

## 2. Decisiones sobre los datos

Las tomó `acondicionarDB/` antes de este repositorio; se documentan porque
condicionan todo lo que sigue.

| decisión | qué se hizo | alternativa descartada |
|---|---|---|
| **recorte** | se eliminan las componentes conexas del grafo cluster–cluster de fingerprint que no contienen ningún cluster con bioactividad `positive`: 2 396 103 → 831 175 compuestos (34.7 %). Los 135 576 con bioactividad positiva sobreviven todos | publicar la base entera: 941 MB de aristas, inviable en un repositorio |
| **codificación** | toda notación propia pasa a entero consecutivo asignado en orden aleatorio con semilla fija (20260908), para que el orden de los códigos no filtre el de los identificadores | publicar los identificadores reales, que es lo que se quiere evitar |
| **empaquetado** | la tabla de aristas va partida en dos `.csv.gz` de 86.5 y 85.9 MB, con las 36 152 622 aristas completas | subir el umbral de peso hasta que entre en un archivo: cuesta compuestos (a umbral 83 se pierden 144 369) |
| **peso** | entero ×100 (0.82 → 82); se descarta `weight_error`, vacía en el 78 % de las aristas y con máximo 0.005, que escalado ×100 redondea a 0 | conservarla: no llevaba información |

## 3. Decisiones del port

Todas verificables en el código, con el comentario al lado.

| # | decisión | por qué, y qué se descartó |
|---|---|---|
| 3.1 | Los códigos que el modelo necesita se escriben a mano en `comun/tdr.py` (`TAG_POSITIVE = 2`, `IPR_DOMAIN = 5`, …) | **descartado:** publicar los diccionarios de `mapeos/`, que es justamente lo que la codificación evita. Escribir cinco constantes cuesta menos que publicar 400 000 filas de correspondencias |
| 3.2 | `SPECIES` nombra a las 16 especies: cada código lleva su organismo (`26` → *Plasmodium falciparum*) además del tipo (grupo, reino, parásito). El código sigue siendo la clave en `DB/`, `control/` y `resultados/`; el nombre es la etiqueta | el modelo contrasta parásitos contra no parásitos y procariotas contra eucariotas: sin el tipo, las figuras por grupo no se leen. Sobre el nombre, ver 3.14 |
| 3.3 | Al concatenar InterPro y OrthoMCL se repone un prefijo (`IP…`, `OG…`) | los dos vocabularios se codificaron por separado desde 0 y sus códigos se pisan: los 14 083 dominios caen dentro del rango de OrthoMCL. **Descartado:** desplazar OrthoMCL por un offset, que arregla la colisión pero no repone lo que `nucleo.get_annot_druggability_pv` necesita, que es distinguirlos por prefijo |
| 3.4 | `nucleo.py` se modifica en **una** línea: `"_".join(map(str, sp_out))` | arma la clave de un diccionario de salida, no interviene en ningún cálculo. **Descartado:** convertir los códigos a texto en toda la cadena, que reintroduce el problema que la codificación resuelve |
| 3.5 | Las rutas se derivan de la raíz del repositorio, buscando hacia arriba la carpeta que contiene `DB/` | la consigna pide que el repositorio lo pueda reproducir alguien que nunca habló con nosotros. **Descartado:** una variable de entorno, que es una cosa más que puede faltar |
| 3.6 | `nombres_ipr()` lanza `NotImplementedError` | nombrar un dominio exige `mapa_interpro`, que es privado. Se prefiere fallar diciendo por qué antes que devolver códigos disfrazados de nombres |
| 3.7 | Los outputs guardados de los notebooks se limpiaron antes de correr | traían los resultados de la versión anterior, calculados sobre otra base: dejarlos mezclaría dos corridas en un mismo archivo |
| 3.8 | El faltante de `lambda_` (que marca el modo híbrido) se rotula `"nan"` a mano, no con `astype(str)` | en pandas 3 `astype(str)` **conserva** el faltante en vez de convertirlo a la cadena `"nan"`, y entonces `sorted` compara `str` contra `float` y matplotlib rechaza el valor. Se escribe explícito, que funciona igual en pandas 2 y 3 |
| 3.9 | La columna de especie que sale del nombre de archivo se convierte a entero cuando son todos dígitos | antes los códigos eran texto y la comparación funcionaba por accidente; con códigos numéricos, `especie == SP_FOCO` comparaba `"26"` contra `26` y no encontraba nada |
| 3.10 | `cargar_subestructuras_crudas` recodifica los ids de `raw_data/` a los códigos de `DB/` | sin eso las salidas no cruzan contra `datos.bioact` y el conjunto llega vacío a `huerfanas/` sin error: la lista de compuestos promiscuos salía con 30 filas falsas en lugar de los compuestos verdaderos |
| 3.11 | Las figuras se dibujan en `<carpeta>/figuras_<analisis>.py` y **sólo leen tablas** de `resultados/`; cada una declara cuáles (`python comun/figuras.py --lista`), y la corrida guarda todo lo que una figura necesita (p. ej. `02_ranking_26.csv` para la ROC, `01_control_v5.csv`) | regenerar una figura costaba la corrida entera: varias dependían de variables en memoria o se dibujaban antes de la corrida, y todas exigían cargar la base. **Descartado:** guardar los objetos intermedios en `pickle`, que acopla las figuras a versiones de pandas y no se puede leer ni comparar contra el oráculo. Al redibujarlas desde las tablas, tres figuras de la corrida anterior resultaron rotuladas con el código crudo (`0`, `1`, …) en lugar del nombre; en las dos matrices especie × especie la causa es que los encabezados leídos del CSV son texto y la búsqueda en `NOMBRE_CORTO` fallaba en silencio. Las figuras nuevas convierten el encabezado antes de buscar |
| 3.12 | Las tablas de `resultados/` (~50 MB) y sus `NN_meta.json` se versionan; las figuras no | quien corrige tiene que poder comprobar figuras y cifras sin pagar ~45 min de corrida con 20 procesos: con las tablas, `make verificar` lo hace en ~1 min. En un clon sin ellas no se regeneraba ninguna figura y la receta de entregables reescribía el informe con «??»; ahora `numeros.py` y `generar_pagina.py` se niegan a escribir si falta un dato. **Descartado:** versionar también las figuras, que se regeneran desde las tablas y duplicarían 30 archivos binarios; y no versionar nada, que dejaba la verificación atada a la corrida completa |
| 3.13 | El cálculo de la lista de promiscuos sale de `analiceDB/03` a `datos_externos/promiscuidad/derivar.py`, y su salida (5 compuestos y dos tablas agregadas) se versiona como insumo; `analiceDB/03` la transcribe y mide su efecto sobre `DB/` | así ningún notebook necesita datos privados y toda la corrida se reproduce desde el repositorio. `derivar.py` reproduce las tres tablas byte a byte. **No se publica** la tabla por compuesto (peso molecular de ~84 000 compuestos al lado de su código): con esa precisión el peso molecular reidentifica el compuesto y deshace la codificación. **Descartado:** publicar las relaciones de subestructura y los pesos ya codificados para calcular la lista dentro del repo, por el mismo riesgo |
| 3.14 | **Se revierte el anonimato de las especies**, y sólo el de las especies: los 16 nombres se escriben en `SPECIES` y pasan a las etiquetas de figuras y a la columna `nombre` de las tablas. Salen de cruzar `mapeos/mapa_especie.csv` contra `raw_data/genomes/genome_data.csv`, y son la única parte de los diccionarios privados que se publica | los códigos hacían el resultado ilegible: «sp26 (Protozoos, parasito)» no dice que el caso de aplicación es la malaria, ni que los tres kinetoplástidos son *T. cruzi*, *T. brucei* y *L. major*, ni que el contraste es contra *H. sapiens*. Y el anonimato ya era nominal: 3.2 admitía que el par (grupo, parásito) identificaba a tres de las 16. **No cambia la exposición de los compuestos**, que es lo que protege la codificación (3.13): los mapeos de compuesto, blanco, cluster, InterPro y OrthoMCL siguen sin publicarse. **Descartado:** recodificar `DB/` y `control/` con el nombre como identificador, que rompe la comparación byte a byte contra la corrida v5 y obliga a rehacer la corrida entera para un cambio de rótulo |

| 3.15 | **Se revela el accession de InterPro de 391 dominios**: los de quinasa, en `tdr.ANN_QUINASA`, con el accession al lado de cada código. El análisis usa sólo el código; el accession está para auditar la marca. `datos_externos/quinasas/derivar.py` la regenera desde el catálogo de InterPro y el mapeo privado | `genome_prioritization/03` pregunta qué le hace β a una categoría grande y promiscua, y qué dominio es de quinasa no se puede decidir desde `DB/`: `ann` es un entero y los nombres no se publican (3.6). Sin la marca no hay análisis. **Costo aceptado:** esos 391 códigos quedan desanonimizados; los otros 36 533 accessions, y todo mapeo de compuesto, blanco o cluster, siguen sin publicarse. **Descartado:** versionar la lista como insumo externo en `datos_externos/`, como la de promiscuos (3.13) — es chica y estable, y esconderla en un CSV no la hacía menos pública, sólo más difícil de auditar; y publicar el nombre del dominio además del accession, que no agrega nada al análisis porque las quinasas se miran como grupo |
| 3.16 | **Se corrige un error del modelo, heredado de v4**: al armar la semilla de una droga, `nucleo.get_druggable_targets` buscaba sus vecinos químicos en `ddt` (fingerprint) y `dds` (subestructura) con el `drug_id` de la droga y de sus *cluster-mates*, pero esas tablas unen **clusters** identitarios (`clusID1/clusID2`, `from/to` son `cluster_id`). Ahora se consulta con los `cluster_id` de esas drogas. Un único salto en la capa química, como antes; las demás reglas del núcleo no se tocaron. Lo justifica `comun/tests/test_vecinos.py`, que con datos sintéticos arma un cluster señuelo con el mismo número que la droga: falla con el código anterior (2 fallas, 1 error) y pasa con el nuevo. Se encontró y corrigió primero en `TDR_2026_v4`, y se portó acá el 2026-09-24 (`historia/README_GWAI_correccion_semilla.md`) | el error venía de `nds_fun.R`, escrito cuando esas aristas eran droga–droga, y se tradujo tal cual. **No fallaba**: las numeraciones se solapan (compuestos 0–831 174, clusters de fingerprint 0–769 636, de subestructura 0–788 536), así que buscar el compuesto 12 345 como cluster 12 345 devolvía los vecinos de **otro** cluster. Sólo afecta a `huerfanas/` (01–04, salvo el embudo) y a lo que las lee; `genome_prioritization/` arma la semilla sin `doi` y no pasa por esa rama, y los *cluster-mates* ya usaban `tclus`/`sclus` bien. **Descartado:** agregar un segundo salto en la capa química, que se probó en v4 y casi no mueve la recuperación (*A. thaliana*: 22.3 → 23.1 %) |
| 3.17 | En `huerfanas/04` se iguala el tipo de `target_id` antes de cruzar las sugerencias con sus anotaciones | `tdr.anotar_targets` devuelve el `target_id` de `sta` (texto) y el ranking lo tiene entero. Es la misma clase de falla que las de §3 (un entero contra el texto que solía ser), pero en un camino que nunca se había ejecutado: hasta la corrección de 3.16 no había ninguna sugerencia bajo r*G. Esta sí lanzaba una excepción. **Descartado:** cambiar el tipo en `tdr.anotar_targets`, que usan otros análisis |
## 4. Qué es código propio y qué es librería

| pieza | de dónde sale |
|---|---|
| modelo de propagación (`nds`, `get_druggable_targets`, `rs`) | `comun/nucleo.py`, propio, congelado salvo 3.4 y 3.16 |
| test exacto de Fisher | `scipy.stats.fisher_exact` |
| corrección por comparaciones múltiples | `statsmodels`, método `fdr_bh` |
| ROC y AUC | `sklearn.metrics.roc_curve`, `auc`, `roc_auc_score` |
| **pAUC normalizada y corrección de McClish** | `comun/tdr.py`, propio. `sklearn` no trae pAUC parcial con interpolación en el borde |
| bootstrap de AUC01 | `comun/tdr.py`, propio, 2 000 remuestreos con `numpy.random.default_rng` |
| componentes conexas del grafo químico | `networkx` |
| paralelización | `comun/tdr.py::paralelizar`, sobre `concurrent.futures` con contexto `fork` |

Dos detalles del código propio que tienen alternativa y por eso se explican:

**pAUC con interpolación en el borde** (`tdr.pauc_normalizada`). Se agrega el
punto exacto `(fpr_max, tpr(fpr_max))` antes de integrar. Truncar en el último
punto con `fpr <= fpr_max`, que es lo directo, **subestima** la pAUC.

**Corrección de McClish** (`tdr.mcclish`). Reescala la pAUC normalizada para que
azar dé 0.5 y clasificador perfecto 1.0, que es lo que hace comparable el número
entre especies con distinta proporción de positivos.

## 5. Cómo se verifica cada resultado

Tres niveles, del más barato al más caro.

**Las pruebas** (`comun/tests/`, 63, corren en ~25 s). Integridad de las tablas,
ausencia de fuga en el leave-one-species-out, métricas contra valores de
referencia, rutas, y el entorno. Cuatro son específicas del port y cubren lo que
puede romperse en silencio: que el filtro de positivos no quede vacío, que la
base sea entera, que los dos vocabularios no se pisen y que la base esté
completa.

**El control externo** (`control/genoma_completo_v5/`). Óptimos por especie
calculados en una corrida independiente con la métrica ya corregida.
`genome_prioritization/02` los contrasta contra los propios.

**El oráculo** (`oraculo_v4/` y `verificacion/10_equivalencia.ipynb`). Las mismas
tablas calculadas antes del recorte y de la codificación. La comparación explota
una asimetría, y el criterio es uno solo: **si el análisis toca la capa química,
el recorte lo mueve; si no la toca, no lo mueve**. El recorte elimina compuestos,
es decir nodos y aristas de esa capa; no toca proteínas ni anotaciones.

| análisis | carga | esperado |
|---|---|---|
| `genome_prioritization/` | `cargar_db(anotaciones=True)`, sin química | **estable** |
| `analiceDB/` | describe la base entera, componentes incluidas | cambia |
| `huerfanas/` | `quimica=True`; su notebook 03 lee las salidas del 01 | cambia |

Una corrección al criterio que había escrito antes: agrupé `huerfanas/` con
`genome_prioritization/` como «no debería moverse», y está mal. `huerfanas/`
construye la semilla desde el vecindario químico de cada droga, así que el
recorte la mueve necesariamente. El tamaño de la muestra es el mismo (7 782
pseudohuérfanas en los dos lados), pero antes de la corrección de §3.16 la semilla
nula difería: 83 % en v4 y 69 % acá.

**La causa era el error de §3.16, no el filtro de promiscuidad.** La primera
lectura fue que el filtro descartaba menos compuestos (de 25 a 5, porque 20 no
sobrevivieron al recorte; las tablas decían 30 y 7 porque tenían filas
duplicadas), pero medido sobre la base (`analiceDB/03_impacto_en_la_base.csv`)
el filtro saca 5 compuestos y **ninguna** arista de la capa de subestructuras de
`DB/`: no podía mover la semilla. Con el error, la semilla de un compuesto
dependía de qué cluster tenía su número, y la codificación renumeró compuestos y
clusters; los clusters «equivocados» eran otros. Con la semilla corregida
(2026-09-24) la predicción era que las semillas coincidieran con las de v4
corregida para los mismos compuestos, y se cumple. Control hecho fuera del
repositorio, porque cruzar los ids exige `mapa_compuesto`, que es privado:

| | v4 corregida | este repositorio |
|---|---:|---:|
| semilla nula | 67.2 % | 67.8 % |
| semillas informativas | 1 383 | 1 365 |
| recuperadas (frank < 0.1) | 17.7 % | 17.5 % |
| r*G | 80 | 76 |
| sugerencias para *P. falciparum* | 2 compuestos → 1 blanco | los mismos 2 compuestos → el mismo blanco, con el mismo puntaje y rG |

- En los 5 218 compuestos que comparten las dos muestras, la clase de semilla
  coincide en el 100 %; frank y rSS, en todos salvo uno (*O. sativa*, puesto 59
  contra 56, por el desempate con los pesos redondeados de la base codificada).
- En los 10 organismos con menos de 1 000 pseudohuérfanas, donde las dos
  muestras son el conjunto completo, el porcentaje de semilla nula y de
  recuperación por organismo es idéntico. Las diferencias del total vienen de
  los 6 organismos muestreados: el sorteo de 1 000 depende del orden de los ids,
  que la codificación cambió.
- La corrida anterior de este repositorio (con el error) queda en el historial:
  `git show e3afdb0:resultados/huerfanas_out/01_resumen_frank.csv`.

## 6. Lo que no se puede reproducir desde este repositorio

Se dice explícitamente, porque un repositorio que calla sus límites no es
verificable:

- **la base misma**: `acondicionarDB/` lee la base real, que no se publica. Lo
  que sí se publica es su salida y el registro de cómo se produjo;
- **los nombres de las anotaciones** (3.6);
- **la identidad de compuestos, blancos, clusters y anotaciones**: por diseño.
  La de las especies sí se publica desde 3.14;
- **la lista de compuestos promiscuos**: se calcula desde relaciones de
  subestructura crudas y un diccionario privado, en
  `datos_externos/promiscuidad/derivar.py` (rutas `TDR_RAW` y `TDR_MAPEOS`); su
  salida se versiona como insumo y ningún notebook lee datos crudos (3.13).
