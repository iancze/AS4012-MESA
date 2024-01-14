# You may wish to review the [`scipy.integrate.odeint` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html).


def Lagrange(state, m):
    r, P, L, T = state
    drdm = 1 / (4.0 * pi * (r**2) * rho(P, T, X, Y))
    dPdm = -(grav * m) / (4 * pi * (r**4))
    dLdm = eps(P, T, X, Y, XC)
    dTdm = -(T / P) * grav * m / (4 * pi * (r**4)) * nabla(P, T, L, m, X, Y)
    return [drdm, dPdm, dLdm, dTdm]
