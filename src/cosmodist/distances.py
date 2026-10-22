import numpy as np

# Constants
# -----------------------------------------------------------------------------

C = 299792.458      # km/s

# Functions
# -----------------------------------------------------------------------------

def hubble_distance(H0):
    """
    Return the Hubble distance in Mpc.
    """

    return C / H0

def E(z, Om):
    """Return the evolution factor of Hubble E(z) for a flat universe.
    """

    return np.sqrt(Om*(1 + z)**3 + (1 - Om))

