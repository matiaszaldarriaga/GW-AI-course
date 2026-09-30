import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Análisis de una corrida de CosmoLattice

    Este notebook lee las salidas de una simulación (una carpeta dentro de `Final/data/`) y las
    analiza en cinco partes:

    1. **Fondo (background):** cómo se expande el universo y cómo se reparte la energía.
    2. **Campos:** cómo oscila el inflatón φ y cómo crece el campo hijo χ por resonancia.
    3. **Espectros de potencia:** en qué escalas (números de onda k) crece cada campo, comparado
       con la teoría de Floquet.
    4. **Ondas gravitacionales (GWs):** el espectro en la simulación y trasladado a hoy.
    5. **¿Cuándo crecen las GWs?** El momento en que los gradientes de los campos se vuelven
       importantes, que es cuando se produce la mayor parte de las GWs.

    **Unidades.** Todo está en *unidades de programa* de CosmoLattice (modelo `lphi4`, α = 1):
    los campos se miden en unidades de f★ (el φ inicial), el tiempo τ es el tiempo conforme
    multiplicado por ω★ = √λ f★, y los números de onda k son comóviles, en unidades de ω★.
    Como α = 1, la cantidad que obedece la ecuación de Lamé (la teoría de la resonancia) es el
    campo *conforme* a·χ, y por eso casi todo se grafica multiplicado por a.

    Para abrirlo, desde `Final/`: `marimo edit code/analisis_corridas.py`.
    """)
    return


@app.cell
def _():
    import os
    import sys
    from pathlib import Path

    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import LinearSegmentedColormap, LogNorm, Normalize
    from scipy.special import ellipj, ellipk

    return (
        LinearSegmentedColormap,
        LogNorm,
        Normalize,
        Path,
        ellipj,
        ellipk,
        mo,
        np,
        os,
        plt,
        sys,
    )


@app.cell
def _(LinearSegmentedColormap, plt):
    # Paleta: categórica en orden fijo (azul, naranja, aqua, amarillo) y una rampa
    # secuencial de un solo tono (claro -> oscuro) para "tiempo" o "magnitud".
    C_AZUL, C_NARANJA, C_AQUA, C_AMARILLO = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
    C_TINTA, C_TINTA2 = "#0b0b0b", "#52514e"
    RAMPA = LinearSegmentedColormap.from_list("rampa_azul", ["#d6e4f5", "#2a78d6", "#0b2a55"])
    plt.rcParams.update({
        "figure.dpi": 110, "axes.grid": True, "grid.color": "#e4e3df", "grid.linewidth": 0.6,
        "axes.edgecolor": "#b9b8b2", "axes.labelcolor": C_TINTA, "xtick.color": C_TINTA2,
        "ytick.color": C_TINTA2, "lines.linewidth": 1.6, "axes.spines.top": False,
        "axes.spines.right": False, "legend.frameon": False, "font.size": 10,
        "axes.titlesize": 10, "axes.titlelocation": "left",
    })
    return C_AMARILLO, C_AQUA, C_AZUL, C_NARANJA, C_TINTA2, RAMPA


@app.cell
def _(DIR_FINAL, selector_corrida):
    def guardar(fig, nombre):
        """Guarda la figura en Final/figures/<corrida>/<nombre>.png (la usa el informe de la corrida)."""
        destino = DIR_FINAL / "figures" / selector_corrida.value
        destino.mkdir(parents=True, exist_ok=True)
        fig.savefig(destino / f"{nombre}.png", dpi=130, bbox_inches="tight")

    return (guardar,)


@app.cell(hide_code=True)
def _(Path, mo, os):
    DIR_FINAL = Path(mo.notebook_dir()).parent
    DIR_DATA = DIR_FINAL / "data"
    _corridas = sorted(p.name for p in DIR_DATA.iterdir()
                       if (p / "average_energies.txt").exists()) if DIR_DATA.exists() else []
    # Corrida por defecto: la variable de entorno CORRIDA si existe (útil para ejecutar sin interfaz,
    # p. ej. `CORRIDA=lphi4_control_N128_VV2 python code/analisis_corridas.py`), si no el piloto.
    _defecto = os.environ.get("CORRIDA", "lphi4_piloto_N128")
    selector_corrida = mo.ui.dropdown(
        options=_corridas,
        value=_defecto if _defecto in _corridas else (_corridas[0] if _corridas else None),
        label="Corrida a analizar",
    )
    selector_corrida
    return DIR_DATA, DIR_FINAL, selector_corrida


@app.cell
def _(np):
    def leer_promedios(ruta):
        """Lee un average_*.txt y devuelve un dict {nombre_de_columna: array}."""
        with open(ruta) as fh:
            cabecera = fh.readline().lstrip("#").split()
        datos = np.loadtxt(ruta, ndmin=2)
        return {nombre: datos[:, i] for i, nombre in enumerate(cabecera)}

    def leer_espectros(ruta):
        """Lee un spectra_*.txt: un bloque por tiempo, separados por líneas en blanco.
        Devuelve un array (n_tiempos, n_bins, n_columnas)."""
        bloques, actual = [], []
        with open(ruta) as fh:
            for linea in fh:
                linea = linea.strip()
                if not linea:
                    if actual:
                        bloques.append(actual)
                        actual = []
                    continue
                if ":" in linea or linea.startswith("#"):
                    continue  # cabecera del bloque
                actual.append([float(x) for x in linea.split()])
        if actual:
            bloques.append(actual)
        return np.array(bloques)

    def leer_parametros(ruta_in):
        """Parsea un .in de CosmoLattice (clave = valor; lo que sigue a # es comentario)."""
        pars = {}
        for linea in open(ruta_in):
            linea = linea.split("#")[0].strip()
            if "=" in linea:
                clave, valor = (s.strip() for s in linea.split("=", 1))
                pars[clave] = valor
        return pars

    def primer_cruce(t, y, umbral):
        """Primer tiempo en que y supera el umbral (interpolado); nan si nunca lo hace."""
        i = np.flatnonzero(y >= umbral)
        if len(i) == 0:
            return np.nan
        i = i[0]
        if i == 0:
            return t[0]
        return np.interp(np.log(umbral), np.log([y[i - 1], y[i]]), [t[i - 1], t[i]])

    return leer_espectros, leer_parametros, leer_promedios, primer_cruce


@app.cell
def _(
    DIR_DATA,
    leer_espectros,
    leer_parametros,
    leer_promedios,
    np,
    selector_corrida,
):
    D = DIR_DATA / selector_corrida.value
    _ins = sorted(D.glob("*.in"))
    PARS = leer_parametros(_ins[0]) if _ins else {}

    fondo = leer_promedios(D / "average_scale_factor.txt")
    energias = leer_promedios(D / "average_energies.txt")
    friedmann = leer_promedios(D / "average_energy_conservation.txt")
    phi_prom = leer_promedios(D / "average_scalar_0.txt")
    chi_prom = leer_promedios(D / "average_scalar_1.txt")
    gw_prom = leer_promedios(D / "average_energies_gws.txt")

    esp_phi = leer_espectros(D / "spectra_scalar_0.txt")   # columnas: k, Δ_campo, Δ_momento, multiplicidad
    esp_chi = leer_espectros(D / "spectra_scalar_1.txt")
    esp_gw = leer_espectros(D / "spectra_energy_gws.txt")  # columnas: k, dΩ_GW/dln k, multiplicidad
    t_esp = np.atleast_1d(np.loadtxt(D / "average_spectra_times.txt"))[: len(esp_gw)]
    k = esp_chi[0, :, 0]                                    # centros de bin (unidades de ω★)
    a_esp = np.interp(t_esp, fondo["t"], fondo["a"])        # factor de escala en esos tiempos

    lam = float(PARS.get("lambda", "nan"))
    q = float(PARS.get("q", "nan"))
    kIR = float(PARS.get("kIR", "nan"))
    fStar = float(PARS.get("initial_amplitudes", "nan").split()[0])
    omegaStar = np.sqrt(lam) * fStar
    return (
        D,
        PARS,
        a_esp,
        chi_prom,
        energias,
        esp_chi,
        esp_gw,
        esp_phi,
        fStar,
        fondo,
        friedmann,
        gw_prom,
        k,
        kIR,
        lam,
        omegaStar,
        phi_prom,
        q,
        t_esp,
    )


@app.cell(hide_code=True)
def _(D, PARS, fStar, k, lam, mo, omegaStar, q, t_esp):
    mo.md(f"""
    **Corrida:** `{D.name}`. N = {PARS.get('N')}, kIR = {PARS.get('kIR')}, dt = {PARS.get('dt')},
    tMax = {PARS.get('tMax')}, kCutOff = {PARS.get('kCutOff')}, GWs = {PARS.get('withGWs')},
    semilla = {PARS.get('baseSeed', '—')}.

    λ = {lam:.3g}, q = g²/λ = {q:.4g}, f★ = {fStar:.4g} GeV, ω★ = √λ f★ = {omegaStar:.4g} GeV.
    Hay {len(t_esp)} tiempos con espectros (de τ = {t_esp[0]:.0f} a {t_esp[-1]:.0f}) y
    {len(k)} bins en k (de {k[0]:.2f} a {k[-1]:.2f}).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Fondo: expansión y reparto de la energía

    En λφ⁴ el inflatón oscila como radiación: en promedio la presión es p = ρ/3 (w = 1/3). En
    tiempo conforme, entonces, a crece linealmente (a′ ≈ constante) y la energía total cae
    como a⁻⁴. Qué mirar:

    * **a(τ) y a′:** a′ oscila alrededor de un valor fijo; si el fluido fuera materia (w = 0),
      a′ crecería.
    * **w(τ):** la ecuación de estado instantánea oscila mucho, pero su promedio tiende a 1/3.
    * **Conservación:** la diferencia relativa entre los dos lados de la ecuación de Friedmann
      tiene que ser ≪ 1.
    * **Reparto de energía:** al principio todo es energía cinética y potencial del inflatón.
      Cuando la resonancia se vuelve no lineal aparecen los términos de **gradiente** (∇φ, ∇χ)
      y de **interacción** (½ q φ²χ²). Los gradientes son la fuente de las GWs (sección 5).
    """)
    return


@app.cell
def _(guardar, C_AZUL, C_NARANJA, C_TINTA2, energias, fondo, friedmann, np, plt):
    _t = fondo["t"]
    _fig, _ax = plt.subplots(2, 2, figsize=(10, 6.2), sharex=True)

    _ax[0, 0].plot(_t, fondo["a"], color=C_AZUL)
    _ax[0, 0].set_ylabel("a(τ)")
    _ax[0, 0].set_title("Factor de escala")

    _ax[0, 1].plot(_t, fondo["aDot"], color=C_AZUL, lw=0.8)
    _ax[0, 1].set_ylabel("a′ = da/dτ")
    _ax[0, 1].set_title("a′ constante en promedio ⇒ radiación")

    # Ecuación de estado instantánea y promediada en una ventana móvil (~2 oscilaciones)
    _E = energias
    _kin = _E["E^kin_scal0"] + _E["E^kin_scal1"]
    _grad = _E["E^grad_scal0"] + _E["E^grad_scal1"]
    _pot = _E["Vpot_term_0"] + _E["Vpot_term_1"]
    _w = (_kin - _grad / 3 - _pot) / (_kin + _grad + _pot)
    _n = max(1, int(round(15 / np.diff(_E["t"]).mean())))
    _w_prom = np.convolve(_w, np.ones(_n) / _n, mode="valid")
    _t_prom = np.convolve(_E["t"], np.ones(_n) / _n, mode="valid")
    _ax[1, 0].plot(_E["t"], _w, color="#c9d9ef", lw=0.6, label="instantánea")
    _ax[1, 0].plot(_t_prom, _w_prom, color=C_AZUL, label="promedio móvil")
    _ax[1, 0].axhline(1 / 3, color=C_NARANJA, ls="--", lw=1)
    _ax[1, 0].text(_E["t"][-1], 1 / 3 + 0.05, "w = 1/3", color=C_TINTA2, ha="right")
    _ax[1, 0].set_ylabel("w = p/ρ")
    _ax[1, 0].set_xlabel("τ (tiempo de programa)")
    _ax[1, 0].legend(loc="lower right")

    _ax[1, 1].semilogy(friedmann["t"], np.abs(friedmann["rel_diff_friedmann"]) + 1e-16, color=C_AZUL, lw=0.8)
    _ax[1, 1].set_ylabel("|error relativo de Friedmann|")
    _ax[1, 1].set_xlabel("τ (tiempo de programa)")
    _ax[1, 1].set_title("Conservación de la energía")
    _fig.tight_layout()
    guardar(_fig, "fondo")
    _fig
    return


@app.cell
def _(guardar, C_AMARILLO, C_AQUA, C_AZUL, C_NARANJA, energias, fondo, np, plt):
    _E = energias
    _tot = _E["E_tot"]
    _series = [
        ("cinética φ", _E["E^kin_scal0"], C_AZUL, "-"),
        ("potencial φ⁴/4", _E["Vpot_term_0"], C_AZUL, ":"),
        ("gradiente φ", _E["E^grad_scal0"], C_NARANJA, "-"),
        ("gradiente χ", _E["E^grad_scal1"], C_AQUA, "-"),
        ("cinética χ", _E["E^kin_scal1"], C_AQUA, ":"),
        ("interacción q φ²χ²/2", _E["Vpot_term_1"], C_AMARILLO, "-"),
    ]
    # Promedio móvil sobre ~1 oscilación del inflatón (período ≈ 7,4 en τ) para que se lea la tendencia
    _n = max(1, int(round(7.4 / np.diff(_E["t"]).mean())))
    _suave = lambda y: np.convolve(y, np.ones(_n) / _n, mode="valid")
    _ts = _suave(_E["t"])
    _fig, _ax = plt.subplots(1, 2, figsize=(10, 3.8), gridspec_kw={"width_ratios": [1.6, 1]})
    for _nom, _y, _c, _ls in _series:
        _ax[0].semilogy(_ts, np.maximum(_suave(_y / _tot), 1e-16), color=_c, ls=_ls, lw=1.3, label=_nom)
    _ax[0].set_ylim(1e-14, 2)
    _ax[0].set_ylabel("fracción de la energía total")
    _ax[0].set_xlabel("τ")
    _ax[0].legend(fontsize=8, ncol=2, loc="lower right")
    _ax[0].set_title("Reparto de la energía (promedio sobre una oscilación)")

    _a = np.interp(_E["t"], fondo["t"], fondo["a"])
    _ax[1].plot(_E["t"], _tot * _a**4, color=C_AZUL)
    _ax[1].set_ylabel("ρ_total · a⁴")
    _ax[1].set_xlabel("τ")
    _ax[1].set_title("ρ a⁴ (constante para radiación exacta)")
    _fig.tight_layout()
    guardar(_fig, "energia")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Campos: oscilación del inflatón y resonancia de χ

    **Teoría (Greene, Kofman, Linde y Starobinsky 1997; Dufaux et al. 2007).** Mientras χ es chico,
    cada modo del campo conforme X_k = a·χ_k obedece la ecuación de Lamé

    $$X_k'' + \left[\kappa^2 + q\,\mathrm{cn}^2(\tau;\,1/\sqrt2)\right] X_k = 0,$$

    donde κ es el k de programa y cn es el coseno elíptico de Jacobi (la forma exacta en que oscila
    el inflatón conforme en λφ⁴). Las soluciones crecen como e^{μ_k τ}; el **exponente de Floquet**
    μ_k depende de κ y de q. Abajo se calcula μ(κ) para el q de la corrida.

    **Advertencia:** la ecuación de Lamé supone a″ = 0 (radiación exacta). Al principio a′/a ≈ 0,8 es
    comparable a la frecuencia de oscilación, así que se esperan desvíos moderados respecto de μ
    de Floquet durante los primeros τ.
    """)
    return


@app.cell
def _(DIR_FINAL, ellipj, ellipk, energias, fondo, np, q, sys):
    def floquet_mu_vec(Ks, q, pasos=3000):
        """Exponente de Floquet de la ecuación de Lamé para muchos κ a la vez (RK4 sobre la
        matriz de transferencia en un período de cn²). Devuelve μ por unidad de τ (0 fuera de banda)."""
        m = 0.5
        T = 2 * ellipk(m)                           # período de cn²
        x = np.linspace(0.0, T, 2 * pasos + 1)      # puntos enteros y medios
        cn2 = ellipj(x, m)[1] ** 2
        h = T / pasos
        K2 = np.asarray(Ks, dtype=float) ** 2
        Y = np.tile(np.eye(2), (len(K2), 1, 1))

        def f(c, Y):
            out = np.empty_like(Y)
            out[:, 0, :] = Y[:, 1, :]
            out[:, 1, :] = -(K2 + q * c)[:, None] * Y[:, 0, :]
            return out

        for i in range(pasos):
            c0, cm, c1 = cn2[2 * i], cn2[2 * i + 1], cn2[2 * i + 2]
            k1 = f(c0, Y)
            k2 = f(cm, Y + h / 2 * k1)
            k3 = f(cm, Y + h / 2 * k2)
            k4 = f(c1, Y + h * k3)
            Y = Y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        tr = np.abs(Y[:, 0, 0] + Y[:, 1, 1]) / 2
        return np.where(tr > 1, np.arccosh(np.maximum(tr, 1)), 0.0) / T

    K_floq = np.linspace(0.0, 8.0, 401)
    mu_floq_1 = floquet_mu_vec(K_floq, q)        # suponiendo amplitud conforme 1 (la ingenua)
    mu_max_1 = float(mu_floq_1.max())

    # Amplitud conforme real del inflatón: después del transitorio inicial (a″ ≠ 0) el fondo
    # es un oscilador λΦ⁴ con energía conforme ρa⁴ = A⁴/4 (unidades de programa).
    _a = np.interp(energias["t"], fondo["t"], fondo["a"])
    _m = (energias["t"] >= 10) & (energias["t"] <= 60)
    A_conf = float((4 * np.mean(energias["E_tot"][_m] * _a[_m] ** 4)) ** 0.25)
    # Lamé con amplitud A: x → A x y κ → κ/A, así que μ_A(κ) = A · μ_1(κ/A)
    mu_floq = A_conf * floquet_mu_vec(K_floq / A_conf, q)
    _i = int(np.argmax(mu_floq))
    k_star, mu_max = float(K_floq[_i]), float(mu_floq[_i])
    _dentro = K_floq[mu_floq > mu_max / 2]
    banda = (float(_dentro.min()), float(_dentro.max()))

    # Chequeo cruzado con la implementación (escalar) de code/analisis_parametros.py
    sys.path.insert(0, str(DIR_FINAL / "code"))
    from analisis_parametros import floquet_mu as _floquet_mu_ref
    mu_ref_kstar = _floquet_mu_ref(1.24, q)
    return (
        A_conf,
        K_floq,
        banda,
        floquet_mu_vec,
        k_star,
        mu_floq,
        mu_floq_1,
        mu_max,
        mu_max_1,
        mu_ref_kstar,
    )


@app.cell(hide_code=True)
def _(A_conf, banda, k_star, mo, mu_max, mu_max_1, mu_ref_kstar, q):
    mo.md(f"""
    **La amplitud importa.** La ecuación de Lamé de arriba supone que el inflatón conforme oscila con
    amplitud 1 (en unidades de f★). Pero en los primeros τ, mientras a″ ≠ 0, el fondo gana energía conforme:
    ρa⁴ pasa de 0,375 a un valor constante, y la amplitud real queda en **A = {A_conf:.4f}** (medida con
    ρa⁴ = A⁴/4 promediado en τ ∈ [10, 60]). Con amplitud A, todo se reescala: el tiempo por A y el momento
    por A, así que μ_A(κ) = A·μ₁(κ/A).

    **Floquet para q = {q:.4g}:** con amplitud 1, μ_max = {mu_max_1:.4f} en κ = 1,24 (la implementación
    independiente de `analisis_parametros.py` da {mu_ref_kstar:.4f}). **Con la amplitud medida**,
    μ_max = **{mu_max:.4f}** en κ★ = **{k_star:.2f}**, y la banda (μ > μ_max/2) va de {banda[0]:.2f} a
    {banda[1]:.2f}. Esta es la predicción que se compara con la simulación.
    """)
    return


@app.cell(hide_code=True)
def _(fondo, mo):
    _tmax = float(fondo["t"][-1])
    ventana_ajuste = mo.ui.range_slider(
        start=0, stop=round(_tmax), step=1,
        value=[min(20, round(0.07 * _tmax)), min(55, round(0.2 * _tmax))],
        label="Ventana de la fase lineal (τ) para ajustar crecimientos exponenciales",
        full_width=True,
    )
    ventana_ajuste
    return (ventana_ajuste,)


@app.cell
def _(
    guardar,
    C_AQUA,
    C_AZUL,
    C_NARANJA,
    C_TINTA2,
    chi_prom,
    fondo,
    mu_max,
    np,
    phi_prom,
    plt,
    ventana_ajuste,
):
    _t = phi_prom["t"]
    _a = np.interp(_t, fondo["t"], fondo["a"])
    _t1, _t2 = ventana_ajuste.value
    _m = (_t >= _t1) & (_t <= _t2)
    _X = _a * chi_prom["rms(phi)"]
    mu_rms = float(np.polyfit(_t[_m], np.log(_X[_m]), 1)[0]) if _m.sum() > 2 else np.nan
    _b = np.polyfit(_t[_m], np.log(_X[_m]), 1)[1] if _m.sum() > 2 else 0.0

    _fig, _ax = plt.subplots(1, 2, figsize=(10, 3.8))
    _ax[0].plot(_t, _a * phi_prom["<phi>"], color=C_AZUL, lw=0.8, label="a·⟨φ⟩ (conforme)")
    _ax[0].set_xlabel("τ")
    _ax[0].set_ylabel("campo homogéneo (unidades de f★)")
    _ax[0].set_title("Inflatón: la amplitud conforme cae cuando χ le roba energía")
    _ax[0].legend(loc="lower right", fontsize=8)

    _ax[1].semilogy(_t, _X, color=C_AQUA, label="a·rms(χ)")
    _ax[1].semilogy(_t, _a * phi_prom["rms(phi)"], color=C_NARANJA, label="a·rms(δφ)")
    _tt = np.array([_t1, _t2])
    _ax[1].semilogy(_tt, np.exp(_b + mu_rms * _tt), color="#0b0b0b", ls="--", lw=2,
                    zorder=5, label=f"ajuste: μ = {mu_rms:.3f}")
    _ax[1].axvspan(_t1, _t2, color="#eeeeea", zorder=0)
    _ax[1].set_xlabel("τ")
    _ax[1].set_ylabel("dispersión conforme")
    _ax[1].set_title(f"Fluctuaciones (Floquet: μ_max = {mu_max:.3f})")
    _ax[1].legend(loc="lower right", fontsize=8)
    _fig.tight_layout()
    guardar(_fig, "campos")
    _fig
    return (mu_rms,)


@app.cell(hide_code=True)
def _(mo, mu_max, mu_rms):
    mo.md(f"""
    La pendiente de ln(a·rms χ) en la ventana da μ = **{mu_rms:.3f}**, contra μ_max = {mu_max:.3f}
    de Floquet. El rms mezcla todos los modos (también los que no resuenan y dominan al principio),
    así que es una medida gruesa: la sección 3 mide μ modo por modo, que es la comparación limpia.
    Las fluctuaciones de φ (naranja) crecen *después* y más rápido: las genera χ por
    re-dispersión (δφ se alimenta de χ², por eso crece a ~2μ).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Espectros de potencia

    CosmoLattice guarda Δ(k) = k³|f_k|²/(2π²), la contribución de cada escala a la varianza del campo
    por intervalo de ln k (⟨f²⟩ = ∫Δ d ln k). Se grafica a²Δ, el espectro del campo **conforme**, para
    que la dilución por la expansión no tape el crecimiento. Cada curva es un tiempo: de claro
    (temprano) a oscuro (tarde). En el panel de χ la franja sombreada es la banda de Floquet
    (μ > μ_max/2) y la línea vertical es κ★.
    """)
    return


@app.cell
def _(
    guardar,
    C_TINTA2,
    Normalize,
    RAMPA,
    a_esp,
    banda,
    esp_chi,
    esp_phi,
    k,
    k_star,
    np,
    plt,
    t_esp,
):
    _norm = Normalize(t_esp[0], t_esp[-1])
    _fig, _ax = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for _i, _t in enumerate(t_esp):
        _c = RAMPA(_norm(_t))
        _ax[0].loglog(k, a_esp[_i] ** 2 * esp_phi[_i, :, 1], color=_c, lw=0.8)
        _ax[1].loglog(k, a_esp[_i] ** 2 * esp_chi[_i, :, 1], color=_c, lw=0.8)
    _ax[1].axvspan(*banda, color="#eeeeea", zorder=0)
    _ax[1].axvline(k_star, color=C_TINTA2, ls="--", lw=1)
    _ax[1].text(k_star * 1.05, 1e-20, "κ★", color=C_TINTA2)
    _ax[0].set_title("Inflatón: a²Δ_δφ(k)")
    _ax[1].set_title("Campo hijo: a²Δ_χ(k)")
    for _x in _ax:
        _x.set_xlabel("k (unidades de ω★)")
    _ax[0].set_ylabel("a² Δ(k)")
    _ax[0].set_ylim(bottom=max(1e-24, np.nanmin(a_esp[0] ** 2 * esp_chi[0, :, 1]) / 10))
    _sm = plt.cm.ScalarMappable(norm=_norm, cmap=RAMPA)
    _fig.colorbar(_sm, ax=_ax, label="τ", fraction=0.03, pad=0.02)
    guardar(_fig, "espectros_campos")
    _fig
    return


@app.cell
def _(
    A_conf,
    C_AQUA,
    C_AZUL,
    C_TINTA2,
    K_floq,
    a_esp,
    esp_chi,
    guardar,
    k,
    mu_floq,
    mu_floq_1,
    mu_max,
    np,
    plt,
    t_esp,
    ventana_ajuste,
):
    # Exponente medido por modo: pendiente de ½ ln(a²Δ_χ) en la ventana lineal
    _t1, _t2 = ventana_ajuste.value
    _m = (t_esp >= _t1) & (t_esp <= _t2)
    _lnX = 0.5 * np.log(a_esp[:, None] ** 2 * esp_chi[:, :, 1])
    mu_k_medido = (np.polyfit(t_esp[_m], _lnX[_m], 1)[0] if _m.sum() > 2
                   else np.full(len(k), np.nan))
    _j = int(np.nanargmax(np.where(k < 3, mu_k_medido, -np.inf)))
    mu_medido_max, k_medido_max = float(mu_k_medido[_j]), float(k[_j])

    _fig, _ax = plt.subplots(figsize=(7.5, 3.8))
    _ax.plot(K_floq, mu_floq_1, color=C_AZUL, lw=1, ls=":", label="Floquet, amplitud 1")
    _ax.plot(K_floq, mu_floq, color=C_AZUL, label=f"Floquet, amplitud medida A = {A_conf:.3f}")
    _ax.plot(k, mu_k_medido, "o", color=C_AQUA, ms=4, mfc="white", mew=1.4,
             label=f"medido, τ ∈ [{_t1}, {_t2}]")
    _ax.axhline(0, color=C_TINTA2, lw=0.6)
    _ax.set_xlim(0, min(8, k[-1]))
    _ax.set_ylim(-0.05, max(mu_max, np.nanmax(mu_k_medido)) * 1.25)
    _ax.set_xlabel("k = κ (unidades de ω★)")
    _ax.set_ylabel("μ_k")
    _ax.set_title("Exponente de crecimiento por modo: teoría vs. simulación")
    _ax.legend(loc="upper right", fontsize=8)
    _fig.tight_layout()
    guardar(_fig, "mu_por_modo")
    _fig
    return k_medido_max, mu_k_medido, mu_medido_max


@app.cell(hide_code=True)
def _(k_medido_max, k_star, mo, mu_max, mu_max_1, mu_medido_max):
    mo.md(f"""
    En la banda principal el modo que más crece en la simulación está en k = {k_medido_max:.2f}, con
    μ = **{mu_medido_max:.3f}**. Floquet con la amplitud medida da μ_max = {mu_max:.3f} en κ★ = {k_star:.2f}
    (diferencia {abs(mu_medido_max / mu_max - 1):.1%}); con amplitud 1 daría {mu_max_1:.3f}
    (diferencia {abs(mu_medido_max / mu_max_1 - 1):.0%}). La forma de la banda y su borde superior también
    coinciden con la curva reescalada. Hay dos desvíos:

    * **Modos con k ≲ 0,75** crecen más rápido que lo que da Floquet. Son pocos modos (la caja tiene
      pocos vectores de onda largos), y es posible que los arrastre algún efecto no lineal temprano;
      queda abierto.
    * **Modos con k ≳ 4** crecen aunque están fuera de la banda (y por encima del corte kCutOff = 4 de
      las fluctuaciones iniciales, así que arrancan de casi cero). Eso no es resonancia de Floquet:
      es re-dispersión no lineal.
    """)
    return


@app.cell
def _(guardar, LogNorm, RAMPA, a_esp, banda, esp_chi, fondo, k, plt, t_esp):
    _Z = a_esp[:, None] ** 2 * esp_chi[:, :, 1]
    _fig, _ax = plt.subplots(figsize=(8, 3.8))
    _pc = _ax.pcolormesh(t_esp, k, _Z.T, cmap=RAMPA, norm=LogNorm(vmin=_Z.max() * 1e-14, vmax=_Z.max()),
                         shading="nearest")
    _ax.grid(False)
    for _b in banda:
        _ax.axhline(_b, color="white", ls=":", lw=0.8)
    _ax.set_yscale("log")
    _ax.set_ylim(k[0], k[-1])
    _ax.set_xlabel("τ")
    _ax.set_ylabel("k (unidades de ω★)")
    _ax.set_title("a²Δ_χ(k, τ): la resonancia empieza en la banda y después se esparce a k grandes")
    _fig.colorbar(_pc, ax=_ax, label="a² Δ_χ", pad=0.02)
    _fig.tight_layout()
    guardar(_fig, "mapa_chi")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Ondas gravitacionales

    CosmoLattice guarda el espectro **dΩ_GW/d ln k**: la fracción de la energía total que hay en
    GWs por intervalo de ln k. Su integral es ρ_GW/ρ (archivo `average_energies_gws.txt`).

    **Traslado a hoy.** λφ⁴ se comporta como radiación desde el principio, así que no hace falta
    suponer nada sobre cuándo termina el recalentamiento: desde el final de la simulación hasta hoy
    las GWs se diluyen como radiación y solo importa cuántos grados de libertad relativistas g★
    hay. Con conservación de la entropía:

    * a_e/a_0 = (g_{s,0}/g★)^{1/3} T_0/T_e, con T_e = (30ρ_e/(π²g★))^{1/4};
    * f_0 = (k/a_e)·ω★·(a_e/a_0)/(2π), pasado de GeV a Hz con 1/ħ;
    * h²Ω_GW,0 = h²Ω_γ,0 · (g_{s,0}^{4/3}/2) · g★^{-1/3} · dΩ_GW/d ln k|_e.

    Se usan T_0 = 2,7255 K, g_{s,0} = 3,931 y h²Ω_γ,0 = 2,473×10⁻⁵. (Con g★ = 100 el prefactor
    da ≈ 1,65×10⁻⁵, el valor usual de la literatura.) Nota: esto supone que el espectro ya dejó de
    cambiar al final de la corrida; el panel de la izquierda permite verificarlo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    g_star = mo.ui.number(start=10, stop=1000, step=1, value=100,
                          label="g★ (grados de libertad relativistas al final de la simulación)")
    g_star
    return (g_star,)


@app.cell
def _(energias, fStar, np, omegaStar):
    # Constantes (valores estándar; PDG)
    HBAR_GEV_S = 6.582119569e-25        # ħ en GeV·s
    KB_GEV_K = 8.617333262e-14          # k_B en GeV/K
    T0_GEV = 2.7255 * KB_GEV_K          # temperatura del CMB hoy
    GS0 = 3.931                          # g_s hoy
    H2_OMEGA_GAMMA = 2.473e-5            # h² Ω_γ hoy

    def gws_hoy(k_prog, dOmega_dlnk, a_fin, rho_fin_prog, g_star):
        """Traslada el espectro al final de la corrida a (f [Hz], h²Ω_GW hoy), suponiendo
        expansión de radiación hasta hoy con conservación de la entropía."""
        rho_fin = rho_fin_prog * fStar**2 * omegaStar**2          # GeV⁴
        T_fin = (30 * rho_fin / (np.pi**2 * g_star)) ** 0.25        # GeV
        a_fin_sobre_a0 = (GS0 / g_star) ** (1 / 3) * T0_GEV / T_fin
        k_fis = k_prog * omegaStar / a_fin                            # GeV
        f0 = k_fis * a_fin_sobre_a0 / (2 * np.pi * HBAR_GEV_S)        # Hz
        h2Omega0 = H2_OMEGA_GAMMA * GS0 ** (4 / 3) / 2 * g_star ** (-1 / 3) * dOmega_dlnk
        return f0, h2Omega0

    rho_fin_prog = float(energias["E_tot"][-1])
    return gws_hoy, rho_fin_prog


@app.cell
def _(
    guardar,
    C_AZUL,
    C_TINTA2,
    Normalize,
    RAMPA,
    a_esp,
    esp_gw,
    g_star,
    gw_prom,
    gws_hoy,
    k,
    np,
    plt,
    rho_fin_prog,
    t_esp,
):
    _norm = Normalize(t_esp[0], t_esp[-1])
    _fig, _ax = plt.subplots(1, 3, figsize=(12, 3.8))

    _ax[0].semilogy(gw_prom["t"], np.maximum(gw_prom["rhoGW_over_rho"], 1e-40), color=C_AZUL)
    _ax[0].set_ylim(bottom=max(1e-30, gw_prom["rhoGW_over_rho"][gw_prom["rhoGW_over_rho"] > 0].min()))
    _ax[0].set_xlabel("τ")
    _ax[0].set_ylabel("ρ_GW / ρ")
    _ax[0].set_title("Energía total en GWs")

    for _i, _t in enumerate(t_esp):
        _ax[1].loglog(k, esp_gw[_i, :, 1], color=RAMPA(_norm(_t)), lw=0.8)
    _y = esp_gw[-1, :, 1]
    _ax[1].set_ylim(_y[_y > 0].max() * 1e-12, _y.max() * 5)
    _ax[1].set_xlabel("k (unidades de ω★)")
    _ax[1].set_ylabel("dΩ_GW / d ln k")
    _ax[1].set_title("Espectro en la simulación (claro→oscuro = τ)")

    f0, h2Omega0 = gws_hoy(k, esp_gw[-1, :, 1], a_esp[-1], rho_fin_prog, g_star.value)
    _ok = h2Omega0 > 0
    _ax[2].loglog(f0[_ok], h2Omega0[_ok], color=C_AZUL)
    _jp = int(np.argmax(h2Omega0))
    f_pico, h2Omega_pico = float(f0[_jp]), float(h2Omega0[_jp])
    _ax[2].plot(f_pico, h2Omega_pico, "o", color=C_AZUL, ms=6, mfc="white", mew=1.6)
    _ax[2].annotate(f"pico: {h2Omega_pico:.2g}\nen f = {f_pico:.2g} Hz", (f_pico, h2Omega_pico),
                    xytext=(8, -28), textcoords="offset points", color=C_TINTA2, fontsize=8)
    _ax[2].set_ylim(h2Omega_pico * 1e-8, h2Omega_pico * 10)
    _ax[2].set_xlabel("f hoy (Hz)")
    _ax[2].set_ylabel("h² Ω_GW hoy")
    _ax[2].set_title(f"Hoy (g★ = {g_star.value:g})")
    _fig.tight_layout()
    guardar(_fig, "gws")
    _fig
    return f_pico, h2Omega_pico


@app.cell(hide_code=True)
def _(f_pico, gw_prom, h2Omega_pico, mo):
    mo.md(f"""
    Al final de la corrida ρ_GW/ρ = {gw_prom['rhoGW_over_rho'][-1]:.3g}. Hoy, el pico del espectro
    queda en h²Ω_GW ≈ **{h2Omega_pico:.2g}** a f ≈ **{f_pico:.2g} Hz**. Esto está muy por encima
    de la banda de LIGO/LISA, como es típico del precalentamiento a escala de GUT.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. ¿Cuándo crecen las GWs? Gradientes, no linealidad y producción de GWs

    La fuente de las GWs es la parte transversa y sin traza del tensor de anisotropía, que para
    escalares es Π_ij ∝ ∂_iφ∂_jφ + ∂_iχ∂_jχ. **Sin gradientes no hay GWs.** Por eso la producción
    sigue a la energía de gradiente, en tres etapas:

    1. **Fase lineal (resonancia):** X_k ∝ e^{μτ} en la banda. La fuente es cuadrática en χ, así
       que h ∝ e^{2μτ} y **ρ_GW ∝ e^{4μτ}**: las GWs crecen el doble de rápido (en el exponente)
       que la energía de χ.
    2. **Fin de la resonancia (τ_nl):** χ crece hasta que su masa inducida sobre el inflatón
       (q⟨X²⟩) se vuelve comparable a la masa propia del inflatón conforme (~1 en unidades de
       programa). La estimación analítica es
       $$\tau_{nl} \approx \tau_0 + \frac{1}{2\mu}\ln\frac{1}{q\,\langle X^2\rangle_{\rm banda}(\tau_0)},$$
       con ⟨X²⟩_banda la varianza inicial de a·χ contenida en la banda resonante.
    3. **Fase turbulenta:** la energía de gradiente satura en una fracción O(10 %); las GWs dejan de
       crecer exponencialmente y ρ_GW/ρ se aplana. El espectro se sigue corriendo a k grandes
       (cascada) cada vez más despacio.

    El umbral de abajo define "los gradientes se volvieron importantes": el primer τ en que la
    energía de gradiente (φ + χ) supera esa fracción de la energía total.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    umbral_gradiente = mo.ui.dropdown(
        options={"0,1 %": 1e-3, "1 %": 1e-2, "5 %": 5e-2, "10 %": 1e-1},
        value="1 %", label="Umbral de la fracción de energía en gradientes",
    )
    umbral_gradiente
    return (umbral_gradiente,)


@app.cell
def _(
    a_esp,
    banda,
    energias,
    esp_chi,
    gw_prom,
    k,
    kIR,
    mu_max,
    mu_medido_max,
    np,
    primer_cruce,
    q,
    t_esp,
    umbral_gradiente,
    ventana_ajuste,
):
    _E = energias
    frac_grad = (_E["E^grad_scal0"] + _E["E^grad_scal1"]) / _E["E_tot"]
    _Omega = gw_prom["rhoGW_over_rho"]
    _Omega_fin = _Omega[-1]

    # Varianza conforme inicial de χ contenida en la banda resonante: ∫ a²Δ d ln k, con d ln k = kIR/k
    _enbanda = (k >= banda[0]) & (k <= banda[1])
    X2_banda_0 = float(np.sum(a_esp[0] ** 2 * esp_chi[0, _enbanda, 1] * kIR / k[_enbanda]))

    # Inicio de la resonancia: el espectro en el modo que más crece supera ×10 su valor inicial
    _jk = int(np.argmin(np.abs(k - 0.5 * (banda[0] + banda[1]))))
    _Xk = a_esp**2 * esp_chi[:, _jk, 1]
    t_res = primer_cruce(t_esp, _Xk / _Xk[0], 10.0)

    tiempos = {
        "t_res": t_res,
        "t_nl_est_floquet": t_esp[0] + np.log(1 / (q * X2_banda_0)) / (2 * mu_max),
        "t_nl_est_medido": t_esp[0] + np.log(1 / (q * X2_banda_0)) / (2 * mu_medido_max),
        "t_grad": primer_cruce(_E["t"], frac_grad, umbral_gradiente.value),
        "t_GW_50": primer_cruce(gw_prom["t"], _Omega, 0.5 * _Omega_fin),
        "t_GW_90": primer_cruce(gw_prom["t"], _Omega, 0.9 * _Omega_fin),
    }

    # Ritmo de crecimiento de ρ_GW/ρ en la fase lineal, comparado con 4μ
    _t1, _t2 = ventana_ajuste.value
    _m = (gw_prom["t"] >= max(_t1, 1e-9)) & (gw_prom["t"] <= _t2) & (_Omega > 0)
    tasa_GW = float(np.polyfit(gw_prom["t"][_m], np.log(_Omega[_m]), 1)[0]) if _m.sum() > 2 else np.nan
    return X2_banda_0, frac_grad, tasa_GW, tiempos


@app.cell
def _(
    guardar,
    C_AMARILLO,
    C_AQUA,
    C_AZUL,
    C_NARANJA,
    C_TINTA2,
    a_esp,
    chi_prom,
    fondo,
    frac_grad,
    energias,
    gw_prom,
    np,
    plt,
    tiempos,
):
    # Tres curvas en un solo eje, cada una dividida por su valor máximo (índice común)
    _a = np.interp(chi_prom["t"], fondo["t"], fondo["a"])
    _X2 = (_a * chi_prom["rms(phi)"]) ** 2
    _curvas = [
        ("(a·rms χ)²", chi_prom["t"], _X2 / _X2.max(), C_AQUA),
        ("energía de gradiente / ρ", energias["t"], frac_grad / frac_grad.max(), C_NARANJA),
        ("ρ_GW / ρ", gw_prom["t"], gw_prom["rhoGW_over_rho"] / gw_prom["rhoGW_over_rho"].max(), C_AZUL),
    ]
    _fig, _ax = plt.subplots(figsize=(10, 4.2))
    for _nom, _t, _y, _c in _curvas:
        _ax.semilogy(_t, np.maximum(_y, 1e-30), color=_c, label=_nom)
    _marcas = [("t_res", "inicio resonancia", ":"), ("t_nl_est_floquet", "τ_nl estimado", "-."),
               ("t_grad", "gradientes > umbral", "--"), ("t_GW_90", "90 % de las GWs", "-")]
    for _clave, _txt, _ls in _marcas:
        _tv = tiempos[_clave]
        if np.isfinite(_tv):
            _ax.axvline(_tv, color=C_TINTA2, ls=_ls, lw=0.9)
            _ax.text(_tv + 1, 3e-24, _txt, rotation=90, va="bottom", fontsize=8, color=C_TINTA2)
    _ax.set_ylim(1e-24, 3)
    _ax.set_xlabel("τ")
    _ax.set_ylabel("cantidad / su máximo")
    _ax.set_title("Las GWs siguen a los gradientes: crecen durante la resonancia y se frenan al saturar")
    _ax.legend(loc="lower right", fontsize=8)
    _fig.tight_layout()
    guardar(_fig, "tiempos_gws")
    _fig
    return


@app.cell(hide_code=True)
def _(X2_banda_0, mo, mu_max, mu_medido_max, q, tasa_GW, tiempos, umbral_gradiente):
    _f = lambda x: f"{x:.1f}"
    mo.md(f"""
    | momento | τ | cómo se define |
    |---|---|---|
    | inicio de la resonancia | {_f(tiempos['t_res'])} | a²Δ_χ en el centro de la banda supera ×10 su valor inicial |
    | fin de la resonancia, estimado (μ de Floquet) | {_f(tiempos['t_nl_est_floquet'])} | fórmula de arriba con μ = {mu_max:.3f}, q⟨X²⟩_banda(0) = {q * X2_banda_0:.2g} |
    | fin de la resonancia, estimado (μ medido) | {_f(tiempos['t_nl_est_medido'])} | ídem con μ = {mu_medido_max:.3f} |
    | gradientes importantes | {_f(tiempos['t_grad'])} | energía de gradiente > {umbral_gradiente.selected_key} de ρ |
    | 50 % de las GWs finales | {_f(tiempos['t_GW_50'])} | ρ_GW/ρ alcanza la mitad de su valor final |
    | 90 % de las GWs finales | {_f(tiempos['t_GW_90'])} | ρ_GW/ρ alcanza el 90 % de su valor final |

    **Ritmo de crecimiento de las GWs en la fase lineal:** d ln(ρ_GW/ρ)/dτ = **{tasa_GW:.3f}**, contra
    4μ = {4 * mu_medido_max:.3f} (μ medido) y 4μ = {4 * mu_max:.3f} (Floquet). Si el cociente es ≈ 1,
    la producción lineal de GWs es la esperada para una fuente cuadrática en χ.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### En qué escala y en qué momento se produce cada GW

    El mapa muestra dΩ_GW/d ln k en el plano (τ, k). Los puntos marcan, para cada k, el momento en que
    ese modo alcanzó la mitad de su valor final: primero se llenan las escalas cercanas a 2κ★ (dos
    cuantos de χ de la banda producen un gravitón con k de hasta 2κ★) y después, más lentamente, las
    escalas más chicas por la cascada. La línea vertical punteada es el momento en que los gradientes
    superan el umbral elegido.

    **Horizonte.** El horizonte comóvil es k_H = a′/a: vale ≈ 0,83 en τ = 0 y cae por debajo de kIR
    antes de τ ≈ 3, así que toda la producción ocurre en modos bien adentro del horizonte (ondas que ya
    se propagan libremente). **Resolución:** si el espectro sigue creciendo en los k más altos de la
    red (k ≳ 20 a N = 128), esa parte es sensible al corte UV de la red y hay que confirmarla con N mayor.
    """)
    return


@app.cell
def _(guardar, C_TINTA2, LogNorm, RAMPA, esp_gw, k, k_star, np, plt, t_esp, tiempos):
    _Z = np.maximum(esp_gw[:, :, 1], 1e-300)
    _fin = _Z[-1]
    t_mitad_k = np.array([
        t_esp[np.flatnonzero(_Z[:, j] >= 0.5 * _fin[j])[0]] if _fin[j] > 0 else np.nan
        for j in range(len(k))
    ])
    _fig, _ax = plt.subplots(figsize=(9, 4.2))
    _pc = _ax.pcolormesh(t_esp, k, _Z.T, cmap=RAMPA, shading="nearest",
                         norm=LogNorm(vmin=_Z.max() * 1e-12, vmax=_Z.max()))
    _ax.grid(False)
    _ax.plot(t_mitad_k, k, "o", color="white", ms=3.5, mec=C_TINTA2, mew=0.6, label="τ en que el modo llega al 50 %")
    _ax.axhline(2 * k_star, color="white", ls=":", lw=0.9)
    _ax.text(t_esp[-1], 2 * k_star * 1.06, "2κ★", color="white", fontsize=8, ha="right")
    if np.isfinite(tiempos["t_grad"]):
        _ax.axvline(tiempos["t_grad"], color="white", ls="--", lw=0.9)
    _ax.set_yscale("log")
    _ax.set_ylim(k[0], k[-1])
    _ax.set_xlabel("τ")
    _ax.set_ylabel("k (unidades de ω★)")
    _ax.set_title("dΩ_GW/d ln k (τ, k)")
    _ax.legend(loc="lower right", fontsize=8)
    _fig.colorbar(_pc, ax=_ax, label="dΩ_GW / d ln k", pad=0.02)
    _fig.tight_layout()
    guardar(_fig, "mapa_gws")
    _fig
    return (t_mitad_k,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Comparación con Dufaux et al. (2007)

    Dufaux, Bergman, Felder, Kofman y Uzan (arXiv:0707.0875, §VI.B) simularon exactamente este modelo con
    q = 120, pero con **λ = 10⁻¹⁴** (nosotros usamos 9×10⁻¹⁴), en una red de 256³ y hasta x = 240. Sus
    resultados de referencia son:

    | qué | Dufaux et al. | dónde |
    |---|---|---|
    | pico hoy | h²Ω_GW ∼ 3×10⁻¹¹ en f ∼ 7×10⁷ Hz | §VI.B y fig. 4 |
    | cola infrarroja al final | Ω_GW ∝ f | §VI.B |
    | fin de la resonancia paramétrica | x ≃ 90 | fig. 5 y texto |
    | (Ω_gw)_p en el pico al final de la resonancia | ∼ 10⁻⁹ en x ∼ 90 | texto después de la ec. 71 |
    | máximo de (Ω_gw)_p | ∼ 5×10⁻⁶ en x ∼ 150; después el pico y el IR no cambian | texto y fig. 6 |
    | crecimiento durante la resonancia | ρ_gw ∝ n², el doble del exponente del número de partículas | texto de la fig. 5 |
    | energía conforme | a⁴ρ ≃ 1,15 λφ₀⁴/4 | antes de la ec. 71 |

    **Cómo traducir.** Su tiempo es x = √λ φ₀ τ y su momento K = k/(√λ φ₀), con φ₀ su amplitud inicial.
    Lo que fija la dinámica en variables conformes es la amplitud conforme del inflatón *después* del
    transitorio: la de ellos es 1,15^{1/4} φ₀ ≈ 1,036 φ₀, y la nuestra A·f★. Por eso se compara en
    x = A·τ y K_A = k/A (el mismo reescalamiento para ambos, a menos del 3,6 % de ellos, que se ignora).
    Qué cambia con λ:

    * **Frecuencia hoy:** f ∝ λ^{1/4} a igual K (su ec. 72), así que su pico se mueve a
      7×10⁷ Hz × 9^{1/4} ≈ 1,2×10⁸ Hz.
    * **Amplitud:** (Ω_gw)_p ∼ α(aH/k★)² ∝ 1/(a_p² K★²) (su ec. 73): no depende de λ directamente, solo
      de cuándo se alcanza el pico. Con λ nueve veces mayor el ruido inicial es tres veces mayor y la
      resonancia termina ≈ ln 9/(2μ) ≈ 6 unidades de x antes, lo que cambia la amplitud apenas ∼10 %.
    * Para el traslado a hoy se usa además **su** convención (ec. 47: h²Ω = 9,3×10⁻⁶ (Ω_gw)_p, que equivale
      a tomar g★/g₀ = 100). La del notebook (sección 4) da un factor ≈ 1,8 mayor con g★ = 100.
    """)
    return


@app.cell
def _(
    A_conf,
    a_esp,
    esp_gw,
    fStar,
    gw_prom,
    k,
    lam,
    np,
    omegaStar,
    rho_fin_prog,
    t_esp,
):
    # Valores de referencia de Dufaux et al. 2007 (arXiv:0707.0875, §VI.B), λ = 1e-14, q = 120
    DUFAUX = {"lam": 1e-14, "h2Omega_pico": 3e-11, "f_pico": 7e7, "Omega_p_max": 5e-6,
              "x_Omega_p_max": 150, "x_fin_resonancia": 90, "Omega_p_x90": 1e-9}
    f_pico_dufaux_reescalado = DUFAUX["f_pico"] * (lam / DUFAUX["lam"]) ** 0.25

    x_esp = A_conf * t_esp              # tiempo en la variable x de Dufaux
    K_A = k / A_conf                    # momento en unidades de √λ·(amplitud conforme)

    # Traslado a hoy con la convención de Dufaux (ec. 47)
    _k_sobre_rho14 = (k * omegaStar / a_esp[-1]) / (rho_fin_prog * fStar**2 * omegaStar**2) ** 0.25
    f_D = _k_sobre_rho14 * 4e10
    h2Omega_D = 9.3e-6 * esp_gw[-1, :, 1]
    _jp = int(np.argmax(h2Omega_D))
    comparacion = {
        "h2Omega_pico_convD": float(h2Omega_D[_jp]),
        "f_pico_convD": float(f_D[_jp]),
        "pendiente_IR": float(np.polyfit(np.log(k[:6]), np.log(esp_gw[-1, :6, 1]), 1)[0]),
    }
    # (Ω_gw)_p en el pico: en x ≈ 90, en x ≈ 150 y al final
    _pico = esp_gw[:, :, 1].max(axis=1)
    for _x in (90, 150):
        _j = int(np.argmin(np.abs(x_esp - _x)))
        comparacion[f"Omega_p_x{_x}"] = float(_pico[_j])
        comparacion[f"x_real_{_x}"] = float(x_esp[_j])
        comparacion[f"K_pico_x{_x}"] = float(K_A[np.argmax(esp_gw[_j, :, 1])])
    comparacion["Omega_p_fin"] = float(_pico[-1])
    comparacion["K_pico_fin"] = float(K_A[np.argmax(esp_gw[-1, :, 1])])
    comparacion["x_fin"] = float(x_esp[-1])
    comparacion["K_A_max_red"] = float(K_A[-1])
    # crecimiento del pico entre x ≈ 170 y el final (Dufaux: no cambia después de x ∼ 150)
    _j170 = int(np.argmin(np.abs(x_esp - 170)))
    comparacion["crec_pico_desde_x170"] = float(_pico[-1] / _pico[_j170] - 1)
    _Om = gw_prom["rhoGW_over_rho"]
    _x_gw = A_conf * gw_prom["t"]
    comparacion["rhoGW_x150_sobre_final"] = float(np.interp(150, _x_gw, _Om) / _Om[-1])
    return DUFAUX, K_A, comparacion, f_D, f_pico_dufaux_reescalado, h2Omega_D, x_esp


@app.cell
def _(
    A_conf,
    C_AZUL,
    C_NARANJA,
    C_TINTA2,
    DUFAUX,
    K_A,
    Normalize,
    RAMPA,
    esp_gw,
    f_D,
    f_pico_dufaux_reescalado,
    guardar,
    gw_prom,
    h2Omega_D,
    np,
    plt,
    x_esp,
):
    _fig, _ax = plt.subplots(1, 3, figsize=(13, 4))

    # (a) como la fig. 6 de Dufaux: espectro acumulado de x = 90 a 240 cada 10
    _xs = np.arange(90, 241, 10)
    _norm = Normalize(_xs[0], _xs[-1])
    for _x in _xs:
        _j = int(np.argmin(np.abs(x_esp - _x)))
        _ax[0].loglog(K_A, esp_gw[_j, :, 1], color=RAMPA(_norm(_x)), lw=0.9)
    _ax[0].axhline(DUFAUX["Omega_p_max"], color=C_NARANJA, ls="--", lw=1)
    _ax[0].text(0.25, DUFAUX["Omega_p_max"] * 1.3, "máximo de Dufaux (x ∼ 150)", color=C_TINTA2, fontsize=8)
    _ax[0].axvspan(K_A[-1], 60, color="#eeeeea", zorder=0)
    _ax[0].text(K_A[-1] * 1.05, 2e-9, "fuera de\nesta red", color=C_TINTA2, fontsize=8)
    _ax[0].set_xlim(0.2, 60)
    _ax[0].set_ylim(1e-9, 2e-5)
    _ax[0].set_xlabel("K = k / (√λ · amplitud conforme)")
    _ax[0].set_ylabel("(Ω_gw)_p = dΩ_GW / d ln k")
    _ax[0].set_title("Como la fig. 6 de Dufaux: x = 90 → 240")

    # (b) hoy, con la convención de Dufaux (ec. 47)
    _ok = h2Omega_D > 0
    _ax[1].loglog(f_D[_ok], h2Omega_D[_ok], color=C_AZUL, label="este piloto (λ = 9×10⁻¹⁴)")
    _ax[1].plot(DUFAUX["f_pico"], DUFAUX["h2Omega_pico"], "s", color=C_TINTA2, ms=7, mfc="white",
                label="pico de Dufaux (λ = 10⁻¹⁴)")
    _ax[1].plot(f_pico_dufaux_reescalado, DUFAUX["h2Omega_pico"], "D", color=C_NARANJA, ms=7,
                label="ídem, llevado a λ = 9×10⁻¹⁴")
    _f0 = f_D[_ok][0]
    _ax[1].loglog(f_D[_ok][:12], h2Omega_D[_ok][0] * (f_D[_ok][:12] / _f0), color=C_TINTA2, ls=":", lw=1,
                  label="∝ f (cola IR de Dufaux)")
    _ax[1].set_ylim(1e-14, 3e-10)
    _ax[1].set_xlabel("f hoy (Hz)")
    _ax[1].set_ylabel("h² Ω_GW hoy (convención de Dufaux)")
    _ax[1].set_title("Hoy: comparación con la fig. 4")
    _ax[1].legend(fontsize=7.5, loc="lower center")

    # (c) como la fig. 5: energía total en GWs contra x
    _ax[2].semilogy(A_conf * gw_prom["t"], np.maximum(gw_prom["rhoGW_over_rho"], 1e-30), color=C_AZUL)
    for _x, _txt, _ha, _dx in ((DUFAUX["x_fin_resonancia"], "fin de la\nresonancia\n(Dufaux)", "right", -4),
                               (DUFAUX["x_Omega_p_max"], "máximo\n(Dufaux)", "left", 4)):
        _ax[2].axvline(_x, color=C_TINTA2, ls="--", lw=0.9)
        _ax[2].text(_x + _dx, 1e-24, _txt, fontsize=8, color=C_TINTA2, ha=_ha)
    _ax[2].set_ylim(1e-26, 1e-4)
    _ax[2].set_xlabel("x = A·τ")
    _ax[2].set_ylabel("ρ_GW / ρ")
    _ax[2].set_title("Como la fig. 5: energía en GWs contra x")
    _fig.tight_layout()
    guardar(_fig, "comparacion_dufaux")
    _fig
    return


@app.cell(hide_code=True)
def _(DUFAUX, comparacion, f_pico_dufaux_reescalado, mo):
    _c = comparacion
    mo.md(f"""
    | qué | este piloto | Dufaux et al. |
    |---|---|---|
    | pico hoy (convención de Dufaux) | h²Ω = {_c['h2Omega_pico_convD']:.2g} en f = {_c['f_pico_convD']:.2g} Hz | {DUFAUX['h2Omega_pico']:.0g} en {DUFAUX['f_pico']:.0g} Hz → {f_pico_dufaux_reescalado:.2g} Hz con nuestro λ |
    | pendiente IR de dΩ/d ln k | {_c['pendiente_IR']:.2f} | 1 (Ω ∝ f) |
    | (Ω_gw)_p en el pico, x ≈ 90 | {_c['Omega_p_x90']:.2g} (x = {_c['x_real_90']:.0f}, K = {_c['K_pico_x90']:.2f}) | ∼ 10⁻⁹ |
    | (Ω_gw)_p en el pico, x ≈ 150 | {_c['Omega_p_x150']:.2g} (x = {_c['x_real_150']:.0f}, K = {_c['K_pico_x150']:.2f}) | ∼ 5×10⁻⁶ |
    | (Ω_gw)_p en el pico, al final | {_c['Omega_p_fin']:.2g} (x = {_c['x_fin']:.0f}, K = {_c['K_pico_fin']:.2f}) | igual que en x ∼ 150 |
    | cambio del pico entre x ≈ 170 y el final | {_c['crec_pico_desde_x170']:+.0%} | ≈ 0 |
    | ρ_GW en x = 150 respecto del final | {_c['rhoGW_x150_sobre_final']:.0%} | "aumenta levemente" después |
    | K máximo de la red | {_c['K_A_max_red']:.0f} | el espectro cae en K ≈ 50 (fig. 6) |
    """)
    return


if __name__ == "__main__":
    app.run()
