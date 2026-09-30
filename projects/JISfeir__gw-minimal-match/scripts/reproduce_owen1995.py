#!/usr/bin/env python3
"""Reproduce the central numerical calculation in Owen (1995/1996).

This script evaluates the noise moments in Eqs. (18), builds the preliminary
metric in Eq. (33), projects out coalescence time with Eq. (34), and reports
the metric determinant, eigenvalues, and square-grid spacings.

Run from the repository root:

    python scripts/reproduce_owen1995.py

The output is deterministic and is written to data/owen1995_reproduction.json.
It uses only the Python standard library.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "data" / "owen1995_reproduction.json"
Q_VALUES = (1, 4, 7, 9, 10, 12, 13, 15, 17)
SOLAR_MASS_SECONDS = 4.9254909476412675e-6


def noise_integral(q: int, cutoff_ratio: float) -> float:
    """Return Owen Eq. (18a) with f_c/f_0 -> infinity."""

    # With t=1/x, the semi-infinite integral becomes a smooth finite one:
    # I(q) = integral_0^(1/r) 5 t^(q/3)/(t^6 + 2 t^2 + 2) dt.
    def integrand(t: float) -> float:
        return 5.0 * t ** (q / 3.0) / (t**6 + 2.0 * t**2 + 2.0)

    return adaptive_simpson(integrand, 0.0, 1.0 / cutoff_ratio, 1e-12)


def adaptive_simpson(function, lower: float, upper: float, tolerance: float) -> float:
    """Integrate a smooth scalar function with recursive adaptive Simpson."""

    def simpson(a: float, b: float, fa: float, fm: float, fb: float) -> float:
        return (b - a) * (fa + 4.0 * fm + fb) / 6.0

    a, b = lower, upper
    m = 0.5 * (a + b)
    fa, fm, fb = function(a), function(m), function(b)
    whole = simpson(a, b, fa, fm, fb)

    def recurse(a, b, fa, fm, fb, estimate, tol, depth):
        m = 0.5 * (a + b)
        lm, rm = 0.5 * (a + m), 0.5 * (m + b)
        flm, frm = function(lm), function(rm)
        left = simpson(a, m, fa, flm, fm)
        right = simpson(m, b, fm, frm, fb)
        correction = left + right - estimate
        if depth == 0 or abs(correction) <= 15.0 * tol:
            return left + right + correction / 15.0
        return (
            recurse(a, m, fa, flm, fm, left, tol / 2.0, depth - 1)
            + recurse(m, b, fm, frm, fb, right, tol / 2.0, depth - 1)
        )

    return recurse(a, b, fa, fm, fb, whole, tolerance, 30)


def normalized_moments(cutoff_ratio: float) -> dict[int, float]:
    """Return J(q) = I(q)/I(7) for all moments needed by Eq. (38)."""

    integrals = {q: noise_integral(q, cutoff_ratio) for q in Q_VALUES}
    return {q: value / integrals[7] for q, value in integrals.items()}


def dimensionless_premetric(j: dict[int, float]) -> list[list[float]]:
    """Return gamma/(2*pi*f_0)^2 from Eqs. (33) and (38).

    In units of 2*pi*f_0, the phase derivatives are
    psi_0=x, psi_1=(3/5)x^(-5/3), psi_2=x^(-1).
    """

    means = [j[4], (3.0 / 5.0) * j[12], j[10]]
    second = [
        [j[1], (3.0 / 5.0) * j[9], j[7]],
        [(3.0 / 5.0) * j[9], (9.0 / 25.0) * j[17],
         (3.0 / 5.0) * j[15]],
        [j[7], (3.0 / 5.0) * j[15], j[13]],
    ]
    return [
        [0.5 * (second[row][col] - means[row] * means[col]) for col in range(3)]
        for row in range(3)
    ]


def projected_metric(gamma: list[list[float]]) -> list[list[float]]:
    """Project out time of coalescence using Owen Eq. (34)."""

    return [
        [gamma[row][col] - gamma[0][row] * gamma[0][col] / gamma[0][0]
         for col in (1, 2)]
        for row in (1, 2)
    ]


def symmetric_2x2_eigensystem(matrix: list[list[float]]) -> tuple[list[float], list[list[float]]]:
    """Return descending eigenvalues and matching unit-vector columns."""

    a, b, d = matrix[0][0], matrix[0][1], matrix[1][1]
    radius = math.hypot(0.5 * (a - d), b)
    eigenvalues = [0.5 * (a + d) + radius, 0.5 * (a + d) - radius]
    columns: list[list[float]] = []
    for value in eigenvalues:
        vector = [b, value - a] if abs(b) > abs(value - d) else [value - d, b]
        norm = math.hypot(*vector)
        columns.append([component / norm for component in vector])
    return eigenvalues, [[columns[col][row] for col in range(2)] for row in range(2)]


def chirp_time_area(f0_hz: float, minimum_component_mass_solar: float) -> float:
    """Integrate the physical wedge area int d(tau_1)d(tau_2) in seconds^2.

    The mass upper limit is infinity, as in Owen Sec. III B.  We integrate the
    absolute Jacobian of Eqs. (35)-(36) in (M, eta).  eta=y^3 regularizes the
    integrable endpoint at eta=0.
    """

    m_min = minimum_component_mass_solar * SOLAR_MASS_SECONDS
    a, b = 743.0 / 336.0, 11.0 / 4.0
    coefficient_1 = (5.0 / 256.0) * (math.pi * f0_hz) ** (-8.0 / 3.0)
    coefficient_2 = (5.0 / 192.0) * (math.pi * f0_hz) ** -2.0

    def transformed_integrand(y: float) -> float:
        if y == 0.0:
            return 0.0
        eta = y**3
        minimum_total_mass = 2.0 * m_min / (1.0 - math.sqrt(1.0 - 4.0 * eta))
        jacobian_after_m_integration = (
            coefficient_1 * coefficient_2 * (3.0 / 8.0) * eta**-3
            * ((2.0 / 3.0) * a - b * eta) * minimum_total_mass ** (-8.0 / 3.0)
        )
        return jacobian_after_m_integration * 3.0 * y**2

    return adaptive_simpson(transformed_integrand, 0.0, (0.25) ** (1.0 / 3.0), 1e-11)


def reproduce_case(name: str, fs_over_f0: float, f0_hz: float,
                   minimal_match: float = 0.97) -> dict:
    """Compute all central metric quantities for one historical PSD."""

    j = normalized_moments(fs_over_f0)
    gamma = dimensionless_premetric(j)
    metric = projected_metric(gamma)
    eigenvalues, eigenvectors = symmetric_2x2_eigensystem(metric)

    # Owen Eq. (50), restoring the factor (2*pi*f_0)^2 in each eigenvalue.
    spacings_seconds = [
        math.sqrt(2.0 * (1.0 - minimal_match)
                  / ((2.0 * math.pi * f0_hz) ** 2 * value))
        for value in eigenvalues
    ]
    area_seconds_squared = chirp_time_area(f0_hz, 0.2)
    sqrt_det_dimensionless = math.sqrt(
        metric[0][0] * metric[1][1] - metric[0][1] ** 2
    )
    number_of_templates = (
        (2.0 * math.pi * f0_hz) ** 2 * sqrt_det_dimensionless
        * area_seconds_squared / (2.0 * (1.0 - minimal_match))
    )

    return {
        "name": name,
        "fs_over_f0": fs_over_f0,
        "f0_hz": f0_hz,
        "minimal_match": minimal_match,
        "minimum_component_mass_solar": 0.2,
        "chirp_time_coordinate_area_seconds_squared": area_seconds_squared,
        "J": {str(q): j[q] for q in Q_VALUES},
        "gamma_divided_by_2pi_f0_squared": gamma,
        "g_divided_by_2pi_f0_squared": metric,
        "sqrt_det_g_divided_by_2pi_f0_squared": sqrt_det_dimensionless,
        "eigenvalues_divided_by_2pi_f0_squared": eigenvalues,
        "eigenvectors_columns_in_tau_basis": eigenvectors,
        "square_grid_spacings_ms_at_MM_0p97": [1e3 * value for value in spacings_seconds],
        "square_grid_template_count_at_MM_0p97": number_of_templates,
    }


def compute() -> dict:
    """Return both historical benchmark cases and a consistency identity."""

    mm = 0.97
    return {
        "source": "Owen, arXiv:gr-qc/9511032v1, Eqs. (17), (18), (33), (34), (50)",
        "method": "adaptive quadrature; analytic mass integral; symmetric eigendecomposition",
        "initial_ligo": reproduce_case("initial LIGO", 1.0 / 5.0, 200.0, mm),
        "advanced_ligo": reproduce_case("advanced LIGO", 1.0 / 7.0, 70.0, mm),
        "event_rate_fraction_at_MM_0p97": mm**3,
        "event_rate_loss_at_MM_0p97": 1.0 - mm**3,
        "paper_reported_benchmarks": {
            "initial_ligo": {
                "chirp_time_area_seconds_squared": 0.18,
                "eigenvalues_divided_by_2pi_f0_squared": [0.721, 0.00427],
                "square_grid_spacings_ms_at_MM_0p97": [0.22, 2.9],
                "square_grid_template_count_at_MM_0p97": 2.7e5,
                "computing_power_gflops_at_event_loss_0p1": 20.0,
            },
            "advanced_ligo": {
                "chirp_time_area_seconds_squared": 24.0,
                "eigenvalues_divided_by_2pi_f0_squared": [1.25, 0.00984],
                "square_grid_spacings_ms_at_MM_0p97": [0.49, 5.6],
                "square_grid_template_count_at_MM_0p97": 8.4e6,
                "computing_power_gflops_at_event_loss_0p1": 270.0,
            },
        },
        "typo_check": {
            "statement": "Eqs. (44)-(45) must scale with (1-MM)^-1, not MM^-1.",
            "reason": "For N=2, Eq. (16) has denominator 2(1-MM), as repeated in Eq. (43).",
        },
    }


def verify(result: dict) -> None:
    """Fail loudly if the central reproduction drifts away from the paper."""

    printed_metrics = {
        "initial_ligo": [[0.552, 0.304], [0.304, 0.173]],
        "advanced_ligo": [[1.01, 0.486], [0.486, 0.246]],
    }
    for case_name, printed in printed_metrics.items():
        computed = result[case_name]["g_divided_by_2pi_f0_squared"]
        for row in range(2):
            for column in range(2):
                if not math.isclose(computed[row][column], printed[row][column], abs_tol=0.006):
                    raise AssertionError(
                        f"{case_name} metric[{row},{column}]={computed[row][column]} "
                        f"does not reproduce Owen's printed {printed[row][column]}"
                    )
        if min(result[case_name]["eigenvalues_divided_by_2pi_f0_squared"]) <= 0.0:
            raise AssertionError(f"{case_name} projected metric is not positive definite")

    printed_areas = {"initial_ligo": 0.18, "advanced_ligo": 24.0}
    for case_name, printed in printed_areas.items():
        computed = result[case_name]["chirp_time_coordinate_area_seconds_squared"]
        if not math.isclose(computed, printed, rel_tol=0.06):
            raise AssertionError(
                f"{case_name} area={computed} differs from Owen's Monte Carlo value {printed}"
            )


def main() -> None:
    result = compute()
    verify(result)
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
