# Bibliografía

Todos los PDF de esta carpeta se bajaron de arXiv el 22 de septiembre de 2026. Salen de
[cosmolattice.net](https://cosmolattice.net) (su documentación, la página del manual sobre ondas
gravitacionales, la de campos de gauge y la de cómo citar) y de una búsqueda de trabajos previos
específicamente sobre campos de gauge y ondas gravitacionales en el recalentamiento. Están
agrupados según para qué sirve cada paper en este proyecto, no por fecha.

## CosmoLattice: el código, su motor y cómo citarlo

| archivo | referencia | para qué está |
|---|---|---|
| `figueroa2021_cosmolattice_code_2102.01031.pdf` | Figueroa, Florio, Torrentí, Valkenburg, *CosmoLattice — User Manual*, arXiv:2102.01031 | El paper del código v1.0 y manual de usuario: instalación, archivos de entrada, cómo definir un modelo. La referencia base de todo lo que hace el build en `../CosmoLattice/`. También describe las condiciones iniciales de los campos de gauge (ecs. 97–102), que motivaron el parche de `code/parches/`. |
| `baezaballesteros2026_cosmolattice2.0_2607.24978.pdf` | Baeza-Ballesteros, Figueroa, Florio, Loayza, Sattler, Torrentí, Urio, *CosmoLattice 2.0*, arXiv:2607.24978 | La versión que está clonada y compilada acá. La v2.0 reorganizó el repositorio (`models/` en la raíz, C++20, motor TempLat) y este es su propio paper del código. |
| `florio2026_templat_2607.24908.pdf` | Florio y Sattler, *TempLat: a versatile C++ engine for lattice field theories*, arXiv:2607.24908 | TempLat es el motor sobre el que corre CosmoLattice 2.0 (CMake lo baja solo con `FetchContent`). Hace falta para leer el código, no solo para correrlo. |
| `figueroa2021_art1_theory_lattice_2006.15122.pdf` | Figueroa, Florio, Torrentí, Valkenburg, *The Art of Simulating the Early Universe — Part I: Integration Techniques and Canonical Cases*, arXiv:2006.15122 | La teoría detrás del código: cómo se ponen en la red los campos escalares **y de gauge**, los integradores y los modelos canónicos de ejemplo (de acá salen las ecuaciones en la red de `lphi4U1` y `lphi4SU2U1`). |
| `baezaballesteros2026_art2_noncanonical_gw_2512.15627.pdf` | Baeza-Ballesteros, Figueroa, Florio, Lizarraga, Loayza, Marschall, Opferkuch, Stefanek, Torrentí, Urio, *The Art of Simulating the Early Universe — Part II: Non-canonical Cases & Gravitational Waves*, JCAP 06:087 (2026), arXiv:2512.15627 | **El paper del método de ondas gravitacionales.** Documenta el algoritmo actual (5 grados de libertad) que usa CosmoLattice 2.0 para evolucionar el tensor transversal y sin traza de las ondas y extraer Ω_GW(f), incluidas las contribuciones de los campos de gauge al estrés anisotrópico. Es lo que hay que citar como método para cualquier número de ondas gravitacionales de este proyecto. |

## Campos de gauge y ondas gravitacionales en el recalentamiento: la literatura en la que se ubica este proyecto

| archivo | referencia | para qué está |
|---|---|---|
| `garciabellido2007_stochastic_gw_hybrid_preheating_astroph0701014.pdf` | García-Bellido y Figueroa, *A stochastic background of gravitational waves from hybrid preheating*, arXiv:astro-ph/0701014 | El primero de los papers de este grupo que propone el recalentamiento de la inflación híbrida (con un campo "cascada" con carga de gauge) como fuente de ondas gravitacionales. De ahí desciende la comparación control/gauge de este proyecto. |
| `garciabellido2008_gw_background_hybrid_inflation_0707.0839.pdf` | García-Bellido, Figueroa y Sastre, *A Gravitational Wave Background from Reheating after Hybrid Inflation*, Phys. Rev. D 77, 043517 (2008), arXiv:0707.0839 | La continuación, con el cuadro completo en tres etapas (recalentamiento taquiónico → choque de burbujas → turbulencia) y el espectro de ondas resultante, para un campo cascada con carga U(1). |
| `dufaux2007_theory_numerics_gw_preheating_0707.0875.pdf` | Dufaux, Bergman, Felder, Kofman y Uzan, *Theory and Numerics of Gravitational Waves from Preheating after Inflation*, arXiv:0707.0875 | La otra referencia principal de teoría y simulación para calcular Ω_GW(f) a partir de inhomogeneidades clásicas en el recalentamiento. Una derivación independiente para contrastar el método de CosmoLattice. Contra este paper se validó el piloto del control (`piloto-lphi4.html`). |
| `gwabelian_cosmicstrings_preheating_1006.0217.pdf` | Dufaux, Figueroa y García-Bellido, *Gravitational Waves from Abelian Gauge Fields and Cosmic Strings at Preheating*, Phys. Rev. D 82, 083518 (2010), arXiv:1006.0217 | Justo sobre el tema: separa lo que un campo de gauge U(1) (frente a solo escalares) le agrega al espectro de ondas del recalentamiento, incluidas las cuerdas cósmicas. El antecedente más cercano a la comparación `lphi4` contra `lphi4U1` de este proyecto. |
| `tranberg2017_gw_nonabelian_tachyonic_1706.02365.pdf` | Tranberg, Tähtinen y Weir, *Gravitational waves from non-Abelian gauge fields at a tachyonic transition*, JCAP 04:012 (2018), arXiv:1706.02365 | Espectro de ondas del recalentamiento taquiónico SU(2)-Higgs (parecido al electrodébil). Encuentra dos picos, ligados a las masas del Higgs y del campo de gauge. Relevante para la parte `lphi4SU2U1` del proyecto. |
| `adshead2018_gw_gauge_preheating_1805.04550.pdf` | Adshead, Giblin y Weiner, *Gravitational waves from gauge preheating*, Phys. Rev. D 98, 043525 (2018), arXiv:1805.04550 | Referencia moderna sobre acoples del inflatón con campos de gauge (dilatónicos y axiales/Chern-Simons) que producen ondas gravitacionales de forma eficiente. Es el caso de comparación para un sector gauge acoplado a través del inflatón y no del campo cascada o del Higgs. |
| `gw_higgs_preheating_z2symmetry_2605.04670.pdf` | Zhou, Yu, Cheng y Zhang, *Gravitational Waves from Higgs Preheating after Inflaton Z2-Symmetry Breaking*, arXiv:2605.04670 (2026) | Un estudio reciente hecho con CosmoLattice (acoples trilineal y cuártico entre inflatón y Higgs). Muestra cómo se extrae hoy un espectro de ondas con este mismo código: un modelo de cómo presentar y verificar los resultados de este proyecto. |

## Lo que a propósito no está

No se incluyen libros generales de cosmología o inflación ni revisiones amplias sobre fondos de
ondas gravitacionales. Esta carpeta se limita a CosmoLattice y a los campos de gauge en el
recalentamiento; no es una bibliografía general de ondas gravitacionales.
