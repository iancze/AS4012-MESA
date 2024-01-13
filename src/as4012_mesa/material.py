import numpy as np
from . import constants


def mu(X, Y):
    """
    Parameters
    ----------

    X:
        hydrogen mass fraction
    Y:
        helium mass fraction

    Returns
    -------
    mean molecular weight [in units of mH]
    """
    return 4.0 / (6.0 * X + Y + 2.0)


def rho_func(P, T, X, Y):
    """

    Parameters
    ----------

    P:
        pressure
    T:
        temperature
    X:
        hydrogen mass fraction
    Y:
        helium mass fraction

    Returns
    -------
        equation of state
    """
    return P * mu(X, Y) * constants.mH / (constants.k_B * T)


def Z(X, Y):
    """
    mass fraction of all elements other than hydrogen and helium

    Parameters
    ----------
    X:
        mass fraction of hydrogen
    Y:
        mass fraction of helium

    Returns
    -------
    mass fraction of all elements other than hydrogen and helium
    """
    return 1.0 - X - Y


def kappa_bf(rho, T, X, Z):
    """
    bound-free opacity

    Parameters
    ----------

    rho:
        density
    T:
        temperature
    X:
        hydrogen mass fraction
    Z:
        metal mass fraction

    Returns
    -------
    bound-free opacity
    """
    # calculate other metals
    c1 = 1.85776232
    c2 = 0.3396116
    c3 = -2.38950921
    c4 = 3.34729929
    c5 = 6.61111851
    return (
        c1
        * (Z / 0.02)
        * (1.0 + X)
        * (rho / 1.0e4) ** c2
        * (T / 2.0e6) ** c3
        * (1.0 + c4 * np.exp(-((T / 10**c5) ** 2)))
    )


def kappa_ff(rho, T, X, Z):
    """
    free-free opacity

    Parameters
    ----------
    rho:
        density
    T:
        temperature
    X:
        hydrogen mass fraction
    Z:
        metal mass fraction

    Returns
    -------
    free-free opacity
    """
    return 4.0e18 * (1 - Z) * (1 + X) * rho * T ** (-3.52)


def kappa_es(X):
    """
    electron scattering opacity

    Parameters
    ----------
    X:
        hydrogen mass fraction

    Returns
    -------
    electron scattering opacity
    """
    return 0.02 * (1.0 + X)


def kappa(rho, T, X, Z):
    """
    total opacity

    Parameters
    ----------
    rho:
        density
    T:
        temperature
    X:
        hydrogen mass fraction
    Z:
        metal mass fraction

    Returns
    -------
    total opacity
    """
    return kappa_bf(rho, T, X, Z) + kappa_ff(rho, T, X, Z) + kappa_es(X)


def eps_pp(rho, T, X):
    """
    energy production via p-p-chain

    Parameters
    ----------
    rho:
        density
    T:
        temperature
    X:
        hydrogen mass fraction

    Returns
    -------
    energy production via p-p-chain
    """
    c1 = 3.28637058e-03
    c2 = 1.15744717e00
    c3 = 4.39985572e00
    return c1 * X * (rho / 80000.0) ** c2 * (T / 15e6) ** c3


def eps_cno(rho, T, X, XC):
    """
    energy production via C-N-O-cycle

    Parameters
    ----------
    rho:
        density
    T:
        temperature
    X:
        hydrogen mass fraction
    XC:
        Carbon mass fraction

    Returns
    -------
    energy production via p-p-chain
    """
    c1 = 1.03613328e-02
    c2 = 7.35735420e-01
    c3 = 2.04183062e01
    return c1 * X * (XC / 0.0025) * (rho / 1.0e5) ** c2 * (T / 15.0e6) ** c3


def eps(rho, T, X, XC):
    """
    total energy production

    Parameters
    ----------
    rho:
        density
    T:
        temperature
    X:
        hydrogen mass fraction
    Y:
        helium mass fraction
    XC:
        Carbon mass fraction

    Returns
    -------
    total energy production
    """
    return eps_pp(rho, T, X) + eps_cno(rho, T, X, XC)


# === log P-T gradients ===
def nabla_RE(P, T, L, m, X, Z):
    """
    radiative nabla

    Parameters
    ----------
    P:
        pressure
    T:
        temperature
    L:
        luminosity
    m:
        mass enclosed
    X:
        hydrogen mass fraction
    Y:
        helium mass fraction
    XC:
        Carbon mass fraction

    Returns
    -------
    nabla radiative

    """
    Y = 1 - X - Z
    rho = rho_func(P, T, X, Y)
    return (
        3.0
        * L
        * P
        * kappa(rho, T, X, Z)
        / (16.0 * np.pi * constants.a_sb * constants.cl * T**4 * constants.G * m)
    )


def nabla(P, T, L, m, X, Y):
    """
    calculate the nabla as the smaller of the radiative and adiabatic

    Parameters
    ----------
    P:
        pressure
    T:
        temperature
    L:
        luminosity
    m:
        mass enclosed
    X:
        hydrogen mass fraction
    Y:
        helium mass fraction
    XC:
        Carbon mass fraction

    Returns
    -------

    """
    n_rad = nabla_RE(P, T, L, m, X, Y)
    return min(n_rad, constants.nabla_AD)
