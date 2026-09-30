"""Analisis de parametros para comparar lphi4, lphi4U1 y lphi4SU2U1 de igual a igual.

Calcula, sin correr CosmoLattice, las cuatro cosas que hacen falta para elegir
los parametros de las corridas (ver ../paginas/analisis-parametros.html):

  1. lambda favorecida por las observaciones del CMB: para lambda*phi^4 puro y
     para el alpha-attractor T-model que usan el Art I y el Art II.
  2. El estado del inflaton al final de la inflacion (phi_*, phi'_*), para ver de
     donde salen los valores de los .in por defecto.
  3. El mapa de resonancia parametrica (exponente de Floquet) de la ecuacion de
     Lame del modelo lambda*phi^4 + g^2 phi^2 chi^2 para cada q candidato: en que
     momento k_* crece mas rapido el hijo, y con que ritmo mu.
  4. La traduccion de kIR, dt y tMax entre modelos, porque omega_* del codigo
     no es el mismo en lphi4 que en los modelos gauge.

Unidades: masa de Planck reducida m_p = 2.435e18 GeV, el valor de CosmoLattice
(TempLat/util/constants.h, reducedMPlanck).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipj, ellipk

MP = 2.435e18          # GeV, TempLat::Constants::reducedMPlanck
AS = 2.1e-9            # amplitud de las perturbaciones escalares (Planck 2018)
NS_PLANCK = (0.9649, 0.0042)
R_MAX = 0.036          # BICEP/Keck 2021, citado en Art II sec. 7.2


# ---------------------------------------------------------------------------
# 1. lambda observacional
# ---------------------------------------------------------------------------

def lphi4_puro(N):
    """lambda*phi^4/4 en slow-roll: lambda de la normalizacion del CMB, n_s y r a N e-folds.

    eps = 8 m_p^2/phi^2, eta = 12 m_p^2/phi^2, N = (phi^2 - phi_end^2)/(8 m_p^2)
    con phi_end^2 = 8 m_p^2 (eps = 1) => phi_N^2 = 8 m_p^2 (N + 1).
    A_s = V/(24 pi^2 m_p^4 eps) = lambda phi^6/(768 pi^2 m_p^6).
    """
    x2 = 8 * (N + 1)                      # (phi_N/m_p)^2
    lam = 768 * np.pi**2 * AS / x2**3
    eps, eta = 8 / x2, 12 / x2
    return {"lambda": lam, "n_s": 1 - 6 * eps + 2 * eta, "r": 16 * eps}


def t_model(p, M, N):
    """alpha-attractor T-model V = (Lambda^4/p) tanh^p(phi/M), todo en unidades de m_p.

    Fin de la inflacion en eps_V = 1: sinh(2 phi_*/M) = sqrt(2) p / M  (Art I ec. 459).
    N(phi) = (M^2/(4p)) [cosh(2 phi/M) - cosh(2 phi_*/M)].
    Devuelve Lambda^4 (en m_p^4) de A_s, n_s, r, y lambda_eff = Lambda^4/M^4 para p = 4
    (Art I ec. 457: lambda mu^{4-p} = Lambda^4 M^{-p}).
    """
    phi_end = M / 2 * np.arcsinh(np.sqrt(2) * p / M)
    c = np.cosh(2 * phi_end / M) + 4 * p * N / M**2
    phi = M / 2 * np.arccosh(c)
    s = np.sinh(2 * phi / M)
    eps = 2 * p**2 / (M**2 * s**2)
    # eta = V''/V, por diferencias finitas
    h = 1e-5 * M
    V = lambda f: np.tanh(f / M) ** p / p
    eta = (V(phi + h) - 2 * V(phi) + V(phi - h)) / h**2 / V(phi)
    Lam4 = AS * 24 * np.pi**2 * eps / V(phi)
    out = {"Lambda4_mp4": Lam4, "Lambda4_GeV4": Lam4 * MP**4, "n_s": 1 - 6 * eps + 2 * eta,
           "r": 16 * eps, "phi_end_mp": phi_end}
    if p == 4:
        out["lambda_eff"] = Lam4 / M**4
    return out


# ---------------------------------------------------------------------------
# 2. Estado al final de la inflacion para lambda*phi^4/4
# ---------------------------------------------------------------------------

def fin_inflacion_lphi4():
    """Integra el fondo exacto y devuelve (u, u') donde eps_H = 1 (a'' = 0).

    Con phi = m_p u y t = s/(sqrt(lambda) m_p) la ecuacion no depende de lambda:
    u'' + 3 h u' + u^3 = 0, h^2 = (u'^2/2 + u^4/4)/3. Entonces
    phi_* = u m_p y phidot_* = sqrt(lambda) m_p^2 u'.
    eps_H = (3/2) u'^2 / (u'^2/2 + u^4/4) = 1  <=>  u'^2 = u^4/4 = V.
    """
    u0 = 20.0
    v0 = -u0**3 / (3 * np.sqrt((u0**4 / 4) / 3))   # slow-roll: 3 h u' = -u^3

    def rhs(s, y):
        u, v = y
        h = np.sqrt((v**2 / 2 + u**4 / 4) / 3)
        return [v, -3 * h * v - u**3]

    def fin(s, y):
        return y[1]**2 - y[0]**4 / 4
    fin.terminal, fin.direction = True, 1
    sol = solve_ivp(rhs, (0, 1e4), [u0, v0], events=fin, rtol=1e-11, atol=1e-13)
    u, v = sol.y_events[0][0]
    return u, v


# ---------------------------------------------------------------------------
# 3. Resonancia parametrica: ecuacion de Lame
# ---------------------------------------------------------------------------
# Durante la fase lineal (Dufaux et al. 2007 ec. 68; GKLS 1997):
#   X'' + (K^2 + q cn^2(x, m=1/2)) X = 0,  K = k/(sqrt(lambda) phi_*),  x = sqrt(lambda) phi_* tau.
# En lphi4 (alpha = 1, omega_* = sqrt(lambda) phi_*) K es exactamente el k de programa y x
# el tiempo de programa. El exponente de Floquet mu da el crecimiento |X| ~ exp(mu x).

M_ELL = 0.5
T_CN2 = 2 * ellipk(M_ELL)           # periodo de cn^2


def floquet_mu(K, q, pasos=4000):
    """Exponente de Floquet de la ecuacion de Lame (por unidad de x)."""
    xs = np.linspace(0, T_CN2, pasos + 1)
    dx = xs[1] - xs[0]
    cn2 = ellipj(xs, M_ELL)[1] ** 2
    w2 = K**2 + q * cn2
    # RK4 sobre la matriz de transferencia (dos soluciones independientes a la vez)
    Y = np.eye(2)

    def f(i_w2, Y):
        return np.array([[0, 1], [-i_w2, 0]]) @ Y
    for i in range(pasos):
        w_a, w_b = w2[i], w2[i + 1]
        w_m = K**2 + q * ellipj(xs[i] + dx / 2, M_ELL)[1] ** 2
        k1 = f(w_a, Y)
        k2 = f(w_m, Y + dx / 2 * k1)
        k3 = f(w_m, Y + dx / 2 * k2)
        k4 = f(w_b, Y + dx * k3)
        Y = Y + dx / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    tr = np.trace(Y) / 2
    return float(np.log(abs(tr) + np.sqrt(max(tr**2 - 1, 0))) / T_CN2)


def banda_principal(q, Kmax=None, nK=240):
    """k_* (donde mu es maximo), mu_max, y el rango de K con mu > mu_max/2."""
    Kmax = Kmax or 2.0 * q**0.25 + 1
    Ks = np.linspace(0.0, Kmax, nK)
    mus = np.array([floquet_mu(K, q) for K in Ks])
    i = int(np.argmax(mus))
    dentro = Ks[mus > mus[i] / 2]
    return {"q": q, "K_star": float(Ks[i]), "mu_max": float(mus[i]),
            "K_media_altura": (float(dentro.min()), float(dentro.max())),
            "mu_K0": float(mus[0]), "K_grid": Ks, "mu_grid": mus}


# ---------------------------------------------------------------------------
# 4. Traduccion de unidades de programa entre modelos
# ---------------------------------------------------------------------------

def traducir(lattice_lphi4):
    """Convierte (kIR, dt, tMax, kCutOff) de lphi4 a los modelos gauge emparejados.

    Con el inflaton emparejado, |Phi_*| = phi_*/sqrt(2) y el codigo usa
    omega_* = sqrt(lambda)|Phi_*| = omega_*(lphi4)/sqrt(2). Un mismo k fisico es
    k~ = k/omega_*: sqrt(2) veces mas grande en los modelos gauge. Un mismo tiempo
    fisico es eta~ = omega_* tau: sqrt(2) veces mas chico.
    """
    s2 = np.sqrt(2)
    return {"kIR": lattice_lphi4["kIR"] * s2, "kCutOff": lattice_lphi4["kCutOff"] * s2,
            "dt": lattice_lphi4["dt"] / s2, "tMax": lattice_lphi4["tMax"] / s2,
            "N": lattice_lphi4["N"]}


def recomendacion(lam=9e-14, q=120.0, red_lphi4=None):
    """Parametros de los tres .in para una comparacion de igual a igual.

    Criterio: mismo estado inicial del inflaton (fin de la inflacion, eps_H = 1), y un
    unico canal resonante con el mismo q en los tres modelos:
      lphi4:      hijo escalar chi con q.
      lphi4U1:    campo U(1) con q_A = q               (gU1s = sqrt(q lambda)).
      lphi4SU2U1: q_A + q_B = q_eff = q, q_A = q_B = q/2 (Art I, discusion tras la tabla 1),
                  sin hijos escalares (qG = qH = 0).
    """
    red_lphi4 = red_lphi4 or {"N": 256, "kIR": 0.25, "kCutOff": 4.0, "dt": 0.01, "tMax": 300.0}
    u, v = fin_inflacion_lphi4()
    phi_s, dphi_s = u * MP, v * np.sqrt(lam) * MP**2
    s2 = np.sqrt(2)
    return {
        "lambda": lam,
        "lphi4": {"initial_amplitudes": phi_s, "initial_momenta": dphi_s, "q": q,
                  "fStar": phi_s, "omegaStar": np.sqrt(lam) * phi_s, **red_lphi4},
        "lphi4U1": {"cmplx_field_initial_norm": phi_s / s2, "cmplx_momentum_initial_norm": dphi_s / s2,
                    "gU1s": np.sqrt(q * lam), "fStar": phi_s / s2,
                    "omegaStar": np.sqrt(lam) * phi_s / s2, **traducir(red_lphi4)},
        "lphi4SU2U1": {"SU2Doublet_initial_norm": phi_s / s2,
                       "SU2Doublet_initial_momenta_norm": dphi_s / s2,
                       "qG": 0.0, "qH": 0.0,
                       "gU1s": np.sqrt(q / 2 * lam), "gSU2s": np.sqrt(4 * q / 2 * lam),
                       "gU1s_si_qA_igual_qB_igual_q": np.sqrt(q * lam),
                       "gSU2s_si_qA_igual_qB_igual_q": np.sqrt(4 * q * lam),
                       "fStar": phi_s / s2, "omegaStar": np.sqrt(lam) * phi_s / s2,
                       **traducir(red_lphi4)},
    }


def figura_bandas(ruta, qs=(120, 100, 240, 300), nK=200, Kmax=6.0):
    """Dibuja mu(K) para cada q: que tan rapido crece el hijo en cada momento K."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    colores = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]   # paleta de referencia, slots 1-4
    estilos = ["-", "--", "-.", ":"]
    notas = {120: "q = 120 (Dufaux et al., recomendado)", 100: "q = 100 (Manual, Art I)",
             240: "q = 240 (q_A + q_B si q_A = q_B = 120)", 300: "q = 300 (lphi4.in por defecto)"}
    Ks = np.linspace(0.0, Kmax, nK)
    fig, ax = plt.subplots(figsize=(8, 4.6), dpi=150)
    fig.patch.set_facecolor("#fcfcfb")
    ax.set_facecolor("#fcfcfb")
    for q, c, ls in zip(qs, colores, estilos):
        mus = np.array([max(floquet_mu(K, q), 0.0) for K in Ks])
        ax.plot(Ks, mus, color=c, lw=2, ls=ls, label=notas[q])
        i = int(np.argmax(mus))
        desplazamiento = {100: (8, -14), 240: (8, 4)}.get(q, (4, 4))   # 100 y 240 comparten K = 0
        ax.annotate(f"q={q}", (Ks[i], mus[i]), xytext=desplazamiento, textcoords="offset points",
                    fontsize=9, color="#3d3d3a")
    ax.set_xlabel("momento K = k / (√λ φ*)   [en lphi4 es el k de programa]", color="#3d3d3a")
    ax.set_ylabel("ritmo de crecimiento μ\n(el hijo crece como e^(μ·tiempo))", color="#3d3d3a")
    ax.set_title("Resonancia paramétrica en λφ⁴: dónde y qué tan rápido crece el campo hijo",
                 fontsize=11, color="#1a1a19", loc="left")
    ax.set_xlim(0, Kmax)
    ax.set_ylim(0, 0.26)
    ax.grid(color="#e4e3dc", lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#b5b4ab")
    ax.tick_params(colors="#5e5d59")
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    fig.tight_layout()
    fig.savefig(ruta, facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    print("=" * 78)
    print("1) lambda observacional")
    print("=" * 78)
    for N in (50, 55, 60):
        d = lphi4_puro(N)
        print(f"   lambda phi^4 puro, N = {N}: lambda = {d['lambda']:.3g}, "
              f"n_s = {d['n_s']:.4f}, r = {d['r']:.3f}")
    print(f"   Planck: n_s = {NS_PLANCK[0]} +- {NS_PLANCK[1]}; BICEP/Keck: r < {R_MAX}")
    val = t_model(2, 5.0, 60)
    print(f"   validacion Art II (p=2, M=5 m_p, N=60): Lambda^4 = {val['Lambda4_mp4']:.3g} m_p^4 "
          f"(Art II: 9.84e-10; la diferencia ~15% viene de A_s y de como se cuentan los e-folds)")
    for M in (5.0, 8.5, 10.0):
        for N in (50, 60):
            d = t_model(4, M, N)
            print(f"   T-model p=4, M = {M:>4} m_p, N = {N}: Lambda^4 = {d['Lambda4_GeV4']:.3g} GeV^4, "
                  f"lambda_eff = {d['lambda_eff']:.3g}, n_s = {d['n_s']:.4f}, r = {d['r']:.4f}")

    print()
    print("=" * 78)
    print("2) Estado al final de la inflacion (lambda phi^4/4, eps_H = 1)")
    print("=" * 78)
    u, v = fin_inflacion_lphi4()
    lam = 9e-14
    print(f"   u_* = phi_*/m_p = {u:.5f},  u'_* = phidot_*/(sqrt(lambda) m_p^2) = {v:.5f}")
    print(f"   con lambda = 9e-14: phi_* = {u * MP:.6g} GeV, phidot_* = {v * np.sqrt(lam) * MP**2:.6g} GeV^2")
    print("   .in por defecto v2.0 (lphi4.in):  5.6964e18, -4.86735e30")
    print("   Manual v1 (lphi4.in, = lphi4SU2U1.in x sqrt(2)): 7.42675e18, -6.2969e30")
    v1 = (7.42675e18 / MP, -6.2969e30 / (np.sqrt(lam) * MP**2))
    print(f"   Manual v1 en unidades adimensionales: u = {v1[0]:.4f}, u' = {v1[1]:.4f}, "
          f"eps_H = {1.5 * v1[1]**2 / (v1[1]**2 / 2 + v1[0]**4 / 4):.3f}")

    print()
    print("=" * 78)
    print("3) Resonancia parametrica (Lame): bordes de banda en K = 0 y k_* por q")
    print("=" * 78)
    for n in range(1, 13):
        lo, hi = n * (2 * n - 1), n * (2 * n + 1)
        mu_c = floquet_mu(0.0, 2 * n**2)
        mu_lo, mu_hi = floquet_mu(0.0, lo - 0.3), floquet_mu(0.0, hi + 0.3)
        if n in (1, 7, 8, 12):
            print(f"   banda n={n:>2}: K=0 inestable para {lo} < q < {hi}; mu(q=2n^2={2*n*n}) = {mu_c:.4f}; "
                  f"fuera de la banda mu = {mu_lo:.1e}, {mu_hi:.1e}")
    for q in (1.2, 3, 50, 60, 100, 120, 128, 150, 240, 300, 1370):
        b = banda_principal(q)
        print(f"   q = {q:>6}: K_* = {b['K_star']:.2f}, mu_max = {b['mu_max']:.4f}, "
              f"media altura en K = {b['K_media_altura'][0]:.2f}-{b['K_media_altura'][1]:.2f}, "
              f"mu(K=0) = {b['mu_K0']:.4f}, q^(1/4) = {q**0.25:.2f}")

    print()
    print("=" * 78)
    print("4) Traduccion de la red de lphi4 a los modelos gauge emparejados")
    print("=" * 78)
    base = {"N": 256, "kIR": 0.25, "kCutOff": 4.0, "dt": 0.01, "tMax": 300.0}
    print(f"   lphi4:            {base}")
    print(f"   lphi4U1/SU2U1:    { {k: round(v, 6) for k, v in traducir(base).items()} }")


if __name__ == "__main__":
    import sys
    if "--tabla" in sys.argv:
        for modelo, valores in recomendacion().items():
            if isinstance(valores, dict):
                print(modelo)
                for k, v in valores.items():
                    print(f"   {k:<32} = {v:.6g}")
            else:
                print(f"{modelo} = {valores:.6g}")
    elif "--figura" in sys.argv:
        import os
        destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures",
                               "bandas_resonancia_q.png")
        figura_bandas(destino)
        print(f"figura escrita en {os.path.normpath(destino)}")
    else:
        main()
