# Campos de gauge y el espectro de ondas gravitacionales del recalentamiento

Proyecto final de *Ondas gravitacionales e investigación asistida por IA*
(UBA, 2026). Consigna del curso: [`final-project.html`](https://matiaszaldarriaga.github.io/GW-AI-course/final-project.html).

> **Versión publicada:** <https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/>
> (la página del proyecto; también el [informe definitivo](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/informes/informe-definitivo.pdf) en PDF de 5 páginas,
> el [informe extendido](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/informes/informe-extendido.pdf)
> y la [bitácora](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/bitacora.html)).

> **¿No sos de física?** Empezá por la [bitácora](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/bitacora.html): cuenta
> el proyecto desde cero, qué se hizo, qué se aprendió y por qué importa, con
> un glosario al final.

## Índice

**En este README**

1. [En palabras simples](#en-palabras-simples)
2. [La pregunta](#la-pregunta)
3. [Enfoque](#enfoque)
4. [Resultados](#resultados-28-de-septiembre-de-2026-proyecto-terminado)
5. [Organización del repositorio](#organización-del-repositorio)
6. [Cómo reproducirlo](#cómo-reproducirlo)

**Páginas y documentos** (en orden de lectura sugerido; los enlaces abren la versión publicada)

| | documento | qué es |
|---|---|---|
| 1 | [Bitácora](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/bitacora.html) | el proyecto contado desde cero, en lenguaje llano, con glosario. **Para empezar si no sos de física.** |
| 2 | [Página del proyecto](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/final-project.html) | presentación completa: pregunta, resultados, conclusiones y cómo se verificó cada uno. |
| 3 | [Informe definitivo (PDF, 5 págs.)](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/informes/informe-definitivo.pdf) · [HTML](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/informe-definitivo.html) | el informe final pedido. |
| 4 | [Informe extendido (PDF)](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/informes/informe-extendido.pdf) | la página del proyecto entera, en PDF. |
| 5 | [¿Qué es CosmoLattice?](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/what-is-cosmolattice.html) | introducción al código de simulación. |
| 6 | [Bases teóricas de los modelos gauge](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/bases-teoricas-modelos-gauge.html) | variables de programa, condiciones iniciales y ley de Gauss. |
| 7 | [Análisis de parámetros](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/analisis-parametros.html) | cómo se eligieron parámetros comparables para los tres modelos. |
| 8 | [Piloto del control `lphi4`](https://tomasciccarella.github.io/GWs-IA-Final---CosmoLattice-studies-with-gauge/paginas/piloto-lphi4.html) | la primera simulación y su validación contra Dufaux et al. (2007). |

## En palabras simples

Al terminar la inflación, el campo que la impulsó (el *inflatón*) quedó
oscilando y le pasó su energía a otros campos de forma violenta. Esa etapa se
llama *recalentamiento*, y agitó el espacio lo suficiente como para producir
ondas gravitacionales. Casi todos los estudios suponen que la energía va a
campos "simples" (escalares). Este proyecto simula qué pasa cuando va a
**campos de gauge**, los que transmiten fuerzas como el electromagnetismo, y
mide cuánto cambia la "huella" de ondas gravitacionales que queda.

## La pregunta

El recalentamiento posterior a la inflación genera un fondo estocástico de
ondas gravitacionales, a partir del estrés anisotrópico de configuraciones de
campo clásicas e inhomogéneas en la red. Casi todo lo publicado sobre esto usa
sólo campos escalares. Cuando el contenido de campos incluye un campo de gauge,
porque el inflatón (o un campo espectador) tiene carga bajo algún grupo de
gauge, la energía-momento del propio campo de gauge contribuye a ese estrés. Y
la dinámica de los campos de gauge (tubos de flujo, producción taquiónica de
bosones de gauge, etc.) puede ser muy distinta de la autorresonancia escalar.

**El proyecto pregunta cuánto de la forma del espectro de ondas
gravitacionales (frecuencia y altura del pico, pendientes a cada lado) se
debe al campo de gauge, manteniendo fijo el resto del modelo.**

## Enfoque

[CosmoLattice 2.0](https://cosmolattice.net/) (Baeza-Ballesteros, Figueroa,
Florio, Loayza, Sattler, Torrentí y Urio, arXiv:2607.24978; teoría en
arXiv:2006.15122 y arXiv:2512.15627) trae tres modelos relacionados que
permiten una comparación controlada sin escribir un modelo nuevo:

| modelo | contenido de campos |
|---|---|
| `lphi4` | un escalar real con potencial λφ⁴ y un campo hijo escalar; sin campo de gauge. **El control.** |
| `lphi4U1` | el mismo tipo de potencial, ahora con un escalar complejo cargado bajo un campo de gauge U(1) (electrodinámica escalar / Higgs abeliano). |
| `lphi4SU2U1` | un doblete escalar con carga SU(2)×U(1), parecido al sector electrodébil: dos campos de gauge en lugar de uno. |

Los valores por defecto de los `.in` de CosmoLattice **no** hacen una
comparación justa: los modelos arrancan con energías distintas y con
resonancias de distinta intensidad. El análisis en
[`paginas/analisis-parametros.html`](paginas/analisis-parametros.html) fija parámetros
comparables, y las decisiones quedaron confirmadas el 22 de septiembre de 2026:

- **λ = 9×10⁻¹⁴** en los tres modelos, con el inflatón arrancando en el estado
  exacto de fin de la inflación.
- **Un único canal resonante con q = 120** en cada modelo: el hijo escalar en
  `lphi4`, el campo U(1) en `lphi4U1`, y los dos campos gauge juntos en
  `lphi4SU2U1` (q_A = q_B = 60, porque según el Art I resuenan con la suma;
  hijos escalares apagados).
- **La misma red física en los tres.** Por un factor √2 en las unidades del
  código, `kIR` y `kCutOff` se multiplican por √2 en los modelos gauge, y `dt`
  y `tMax` se dividen por √2.

Pasos:

1. Correr el **control** (`lphi4`), primero con una corrida piloto de N = 128, y
   validarlo contra el espectro de Dufaux et al. (2007) para q = 120.
2. Correr **`lphi4U1`** y **`lphi4SU2U1`** con los valores emparejados. Chequear
   que la ley de Gauss se cumpla a precisión de máquina desde el inicio y que
   el inflatón oscile igual que en el control.
3. Extraer Ω_GW(f) de cada corrida y comparar: posición y altura del pico, y si
   los modelos con gauge dejan rasgos que el control no tiene (un quiebre, un
   segundo pico, otra pendiente a alta frecuencia).

## Resultados (28 de septiembre de 2026, proyecto terminado)

Resumen en [`paginas/final-project.html`](paginas/final-project.html) (conclusiones y cómo se verificó cada resultado) y
en los PDF [`informes/informe-definitivo.pdf`](informes/informe-definitivo.pdf) (5 páginas, el informe pedido) e
[`informes/informe-extendido.pdf`](informes/informe-extendido.pdf); el detalle, en la bitácora.


- **Control `lphi4`:** validado contra Dufaux et al. (2007) (`paginas/piloto-lphi4.html`) y repetido con el
  integrador VV2, el mismo que exigen los modelos con gauge (bitácora §3.2).
- **Resolución:** lo que controla el espectro de ondas es el k máximo de la red, no N. 64 puntos
  con la caja a la mitad (`kIR = 0.5`) dan lo mismo que 128 puntos, 8 veces más rápido. Ninguna de
  las dos resuelve k > 4, así que la comparación se apoya en el pico y el IR (bitácora §3.3).
- **`lphi4U1`:** CosmoLattice arranca el campo de gauge sin modos transversales (A = 0), y eso
  retrasa artificialmente la resonancia. Con un parche que les da fluctuaciones de vacío
  (`code/parches/`), la resonancia gauge va a la par de la del control, y el espectro de ondas en
  la parte confiable sale 0,56–0,79 veces el del control (medio 0,68, tres semillas; bitácora §3.4 y §3.6).
- **`lphi4SU2U1`:** SU(2) arranca igual (links en la identidad). El parche análogo mostró que, con el
  inflatón cargado bajo los dos campos, U(1) y un color de SU(2) se mezclan como el fotón y la Z: hay
  un "fotón" sin masa que no resuena, una "Z" con q = 120 (como el control) y dos "W" con q = 60. El
  vacío se genera en esa base (bitácora §3.5).
- **Resultados de `lphi4SU2U1`** (una semilla, bitácora §3.7): la Z resuena como el campo hijo del
  control (1 % de la energía en τ = 68); las W casi no resuenan al principio pero se disparan después
  (1 % en τ = 117) y terminan con tanta energía como Z + fotón. Los gauge se llevan 64 % de la energía
  (control 48 %, U(1) 40 %). El espectro de ondas en la parte confiable es 1,11 veces el del control en
  promedio y 1,7–1,9 veces cerca del pico (k = 1,5–2); 1,7 veces el de U(1).
- **Cómo se producen las ondas** (bitácora §3.8): en la fase lineal los tres modelos siguen al cuadrado del
  campo. U(1) produce menos ondas casi solo porque recibe menos energía (eficiencia 0,94 del control).
  SU(2)×U(1) produce más y antes (80 % de sus ondas ya en τ = 120), no por las W tardías. Hoy el pico queda
  en h²Ω_GW ~ 10⁻¹⁰ a ~6×10⁷ Hz en los tres.
- **Forma del espectro** (bitácora §3.9): el control tiene una meseta de k = 2 a 4; U(1) la inclina hacia
  las ondas cortas (pendiente 0,55 ± 0,12 contra 0,09 ± 0,12); SU(2)×U(1) tiene un pico en k = 2. La
  pendiente IR (~1) no cambia de forma medible.
- **Problemas encontrados** en el camino (física, medición y herramientas): bitácora §3.10.
- **Falta:** más semillas de SU(2)×U(1); entender por qué SU(2)×U(1) produce las ondas antes y el disparo tardío de las W; un diagnóstico de
  crecimiento por modo para SU(2), porque su espectro guardado es el de |B|.

## Organización del repositorio

| | |
|---|---|
| `index.html` | la portada de GitHub Pages: redirige a la página del proyecto. |
| `paginas/` | **todas las páginas HTML** (se describen una por una abajo). Se abren en el navegador; las figuras las toman de `figures/`. |
| `informes/` | los dos PDF: `informe-definitivo.pdf` (5 páginas, **el informe final pedido**) e `informe-extendido.pdf` (`paginas/final-project.html` completo). Se generan con `code/generar_pdf.py`. |
| `paginas/bitacora.html` | **para empezar si no sos de física**: diario de trabajo en lenguaje llano, con lo hecho, lo aprendido y un glosario. Se actualiza a medida que avanza el trabajo. |
| `paginas/final-project.html` | la página de presentación, para un lector que no estuvo en clase. Se arma a medida que avanza el trabajo, no al final. |
| `paginas/what-is-cosmolattice.html` | introducción a CosmoLattice para quien nunca lo usó: qué es, cómo pone campos escalares y de gauge U(1)/SU(2) en una red, y las ecuaciones que generan las ondas gravitacionales, cada una citada con su número de ecuación. |
| `paginas/bases-teoricas-modelos-gauge.html` | un nivel más abajo: variables de programa, condiciones iniciales y ley de Gauss discreta en los tres modelos, cada paso verificado por `code/verificar_variables_de_programa.py`. |
| `paginas/analisis-parametros.html` | qué parámetros hacen comparables a los tres modelos: los valores que usan los autores y por qué, λ según las observaciones, un análisis de Floquet de q y la tabla recomendada. Los números salen de `code/analisis_parametros.py`. |
| `paginas/piloto-lphi4.html` | la primera simulación: el piloto del control `lphi4` (N = 128, q = 120). Calidad numérica, resonancia contra Floquet, cuándo y dónde se producen las GWs, comparación con Dufaux et al. (2007) y qué implica para las corridas con gauge. Figuras y números de `code/analisis_corridas.py`. |
| `paginas/informe-definitivo.html` | la fuente HTML del informe definitivo: 5 páginas con texto y figuras que explican el trabajo. |
| `AGENTS.md` | por dónde empezar si sos un agente que clona el repo. |
| `requirements.txt` | el entorno de Python (versiones exactas). |
| `code/` | todo lo escrito desde cero: verificaciones, análisis, archivos de configuración de las corridas (`*.in`), post-procesamiento y gráficos. `convergencia_N.py` (resolución), `comparar_modelos.py` (control contra U(1)), `crecimiento_por_modo_U1.py` (crecimiento contra Floquet), `validar_vacio_su2.py` (prueba del parche SU(2)), `semillas_U1.py` (tres semillas), `analisis_SU2U1.py` (SU(2)×U(1)), `produccion_gws.py` (cómo y cuándo se producen las ondas, espectro de hoy), `pendientes_espectro.py` (forma del espectro), `progreso_corrida.py` (avance de una corrida) y `reproducir_analisis.py` (corre todo el análisis de una vez). |
| `code/parches/` | los cambios que le hicimos a CosmoLattice, como parches de `git`, explicados en `code/parches/LEEME.md`. Hoy: la condición inicial con vacío transversal para U(1) y, encima, para SU(2)×U(1) (con la mezcla tipo fotón/Z). |
| `data/` | salidas de las corridas (promedios y espectros en texto, cada carpeta con su `.in` y los logs de tiempo). `data/convergencia_N/` tiene la prueba de resolución, `data/pruebas_costo_N128/` las pruebas de costo, `data/semillas/` las semillas extra, `data/prueba_su2_vacioT/` las pruebas del parche SU(2) y `data/lphi4SU2U1_vacioT_N64_kIR0.5_VV2/` la corrida larga, cada una con su `LEEME.md`. |
| `figures/` | todas las figuras que aparecen en las páginas o en el PDF. |
| `bibliografía/` | los papers de referencia: los de CosmoLattice (código, teoría, GWs) y la literatura sobre campos de gauge en el recalentamiento. `bibliografía/BIBLIOGRAFIA.md` explica qué es cada uno y para qué está. |
| `CosmoLattice/` | el código de CosmoLattice, clonado de upstream. No se commitea (ver "Cómo reproducirlo"): se compila desde la fuente cada vez, con los parches de `code/parches/` aplicados. |
| `provenance/` | `claims.yaml` y `numbers.json`: qué se afirma, cómo se verificó (`verificacion`) y qué lo respalda. El formato está en `.claude/provenance/*.md`. |
| `.claude/`, `.codex/` | el mismo control de procedencia que en `day5/exercise/` del repo del curso: un hook de inicio y fin de sesión que no deja terminar un turno con una figura o un número sin registrar. |

## Cómo reproducirlo

CosmoLattice compila sin problemas acá, en tres de sus modelos. La primera
simulación física es el piloto del control (`code/lphi4_piloto_N128.in`,
salidas en `data/lphi4_piloto_N128/`, análisis en `paginas/piloto-lphi4.html`).

**Atajo:** si solo querés rehacer los análisis y las verificaciones desde los datos del repo (sin simular),
alcanza con `pip install -r requirements.txt` y `python3 code/reproducir_analisis.py` (~2,5 min). Regenera
todas las figuras y los números, y termina con el control de procedencia.

Para volver a simular:

```bash
git clone https://github.com/cosmolattice/cosmolattice.git CosmoLattice
cd CosmoLattice
git checkout acc8278d8832890754a1df16aec9eab5e1867c5c   # el commit con el que se hizo todo
mkdir build_lphi4 && cd build_lphi4
cmake -DMODEL=lphi4 -DOPENMP=ON ..
make cosmolattice -j"$(nproc)"
# repetir con -DMODEL=lphi4U1 y -DMODEL=lphi4SU2U1, cada uno en su propio directorio de build
```

- Commit de upstream: `acc8278d8832890754a1df16aec9eab5e1867c5c` (2026-08-04),
  `https://github.com/cosmolattice/cosmolattice`. Ya incluye el fix
  `f6b9c267` del medidor de la ley de Gauss en SU(2). El `FetchContent` de
  CMake descarga automáticamente al configurar el backend TempLat (fijado en
  `v1.0.2` por el propio `CMakeLists.txt` de CosmoLattice) y Kokkos. Hace falta
  conexión a internet una vez; no se incluyen en el repo.
- Herramientas usadas: `g++` 13.3.0 (Ubuntu 24.04), CMake 4.0.3, GNU Make 4.3,
  compilado con `-DOPENMP=ON` (Kokkos detectó OpenMP como backend de CPU; sin
  GPU ni MPI).
- Los tres builds (`lphi4`, `lphi4U1`, `lphi4SU2U1`) compilaron a un binario
  funcional con una misma advertencia inofensiva (`-Wshadow` sobre `FloatType`
  en `abstractmodel.h`, presente en los tres): un choque de nombres dentro de
  la jerarquía de templates de CosmoLattice, no algo introducido acá.
- Prueba de humo de `lphi4`: `./lphi4 input=../../models/parameter-files/lphi4.in N=16 tMax=0.5`
  terminó bien (código de salida 0) y escribió los archivos esperados
  (`average_*.txt`, `spectra_*.txt`). Es un chequeo del build, no un
  resultado físico: `N=16` y `tMax=0.5` son demasiado chicos para significar
  algo, y no se guardó nada de esa corrida.
- Entorno de Python: `pip install -r requirements.txt` (Python 3.12.9; numpy, scipy, matplotlib,
  sympy, pyyaml y marimo, con las versiones exactas usadas).
- Las verificaciones y el análisis se reproducen con
  `python3 code/verificar_variables_de_programa.py` y
  `python3 code/analisis_parametros.py [--tabla | --figura]`, o todo junto con
  `python3 code/reproducir_analisis.py`.
- El piloto se corre desde `data/lphi4_piloto_N128/` con
  `../../CosmoLattice/build_lphi4/lphi4 input=lphi4_piloto_N128.in` (≈ 1 h 20 min
  con 8 núcleos, 320 MB) y se analiza con `marimo edit code/analisis_corridas.py`
  (necesita además `marimo`), que también regenera `figures/lphi4_piloto_N128/`.
- Las corridas de resolución se corren con `data/convergencia_N/correr.sh` (en serie, ~1 h en
  total) y se comparan con `python3 code/convergencia_N.py`.
- Para el U(1) con vacío transversal hay que aplicar el parche y compilar en un build aparte:

  ```bash
  cd CosmoLattice && git apply ../code/parches/u1_vacio_transversal.patch
  mkdir build_lphi4U1_tv && cd build_lphi4U1_tv
  cmake -DMODEL=lphi4U1 -DOPENMP=ON .. && make -j"$(nproc)"
  ```

  El `.in` es `code/lphi4U1_vacioT_N64_kIR0.5_VV2.in` (la única diferencia con
  `code/lphi4U1_N64_kIR0.5_VV2.in` es `ICtype_U1 = RandomWithMatterTransverseVacuum`). Cada corrida
  de U(1) con N = 64 tarda ~1 h 15 min con 8 núcleos. Se comparan con
  `python3 code/comparar_modelos.py` y `python3 code/crecimiento_por_modo_U1.py <carpeta>`.
- Para SU(2)×U(1) con vacío transversal se aplican los dos parches, en orden, y se compila aparte:

  ```bash
  cd CosmoLattice && git apply ../code/parches/u1_vacio_transversal.patch
  git apply ../code/parches/su2_vacio_transversal.patch
  mkdir build_lphi4SU2U1_tv && cd build_lphi4SU2U1_tv
  cmake -DMODEL=lphi4SU2U1 -DOPENMP=ON .. && make -j"$(nproc)" lphi4SU2U1
  ```

  El `.in` es `code/lphi4SU2U1_vacioT_N64_kIR0.5_VV2.in` (~11 h con 8 núcleos). Las pruebas del
  parche están en `data/prueba_su2_vacioT/` y se verifican con `python3 code/validar_vacio_su2.py`.
- Análisis: `python3 code/semillas_U1.py` (tres semillas de control y U(1), `data/semillas/`),
  `python3 code/analisis_SU2U1.py` (SU(2)×U(1) contra control y U(1)) y
  `python3 code/crecimiento_por_modo_U1.py lphi4SU2U1_vacioT_N64_kIR0.5_VV2`; cómo y cuándo se producen las
  ondas, eficiencia y espectro de hoy: `python3 code/produccion_gws.py`. El avance de una corrida
  en curso se ve con `python3 code/progreso_corrida.py data/<carpeta>`.
- El código de CosmoLattice y los directorios de build se clonan de cero y no
  se commitean (`.gitignore` excluye `CosmoLattice/`): es una dependencia
  externa, fijada por el hash de commit de arriba, no algo que escribió este
  proyecto.

Los parámetros de cada corrida, su tiempo de cómputo y cómo se verificaron las salidas (ley de
Gauss, conservación de la energía) están en la bitácora y en `provenance/`.
