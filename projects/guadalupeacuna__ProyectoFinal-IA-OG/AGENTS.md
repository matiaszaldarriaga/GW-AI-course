# Instrucciones para un agente que clona este repositorio

Estás frente al proyecto final "Bigravedad camaleónica y materia oscura de espín 2" de Guadalupe Ahumada Acuña.
No hace falta hablar con la autora para reproducirlo. Empezá leyendo `README.md` y `PROVENANCE.md`.

## Tarea 1: reproducir las verificaciones (obligatoria)

1. Chequeá el entorno: `python -c "import sympy, numpy, scipy, mpmath"` (se probó con sympy 1.12) y, si está,
   `wolframscript -code '$Version'` (se probó con 12.1.1). Los `.m` **no** necesitan xAct.
2. Corré `cd verificaciones && bash run_all.sh` (~3 min). En Windows sin bash, corré a mano cada línea de `run_all.sh`.
3. Compará con los `.log` que están versionados en `verificaciones/`. Para dar el chequeo por bueno:
   - `check_constraint_fondo.log` termina en `7/7 PASS` y el script sale con código 0;
   - `check_mezcla_tensorial.log` termina en `6/6 PASS`;
   - `derivacion_TT_general.log` termina en `17/17 PASS` y el script sale con código 0;
   - `checks.log` dice `21 PASS, 0 FAIL` y `checks2.log` dice `34 PASS, 0 FAIL`. Estos dos scripts salen siempre
     con código 0, así que hay que mirar el resumen;
   - `derivacion_independiente_TT.log` contiene `cierra en (u-v)?  g: True   f: True` y las dos razones de masa `= 1`.
4. Si algo no coincide, no "arregles" el chequeo para que pase: reportá el residuo.

## Qué afirma cada chequeo (para no sobreinterpretarlos)

| Script | Entrada | Qué demuestra | Qué NO demuestra |
|---|---|---|---|
| `derivacion_TT_general.m` (Claude) | sólo la acción, en componentes | fondo de g y de f, c(t) y sector tensorial con c(t), ξ(t) generales; compara con el notebook y con las notas | vectores ni escalares |
| `check_mezcla_tensorial.py` (Claude) | las masas y los gradientes que salen de `derivacion_TT_general.m` | simetrización, m_M², ángulo θ_k en forma cerrada, θ₀ de las notas, condición de resonancia | nada con el fondo variando (usa coeficientes congelados) |
| `check_constraint_fondo.py` (Claude) | las ecuaciones de fondo impresas en el notebook | d/dt(Friedmann) ⇒ vínculo de Bianchi; que las tres formas (notebook, notas, 1702.04490) sean idénticas; control negativo | que esas ecuaciones salgan de la acción (eso lo hace `derivacion_TT_general.m`) |
| `derivacion_independiente_TT.m` (Codex) | la acción | caso c = 1, ξ constante | el caso general |
| `checks.py`, `checks2.py` (Claude) | las notas de Claude | consistencia interna de las Secs. 7–11 | en `checks.py`, el fondo está tipeado y no derivado; el bloque A de `checks2.py` es numérico, sobre una sola curva |

## Tarea 2 (opcional): el notebook de la autora

`codigo/Perturbaciones_Chameleon.nb` está guardado con las salidas de una corrida limpia. Para rehacerla hace falta
Mathematica ≥ 12.1 con xAct (xTensor 1.2.0, xPert 1.0.6, xPand 0.4.3) en `$UserBaseDirectory/Applications`:
`wolframscript -file codigo/evaluar_notebook.wls codigo/Perturbaciones_Chameleon.nb salida.nb`.
Ese script abre el notebook en un front end oculto, lo evalúa entero y lo guarda.
Controles dentro del notebook, en las celdas marcadas `[Claude, 28-09-2026]`:
- el último `Simplify` del bloque de c(t) tiene que dar `0`;
- en el bloque "Sector tensorial de f", las salidas tienen que ser, en orden: `0`, la lista de masas, `{0, 0, True}`, `0` y la masa `ttmM2`.

No evalúes `material/Perturbaciones_Chameleon_corregido.nb` como si fuera correcto: es un parche que falló sus
propios chequeos (ver `PROVENANCE.md`).

## Tarea 3 (opcional): regenerar el informe

`cd informe/figs && python make_figs.py && cd .. && pdflatex informe_proyecto_final.tex` (corré pdflatex dos veces).

## Reglas

- No modifiques nada dentro de `material/`: es el registro histórico.
- Todo archivo nuevo lleva su entrada en `PROVENANCE.md` (autor, entrada, chequeo).
- Distinguí siempre "derivado", "copiado de un paper" y "chequeado numéricamente".
