import math

# comment
def density(h):
    """Returns ISA air density in kg/m^3 at altitude h in metres."""
    density_sea_level = 1.225
    if h <= 11000:
        return density_sea_level * (1 - 2.2558e-5 * h) ** 4.2561
    else:
        rho_11 = density_sea_level * (1 - 2.2558e-5 * 11000) ** 4.2561
        g = 9.81
        R = 287.05
        T_11 = 216.65
        return rho_11 * math.exp(-g * (h - 11000) / (R * T_11))

def temperature(h):
    """Returns ISA temperature in Kelvin at altitude h in metres."""
    T0 = 288.15
    L  = 0.0065
    if h <= 11000:
        return T0 - L * h
    else:
        return 216.65

def pressure(h):
    """Returns ISA pressure in Pa at altitude h in metres."""
    p0 = 101325.0
    T  = temperature(h)
    T0 = 288.15
    g  = 9.81
    R  = 287.05
    L  = 0.0065
    return p0 * (T / T0) ** (g / (L * R))