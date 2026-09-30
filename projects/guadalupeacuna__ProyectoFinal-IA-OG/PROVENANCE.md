# Proveniencia

Para cada artefacto: **quién** lo produjo, **a partir de qué** entrada, **cuándo** (fecha de modificación del
archivo, 2026 salvo indicación) y **cómo se chequeó**. "Usuario" soy yo. "Claude" es Claude Code. "Codex" es
OpenAI Codex. Las rutas son relativas a la raíz del repositorio.

Convención de estado: **V** = verificado por un camino independiente · **P** = parcial · **N** = no verificado ·
**X** = sabido incorrecto (se conserva como registro).

## 1. Entradas

| Archivo | Autor | Qué es |
|---|---|---|
| `consignas/final-project.html`, `consignas/consigna_email.txt` | Curso | Consigna del proyecto final |
| `material/Notas/Notes_Bigravity_MIO.pdf` | Usuario | Mis notas: chameleon bigravity (resumen de 1702.04490), estabilidad estándar (resumen de 2108.06722), ecuaciones lineales tensoriales, autoestados de masa, *Next steps*. Punto de partida de todo. |
| `material/Modelo-de-codigo_Standar_Bigravity.nb` (15-09) | Usuario | Mi código modelo en xPand: c = 1, ξ constante, sin escalar. Llega a las ecuaciones tensoriales lineales. |
| `material/Standard_Bigravity-TercerOrden_MODELO.nb` (2025-10-28) | Usuario | Versión anterior del modelo (4 celdas distintas; no tiene contenido de tercer orden). |
| `material/claude/consignaclaude.txt`, `material/codex/consignacodex.txt` (19-09) | Usuario | **Mismo prompt** a los dos agentes (A/B): equivalencia orden a orden de G[g] y G[f] y reglas `IndexSet` para f. |
| `material/codex/consigna0_21-09-26_codex.txt` (21-09) | Usuario | Segundo prompt a Codex: componente 00, fondo de f, revisar la ecuación del escalar. |
| `material/Notas/RepasoReunion_Chameleon_Bigravity/Notas_Reunion.txt` (24-09) | Usuario | Mis notas de una reunión con colegas (dictadas). **Anonimizadas** el 28-09: los nombres de los colegas se reemplazaron por "colega", también en el nombre del archivo. |
| `consignas/consigna_Claude.txt` (28-09) | Usuario | Prompt con que se armó esta entrega. |

## 2. Notas analíticas (etapa a)

| Archivo | Autor | Entrada | Chequeo | Estado |
|---|---|---|---|---|
| `material/Notas/notes_spin2_anterior.tex` (08-09) | Claude | Mis notas + *Next steps* | `checks.py`, `checks2.py` | ver abajo |
| `material/archivos_previos/informe_chameleon_spin2.{txt,html}` (09-09 15:11) | Codex | Notas de Claude, líneas 697–1669 | — | 1ra auditoría: 11 problemas + 50 supuestos |
| `material/archivos_previos/segunda_auditoria_chameleon_spin2.txt` (16:03) | Codex | Notas corregidas | — | 16 problemas |
| `material/archivos_previos/tercera_auditoria_chameleon_spin2.txt` (16:22) | Codex | Notas corregidas | — | 20 problemas |
| `material/archivos_previos/cuarta_auditoria_chameleon_spin2.txt` (16:45) | Codex | Notas corregidas | — | 17 problemas |
| `material/Notas/notes_spin2_auditado.tex` (09-09 17:23) | Claude (corrigiendo tras cada auditoría) | Notas + 4 auditorías | ver secciones | Fondo (Sec. 7): **V**. Estabilidad (Sec. 8): **P**. Tensores con ángulo θ(t) (Sec. 9): **N**. Oscilaciones y materia oscura (Secs. 10–11): **N** |
| `material/Notas/guia_derivaciones.tex` (01-09) | Claude | Notas | — | **N**. Contiene referencias erróneas: autores de 1711.04655 equivocados y "2107.xxxxx" en lugar de 2108.06722 |
| `material/outputs_claude/checks.py` (31-08) | Claude | Notas Secs. 7–11 | 21/21 PASS (`verificaciones/checks.log`) | Las ecuaciones de fondo están *tipeadas* de las notas, no derivadas: chequea consistencia interna |
| `material/outputs_claude/checks2.py` (01-09) | Claude | Notas + acción | 34/34 PASS | El bloque A compara Euler–Lagrange **numéricamente** en una sola curva (3 instantes). El bloque F es numérico, con tolerancia del 25 % |
| `material/Notas/RepasoReunion_Chameleon_Bigravity/Repaso_Chameleon_Bigravity.{tex,pdf}` (24-09) | Claude | Mis notas de la reunión + 1702.04490 + 1711.04655 | Contrastado con los papers por el agente; no lo chequeé línea por línea | **P**. Usa las Figs. 1–5 originales de 1711.04655 (`figs/`), citadas en cada leyenda (`\creditoII`) y en `figs/CREDITOS.md`. **Anonimizado** el 28-09 y recompilado |

## 3. Código (etapa b)

| Archivo | Autor | Entrada | Chequeo | Estado |
|---|---|---|---|---|
| `material/archivos_previos/cambios_codigo_bigravity_cneq1.txt` (17-09) | Codex | Mi código modelo | — | Plan de 10 puntos para c ≠ 1, ξ(t): diferencia de conexiones, f⁻¹ como inversa verdadera, `Rulesdf` con factores de c |
| `material/archivos_previos/Gf_general_patch.wl` (17-09) | Codex | ídem | — | Parche con `ruleCf`, `ruleRicfConn`, `ruleGfConn` |
| `material/claude/claude_Perturbaciones_Chameleon.nb` (18-09), `material/archivos_previos/claude_Reporte_cambios_cneq1.html` | Claude | Mi notebook + los 10 puntos | 9 chequeos simbólicos = 0 desde un kernel limpio (según el reporte) | **V** para la geometría de fondo de f |
| `material/archivos_previos/codex_Perturbaciones_Chameleon_Xgeneral.nb` (17-09) | Codex | ídem | — | registro |
| `material/claude/v1CLAUDE_Perturbaciones_Chameleon.nb` (21-09) | Claude | Prompt A/B | Bloque C1–C13: `inverf·f`, R[f] contra FLRW exacto, límite ξ, c → 1 | **P**. Mantiene la regla `PertX` con factor 1/2, que Codex mostró incorrecta para c ≠ 1 |
| `material/codex/v1CODEX_Perturbaciones_Chameleon.nb` (19–22-09), `v2CODEX_…nb` (21-09) | Codex | Prompt A/B + 2do prompt | `v1_validacion.log`: ALL_CHECKS_PASS. `revision_entrega.log`: 171 chequeos | **P**. v2 abandona xAct (componentes explícitas), contra mi estilo |
| `material/Perturbaciones_Chameleon.nb` (25-09) | **Usuario**, con estructuras de f diseñadas con Claude | Mi modelo + reglas de los agentes | Fondo g: grilla nula. Fondo f, KG, vínculo, ecuación para ξ: `verificaciones/check_constraint_fondo.py` | **V** hasta el fondo. **P** a orden lineal (`EqTg` sale; `EqTf` da `$Aborted`; `rδf` todavía supone f = ξ²g). **Corregido en `codigo/`** (sección 4) |
| `material/outputs_codex/constraint_*` (23–24-09) | Codex | Mi notebook | `constraint_auditoria_actual.txt`: con los signos actuales queda residuo de materia; con `rhodot` y `phidd` corregidos, 0 | Encontró el **bug de signo** |
| `material/outputs_claude/constraint_background_CORRECCION.wl` (24-09 12:34) | Claude | Mi notebook | Llega al mismo vínculo que 1702.04490 | Encontró el **mismo bug**, de forma independiente |
| `material/Perturbaciones_Chameleon_corregido.nb` (24-09 12:45) | Codex (parche automático) | Mi notebook | `outputs_codex/constraint_copia_corregida_checks.wl`: `{True, False, False, True, True}` | **X**. El script terminó con `Exit[1]` pero escribió igual el notebook |
| `material/outputs_claude/chameleon_bigravity_estabilidad.nb` (09-09) | Claude | Notas + 1711.04655 | Sin salidas guardadas | **P/X**: los In 41 e In 45 cargan a mano κ₁, Σ, Σ₁, Σ₂ del paper (**copia, no derivación**) |
| `material/outputs_claude/Camaleon_cscalar_xchico.nb` (15-09) | Claude | Σ del paper | Numérico | **N** |
| `material/outputs_claude/chameleon_bigravity_lagrangiano_orden3*.nb` (15-09) | Claude | Mi modelo | Chequeo covariante del sector g | registro |
| `material/outputs_codex/Chameleon_1711_analitico.{nb,wl}`, `Chameleon_motor_analitico.wl`, `Chameleon_1711_LEEME.md`, `Resumen_Chameleon_1711.html` (14–15-09) | Codex | Acción de 1711.04655 | `finalizar_resultado_escalar.log`, `comprobar_identidades_final.log`: identidades exactas. Las fórmulas del paper **no** se usan como entrada, sólo como blanco de comparación | **P**. Pendientes: `verificar_final.log` (UNRESOLVED en masas vector/tensor) y `verificar_xpand_legible.log` (KG) |
| `material/outputs_codex/igualdad_asintotas.png`, `igualdad_analitica_resumen.{png,svg}` | Codex | — | El propio Codex la llama "unión esquemática, no es una integración" | Figura decorativa |

El resto de `material/outputs_codex/` (~200 archivos `.wls`/`.log`/`.wl`) son pasos intermedios de Codex. Incluye
respaldos de notebooks (`respaldo_*`, `v3_respaldo_*`), volcados de celdas (`*.inputs.txt`, `modelo_lectura.txt`)
y checkpoints grandes (`resultado_escalar.wl`, 35 MB). Se conservan sin tocar como registro completo; la mayoría
de los logs están en UTF-16.

## 4. Esta entrega (28-09)

Pedidos: `consignas/consigna_Claude.txt` (primera versión) y `consignas/consigna_Claude_2.txt` (completar,
aplicar todas las sugerencias y correr todo).

| Archivo | Autor | Entrada | Chequeo |
|---|---|---|---|
| `verificaciones/derivacion_TT_general.m` | Claude | **Sólo la acción**, en componentes y sin xAct. Generaliza `derivacion_independiente_TT.m` a c(t), ξ(t), β(φ) | 17/17 PASS: fondo de g y f contra el notebook; c(t) contra las notas; masas contra `EqTg` y contra `m_M²` de las notas |
| `verificaciones/check_mezcla_tensorial.py` | Claude | Las ecuaciones tensoriales de `derivacion_TT_general.m`, a fondo congelado | 6/6 PASS: ángulo θ_k en forma cerrada; θ₀ y ramas de resonancia de las notas |
| `informe/figs/mezcla_tensorial.pdf` | Claude (`make_figs.py`) | La fórmula cerrada de θ_k (chequeo [3] de arriba) | No es una integración numérica: evalúa la fórmula |
| `verificaciones/check_constraint_fondo.py` | Claude | **Sólo** las ecuaciones de fondo impresas en `Perturbaciones_Chameleon.nb` (listadas en el docstring) | 7/7 PASS, con un control negativo: con el signo de ρ̇ invertido, falla |
| `verificaciones/derivacion_independiente_TT.m` (copiado de `archivos_previos/`, 11-09) | Codex, sin xAct | Sólo la acción (c = 1, ξ constante) | Re-corrido hoy: `derivacion_independiente_TT.log` |
| `verificaciones/checks.py`, `checks2.py` | Claude (31-08 / 01-09) | Notas | Re-corridos hoy: logs |
| `verificaciones/run_all.sh` | Claude | — | Corre todo lo anterior |
| `codigo/Perturbaciones_Chameleon.nb` | **Usuario**, con 5 arreglos de Claude marcados en celdas `[Claude, 28-09-2026]` | `material/Perturbaciones_Chameleon.nb` (25-09) | Evaluado entero desde un kernel limpio en 812 s (`codigo/evaluar_notebook.wls`, log en `codigo/corrida_Perturbaciones_Chameleon.log`), sin celdas de mensaje. Controles internos: residuo de c(t) = 0; tensores contra `EqTg` = 0 |
| `codigo/herramientas/editar_nb_fe.wls`, `tt_en_notebook.wl` | Claude | El notebook original | Aplican los arreglos dentro del front end, de modo reproducible |
| `codigo/Modelo-de-codigo_Standar_Bigravity.nb` | Usuario (+ `codigo/herramientas/editar_modelo_fe.wls`, Claude) | `material/Modelo-de-codigo_Standar_Bigravity.nb` | Las 2 celdas de fórmulas quedan no evaluables; re-evaluado desde un kernel limpio en 267 s, sin celdas de mensaje |
| `informe/`, `index.html`, `index_es.html`, `README.md`, `PROVENANCE.md`, `AGENTS.md` | Claude, a pedido mío, a partir de todo lo anterior | Todo `material/`, más los resúmenes de 2 subagentes que leyeron los notebooks sin evaluarlos | Los resultados que se citan salen de los logs de `verificaciones/` y de la corrida limpia |
| `informe/figs/make_figs.py` | Claude | Fechas de archivos; problemas de las auditorías, clasificados a mano por Claude y revisados contra el texto de cada auditoría (la lista está en el script) | La clasificación queda a la vista |

### Los arreglos al notebook (todos marcados dentro del notebook)

1. **`BackgroundG`** se usaba en el capítulo de primer orden pero no estaba definida en ninguna celda; la corrida limpia
   del original lo muestra con `ReplaceAll::reps: {BackgroundG}`. Ahora vale `Join[H2, Hdot, Hf2, Hfdot]`.
2. **c(t) explícito.** Nuevas celdas `EcuacionC` y `cMenos1` (`Solve`), y comparación con la forma de las notas:
   el residuo da 0.
3. **`Rulesdf`** usaba `XI^2 SVT`, que sólo vale para c = 1. Ahora usa `SVTf`, que agrega CF² en δf₀₀ y CF en δf₀ᵢ;
   el sector tensorial no cambia.
4. **`EqTf`** no terminaba (`$Aborted`), y `rδf` supone f = ξ²g. Esas dos celdas quedan con `Evaluatable -> False`,
   y el sector tensorial de f para c y ξ generales se deriva en componentes dentro del mismo notebook, usando
   las reglas de fondo del notebook, y se compara con `EqTg`.
5. Se borraron las salidas guardadas, incluida una vieja de otra sesión, y el notebook se re-evaluó de punta a
   punta. Pendiente, documentado: la regla de `PertX` es exacta sólo en el sector tensorial.

### Decisiones con alternativas defendibles

- **g es la única métrica de xTensor.** f se representa como tensor, con `inverf` como inversa verdadera y la geometría
  por diferencia de conexiones. La alternativa (dos métricas en xTensor) complica las perturbaciones de f con xPand.
- **Convención de signo de β_n.** Mi código usa `+ M_g² m² Σ β_n e_n`; las notas de Claude, `− m² M² Σ β_n e_n`.
  Los vínculos son lineales en β, así que coinciden (chequeo [2]). La ecuación para ξ difiere en signo y
  normalización, como corresponde al diccionario.
- **Qué cuenta como independiente.** Un chequeo es independiente si no comparte código con la derivación.
  `checks.py` **no** es independiente de las notas para las ecuaciones de fondo, porque las tipea.
