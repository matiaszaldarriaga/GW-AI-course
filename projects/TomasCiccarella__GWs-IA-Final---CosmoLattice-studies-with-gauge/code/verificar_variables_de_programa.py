"""Verifica con sympy las cuentas de la base teorica sobre variables de
programa, condiciones iniciales y restriccion de Gauss usadas por
CosmoLattice (ver ../paginas/bases-teoricas-modelos-gauge.html).

Cada bloque reproduce, de forma simbolica, una cuenta que en el codigo de
CosmoLattice (Final/CosmoLattice/include/..., Final/CosmoLattice/models/...)
aparece hecha "a mano" o implicita en los valores por defecto de los .in, y
chequea que sea consistente con las formulas publicadas en Figueroa et al.
2006.15122 ("Art I") y 2102.01031 ("User Manual"). No corre CosmoLattice ni
lee sus fuentes C++: es una verificacion algebraica independiente de esas
formulas, hecha a partir de lo que ambas fuentes (paper y codigo) dicen. La
unica lectura de archivos es la comparacion final (comparar_defaults), que toma los .in por defecto de
CosmoLattice/models/parameter-files/ para ponerlos en una misma escala (si
CosmoLattice/ no esta clonado, esa parte se saltea).
"""
import sympy as sp


def check(nombre, expr_deberia_ser_cero, mostrar=None):
    resultado = sp.simplify(expr_deberia_ser_cero)
    if resultado != 0:
        # sp.simplify no siempre cancela exponenciales complejas: se reintenta
        # pasando a senos/cosenos (expand_complex) antes de declarar FALLA.
        resultado = sp.simplify(sp.expand_complex(resultado))
    ok = resultado == 0
    estado = "OK" if ok else "FALLA"
    print(f"[{estado}] {nombre}")
    if mostrar is not None:
        print(f"       {mostrar}")
    if not ok:
        raise AssertionError(f"{nombre}: residuo no nulo -> {resultado}")
    return ok


print("=" * 78)
print("1) Reescalado del potencial lphi4: V = (lambda/4) phi^4")
print("=" * 78)

lam, fstar, phi_pr = sp.symbols('lambda f_star varphi_pr', positive=True)
omega_star = sp.sqrt(lam) * fstar          # models/lphi4.h: omegaStar = sqrt(lambda)*fStar
phi_fisico = fstar * phi_pr                # phi = fStar * phi_pr  (definicion de variable de programa)

V_fisico = sp.Rational(1, 4) * lam * phi_fisico**4
V_programa = sp.simplify(V_fisico / (fstar**2 * omega_star**2))

check(
    "V_programa == varphi_pr^4 / 4  (potentialTerms(0) del codigo: 0.25*fldS(0)^4)",
    V_programa - phi_pr**4 / 4,
    mostrar=f"V_programa calculado = {V_programa}",
)

print()
print("=" * 78)
print("2) Reescalado del acoplamiento hijo: q = g^2/lambda")
print("=" * 78)

q, chi_pr = sp.symbols('q varphi_pr_hijo', positive=True)
g = sp.sqrt(q * lam)                        # models/lphi4.h linea 97: g = sqrt(q*lambda)
chi_fisico = fstar * chi_pr

Vint_fisico = sp.Rational(1, 2) * g**2 * phi_fisico**2 * chi_fisico**2
Vint_programa = sp.simplify(Vint_fisico / (fstar**2 * omega_star**2))

check(
    "Vint_programa == (q/2) * varphi_pr^2 * chi_pr^2  (potentialTerms: 0.5*q*(fldS0*fldS1)^2)",
    Vint_programa - sp.Rational(1, 2) * q * phi_pr**2 * chi_pr**2,
    mostrar=f"Vint_programa calculado = {Vint_programa}",
)

print()
print("=" * 78)
print("3) Derivadas del potencial de programa (lo que codifican potDeriv/potDeriv2)")
print("=" * 78)

V_total_pr = phi_pr**4 / 4 + sp.Rational(1, 2) * q * phi_pr**2 * chi_pr**2

dV_dphi = sp.diff(V_total_pr, phi_pr)
dV_dchi = sp.diff(V_total_pr, chi_pr)
d2V_dphi2 = sp.diff(V_total_pr, phi_pr, 2)
d2V_dchi2 = sp.diff(V_total_pr, chi_pr, 2)

print(f"       dV_pr/d(varphi_pr)       = {dV_dphi}")
print(f"       dV_pr/d(chi_pr)          = {dV_dchi}")
print(f"       d^2V_pr/d(varphi_pr)^2   = {d2V_dphi2}")
print(f"       d^2V_pr/d(chi_pr)^2      = {d2V_dchi2}")
check(
    "d^2V_pr/d(varphi_pr)^2 en el punto homogeneo (chi_pr=0) define la masa m_pr^2 usada en omega_k",
    d2V_dphi2.subs(chi_pr, 0) - 3 * phi_pr**2,
)

print()
print("=" * 78)
print("4) Ecuacion de Friedmann en variables de programa (regla de la cadena)")
print("=" * 78)

alpha, omega_star_s, fstar_s, Mpl, rho_pr, a, H = sp.symbols(
    'alpha omega_star f_star M_pl rho_pr a H', positive=True
)

# Definicion del tiempo de programa: d(eta)/dt = a^{-alpha} * omega_star
# => a'(eta) = (da/dt) * (dt/d eta) = adot * a^{alpha}/omega_star
a_prima_sobre_a = H * a**alpha / omega_star_s      # esto ES a'/a, por la regla de la cadena de arriba

friedmann_fisica = H**2 - rho_pr * omega_star_s**2 * fstar_s**2 / (3 * Mpl**2)
# rho_fisica = omega_star^2 * fstar^2 * rho_pr  (reescalado de energias, Energies::kineticS etc.)

H2_en_terminos_de_rho_pr = sp.solve(friedmann_fisica, H**2)[0]
a_prima_sobre_a_cuadrado = sp.simplify(
    (a_prima_sobre_a**2).subs(H**2, H2_en_terminos_de_rho_pr)
)

formula_codigo = a**(2 * alpha) * fstar_s**2 * rho_pr / (3 * Mpl**2)

check(
    "(a'/a)^2 == a^(2 alpha) * (f_star/M_pl)^2 * rho_pr/3  (scalefactorinitializer.h / hubbleconstraint.h)",
    a_prima_sobre_a_cuadrado - formula_codigo,
    mostrar=f"(a'/a)^2 calculado = {a_prima_sobre_a_cuadrado}",
)

print()
print("=" * 78)
print("5) Normalizacion de las fluctuaciones de vacio iniciales")
print("=" * 78)

omega_star_n, fstar_n, Lbox, dx, Nlat, omega_k = sp.symbols(
    'omega_star f_star L dx N omega_k', positive=True
)

# fluctuationsgenerator.h: Norm(k) es el rms de Re(phi_k) (y, por separado, de Im(phi_k))
Norm_k = (omega_star_n / fstar_n) * (Lbox / dx**2) ** sp.Rational(3, 2) \
    * (1 / sp.sqrt(2 * omega_k)) * (1 / sp.sqrt(2))

# <|phi_k|^2> = <Re^2> + <Im^2> = 2*Norm(k)^2  (Re e Im independientes, misma varianza)
varianza_codigo = sp.simplify(2 * Norm_k**2)

# Art I eq. 435-436 / User Manual eq. 62, evaluada en a=1 (a_* = 1 por convencion) y con L = N*dx
varianza_paper = (omega_star_n / fstar_n) ** 2 * (Lbox / dx**2) ** 3 / (2 * omega_k)

check(
    "2*Norm(k)^2 == (omega_star/f_star)^2 (L/dx^2)^3 / (2 omega_k)  [formula publicada, a=1]",
    varianza_codigo - varianza_paper,
    mostrar=f"2*Norm(k)^2 = {varianza_codigo}",
)

# Chequeo adicional: con L = N*dx, (L/dx^2)^3 == (N/dx)^3, tal como se escribe en el paper
check(
    "(L/dx^2)^3 == (N/dx)^3 cuando L = N*dx",
    sp.simplify((Lbox / dx**2) ** 3 - (Nlat / dx) ** 3).subs(Lbox, Nlat * dx),
)

print()
print("=" * 78)
print("6) Condicion inicial del campo de gauge: solucion de la ley de Gauss discreta")
print("=" * 78)

kx, ky, kz = sp.symbols('k_x k_y k_z', real=True)
j0 = sp.symbols('j_0')  # corriente J_0 en espacio de Fourier (tratada como escalar simbolico)

# Derivada discreta "hacia atras" en espacio de Fourier: Delta_i^- f(n) <-> (1 - e^{-i k_i}) * f(k)
keff = [1 - sp.exp(-sp.I * kx), 1 - sp.exp(-sp.I * ky), 1 - sp.exp(-sp.I * kz)]

keff2 = sp.nsimplify(sp.simplify(sum(sp.conjugate(k) * k for k in keff)))
keff2_forma_cerrada = sp.simplify(
    keff2.rewrite(sp.cos).expand()
)
print(f"       |k_eff|^2 en forma cerrada = {keff2_forma_cerrada}")

# La condicion inicial (u1initializer.h) asigna pi_i(k) = conj(keff_i)/|keff|^2 * j0(k).
pi_asignado = [sp.conjugate(k) / keff2 * j0 for k in keff]

# La ley de Gauss discreta en espacio de Fourier es sum_i keff_i * pi_i(k) == j0(k).
lado_izquierdo = sp.simplify(sum(k * p for k, p in zip(keff, pi_asignado)))

check(
    "sum_i k_eff_i * pi_i(k) == j_0(k)  (la asignacion de u1initializer.h resuelve Gauss por construccion)",
    sp.simplify(lado_izquierdo - j0),
)

print()
print("=" * 78)
print("7) Escalar complejo de lphi4U1: que guarda el codigo, y el factor sqrt(2)")
print("=" * 78)

# Hipotesis a verificar: las dos componentes de fldCS son x = Re(phi), y = Im(phi),
# con phi = (phi_0 + i phi_1)/sqrt(2) (Art I ec. 9), o sea x = phi_0/sqrt(2).
eta = sp.symbols('eta')
x = sp.Function('x')(eta)
y = sp.Function('y')(eta)
r = sp.sqrt(x**2 + y**2)                   # norm(fldCS) = sqrt(total(pow<2>)), TempLat norm.h
Vr = sp.Function('V')

# Lagrangiano homogeneo de programa (a = 1): |phi'|^2 - V(|phi|). El codigo mide la
# energia cinetica como norm2(piCS)*a^-6, SIN el 1/2 de los singletes (energies.h).
L = sp.diff(x, eta)**2 + sp.diff(y, eta)**2 - Vr(r)
eom_x = sp.diff(sp.diff(L, sp.diff(x, eta)), eta) - sp.diff(L, x)   # = 0 en la solucion
x2_desde_lagrangiano = sp.solve(eom_x, sp.diff(x, eta, 2))[0]

# complexscalarkernels.h: pi' = ... - a^(3+alpha)/2 * derivCS, con
# derivCS_0 = potDerivNormCS / norm(fld) * fld(0)   (potential.h, derivComponentFromNorm)
dVdr = sp.Subs(sp.Derivative(Vr(sp.Symbol('rr')), sp.Symbol('rr')), sp.Symbol('rr'), r).doit()
x2_codigo = -sp.Rational(1, 2) * dVdr / r * x

check(
    "x'' del Lagrangiano |phi'|^2 - V(|phi|) == kernel del codigo (-1/2 * V'(|phi|) x/|phi|)",
    x2_desde_lagrangiano - x2_codigo,
)

# Mapa radial: el modulo del complejo equivale a un singlete varphi_r = sqrt(2)|phi|
lam7, R = sp.symbols('lambda R', positive=True)
Rp = sp.symbols("R'", real=True)
varphi_r, varphi_rp = sp.sqrt(2) * R, sp.sqrt(2) * Rp
check(
    "V = lambda |phi|^4 == (lambda/4) varphi_r^4 con varphi_r = sqrt(2)|phi|",
    lam7 * R**4 - lam7 / 4 * varphi_r**4,
)
check(
    "cinetica |phi'|^2 (codigo) == (1/2) varphi_r'^2 (singlete canonico)",
    Rp**2 - sp.Rational(1, 2) * varphi_rp**2,
)

# Parametro de resonancia gauge, Art I ec. 476 con omega_* de la ec. 463 (p = 4):
# varphi_* = sqrt(2)|Phi_*|,  omega_* = sqrt(lambda) varphi_*
gA, QA, gB, QB, Rs = sp.symbols('g_A Q_A g_B Q_B R_star', positive=True)
vphi_s = sp.sqrt(2) * Rs
om_463 = sp.sqrt(lam7) * vphi_s
om_codigo = sp.sqrt(lam7) * Rs                # lphi4U1.h: omegaStar = sqrt(lambda)*normCmplx0
qA_expr = QA**2 * gA**2 * vphi_s**2 / om_463**2
qB_expr = QB**2 * gB**2 * vphi_s**2 / (4 * om_463**2)
check("q_A* == Q_A^2 g_A^2 / lambda", qA_expr - QA**2 * gA**2 / lam7)
check("q_B* == Q_B^2 g_B^2 / (4 lambda)", qB_expr - QB**2 * gB**2 / (4 * lam7))
check(
    "omega_* del codigo == omega_* de la ec. 463 / sqrt(2)  (eleccion de unidades, no un error)",
    om_codigo - om_463 / sp.sqrt(2),
)


print()
print("=" * 78)
print("8) Doblete SU(2): carga total inicial nula y ley de Gauss no abeliana")
print("=" * 78)

# Doblete en componentes reales (Art I ec. 9): Phi = (phi0 + i phi1, phi2 + i phi3)/sqrt(2).
# Densidades de carga (Art I ecs. 447-448, sin constantes): J^A ~ Im[Phi^dag Phi'],
# J^a ~ Im[Phi^dag sigma_a Phi']. Se escriben como formas bilineales sum M_nm phi_n phi'_m.
ph = sp.symbols('phi0:4', real=True)
dph = sp.symbols('dphi0:4', real=True)
Phi = sp.Matrix([ph[0] + sp.I * ph[1], ph[2] + sp.I * ph[3]]) / sp.sqrt(2)
dPhi = sp.Matrix([dph[0] + sp.I * dph[1], dph[2] + sp.I * dph[3]]) / sp.sqrt(2)
sigmas = [sp.eye(2),
          sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
formas = []
for s_ in sigmas:                        # s_ = identidad -> carga U(1); sigma_a -> carga SU(2)
    dens = sp.expand(sp.im((Phi.H * s_ * dPhi)[0]))
    formas.append(sp.Matrix(4, 4, lambda n, m: dens.coeff(ph[n]).coeff(dph[m])))

# Modo cero de la carga = sum_x J(x) = sum_k sum_nm M_nm Re[conj(phi_n(k)) phi'_m(k)] (Parseval).
# Construccion de su2initializer.h en cada k (a = 1): amplitudes iguales para las ondas
# izquierda y derecha (ec. 452) y fase derecha de la componente a fijada por las demas (ec. 453).
Amp = sp.symbols('A0:4', positive=True)
thL = sp.symbols('thetaL0:4', real=True)
thR0, w0, hdot = sp.symbols('thetaR0 omega_0 aDot', real=True)
Lf = [sp.exp(sp.I * t) for t in thL]
Rf = [sp.exp(sp.I * thR0) * Lf[a_] * sp.conjugate(Lf[0]) for a_ in range(4)]   # rightPhases del codigo


def modo_cero(omegas):
    """Integrando en k de las cuatro cargas, con frecuencias omegas[a] por componente."""
    f = [Amp[a_] * (Lf[a_] + Rf[a_]) / 2 for a_ in range(4)]
    df = [-sp.I * omegas[a_] * Amp[a_] * (Lf[a_] - Rf[a_]) / 2 - hdot * f[a_] / sp.sqrt(2)
          for a_ in range(4)]
    return [sum(M[n, m] * sp.re(sp.expand_complex(sp.conjugate(f[n]) * df[m]))
                for n in range(4) for m in range(4) if M[n, m] != 0) for M in formas]


for nombre_carga, integrando in zip(["U(1)", "SU(2) a=1", "SU(2) a=2", "SU(2) a=3"],
                                    modo_cero([w0] * 4)):
    check(f"carga {nombre_carga}: modo cero nulo con la construccion de su2initializer.h",
          sp.simplify(sp.expand_complex(integrando)))

# Contraejemplo: con una frecuencia propia por componente (como escribe la ec. 442) la carga
# no se anula. Por eso el codigo usa omega0 (la de la componente 0) para las cuatro.
w_distintas = sp.symbols('omega0:4', positive=True)
residuo = sp.simplify(sp.expand_complex(modo_cero(w_distintas)[0]))
print(f"       con omega_a distintas, carga U(1) del modo cero = {residuo}")
if residuo == 0:
    raise AssertionError("se esperaba carga no nula con frecuencias distintas")
print("[OK] con frecuencias distintas por componente la carga NO se anula (justifica omega0 comun)")

# Ley de Gauss SU(2) discreta (Art I ec. 388; gausslaws.h::checkSU2):
#   sum_i [pi_i(x) - U_i^dag(x-i) pi_i(x-i) U_i(x-i)] / dx.
# En t = 0 el codigo pone B = 0 y unitariza: U_i = identidad. Entonces el transporte
# paralelo es trivial y cada color a cumple la misma ecuacion que U(1), que su2initializer.h
# resuelve con conj(k_eff)/|k_eff|^2 (chequeo 6).
pi_x = sp.Matrix(2, 2, sp.symbols('p0:4'))
pi_xm = sp.Matrix(2, 2, sp.symbols('q0:4'))
U = sp.eye(2)
check(
    "con U = identidad, pi(x) - U^dag pi(x-i) U == pi(x) - pi(x-i)  (divergencia hacia atras, como U(1))",
    sp.Matrix(pi_x - U.H * pi_xm * U - (pi_x - pi_xm)).norm(),
)


# Acoplamientos a los hijos escalares de lphi4SU2U1 (Manual ec. 90):
#   g^2 |Phi|^2 varphi^2  y  2 h^2 |Phi|^2 |phi|^2.
# Con f_* = |Phi_*| y omega_* = sqrt(lambda)|Phi_*| (lphi4SU2U1.h) el termino de programa es
# qG |Phi~|^2 varphi~^2 con qG = g^2/lambda; en el singlete equivalente varphi_r = sqrt(2)|Phi|
# el termino es (1/2) g^2 varphi_r^2 varphi^2, el mismo que el del hijo chi de lphi4.
gG, Phit, vpt = sp.symbols('g_G Phi_t varphi_t', positive=True)
fS = sp.symbols('f_S', positive=True)
term_prog = gG**2 * (fS * Phit)**2 * (fS * vpt)**2 / (fS**2 * (sp.sqrt(lam7) * fS)**2)
check("g^2|Phi|^2 varphi^2 / (f_*^2 omega_*^2) == (g^2/lambda) |Phi~|^2 varphi~^2  => qG = g^2/lambda",
      term_prog - gG**2 / lam7 * Phit**2 * vpt**2)
check("g^2 |Phi|^2 varphi^2 == (1/2) g^2 varphi_r^2 varphi^2 con varphi_r = sqrt(2)|Phi|  (= hijo de lphi4)",
      gG**2 * R**2 - sp.Rational(1, 2) * gG**2 * (sp.sqrt(2) * R)**2)

def leer_in(nombre):
    """Lee un .in por defecto de CosmoLattice (clave = valor, # comenta)."""
    import os
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "CosmoLattice", "models", "parameter-files", nombre)
    pars = {}
    for linea in open(ruta, encoding="utf-8"):
        linea = linea.split("#")[0].strip()
        if "=" in linea:
            k, v = (s.strip() for s in linea.split("=", 1))
            pars[k] = v.split()
    return pars


def comparar_defaults():
    """Los .in por defecto de lphi4 y lphi4U1, puestos en la misma escala."""
    p4, pU1, pSU2 = leer_in("lphi4.in"), leer_in("lphi4U1.in"), leer_in("lphi4SU2U1.in")
    lam = float(p4["lambda"][0])
    assert lam == float(pU1["lambda"][0])
    phi_s, dphi_s = float(p4["initial_amplitudes"][0]), float(p4["initial_momenta"][0])
    R_s, dR_s = float(pU1["cmplx_field_initial_norm"][0]), float(pU1["cmplx_momentum_initial_norm"][0])
    g_U1 = float(pU1["gU1s"][0])

    rho_lphi4 = 0.5 * dphi_s**2 + lam / 4 * phi_s**4        # singlete canonico
    rho_U1 = dR_s**2 + lam * R_s**4                          # |phi'|^2 + lambda|phi|^4
    return {
        "q_lphi4_default": float(p4["q"][0]),
        "qA_lphi4U1_default": g_U1**2 / lam,
        "qA_lphi4SU2U1_default": float(pSU2["gU1s"][0])**2 / float(pSU2["lambda"][0]),
        "qB_lphi4SU2U1_default": float(pSU2["gSU2s"][0])**2 / (4 * float(pSU2["lambda"][0])),
        "rho_ratio_U1_over_lphi4_default": rho_U1 / rho_lphi4,
        "rho_ratio_SU2U1_over_lphi4_default": (float(pSU2["SU2Doublet_initial_momenta_norm"][0])**2
                                               + lam * float(pSU2["SU2Doublet_initial_norm"][0])**4) / rho_lphi4,
        "gSU2s_matched_q300": (4 * float(p4["q"][0]) * lam) ** 0.5,
        "cmplx_norm_matched": phi_s / 2**0.5,
        "cmplx_momentum_matched": dphi_s / 2**0.5,
        "gU1s_matched_q300": (float(p4["q"][0]) * lam) ** 0.5,
    }


try:
    d = comparar_defaults()
except FileNotFoundError:
    print("       (CosmoLattice/ no esta clonado: se saltea la comparacion de .in por defecto)")
else:
    print(f"       q de lphi4.in                       = {d['q_lphi4_default']:.6g}")
    print(f"       q_A* de lphi4U1.in (gU1s^2/lambda)  = {d['qA_lphi4U1_default']:.6g}")
    print(f"       q_A*, q_B* de lphi4SU2U1.in         = {d['qA_lphi4SU2U1_default']:.6g}, {d['qB_lphi4SU2U1_default']:.6g}")
    print(f"       rho_inicial(U1) / rho_inicial(lphi4) = {d['rho_ratio_U1_over_lphi4_default']:.6g}")
    print(f"       rho_inicial(SU2U1) / rho_inicial(lphi4) = {d['rho_ratio_SU2U1_over_lphi4_default']:.6g}")
    print(f"       para igualar a lphi4: cmplx_field_initial_norm    = {d['cmplx_norm_matched']:.6g}")
    print(f"                             cmplx_momentum_initial_norm = {d['cmplx_momentum_matched']:.6g}")
    print(f"                             gU1s (q_A* = q = 300)       = {d['gU1s_matched_q300']:.6g}")
    print(f"       (SU2U1: SU2Doublet_initial_norm / _momenta_norm = los mismos dos valores de arriba)")
    print(f"                             gSU2s (q_B* = q = 300)      = {d['gSU2s_matched_q300']:.6g}")
    print(f"                             qG (hijo singlete = chi)    = {d['q_lphi4_default']:.6g}")

print()
print("Todas las verificaciones terminaron OK.")
