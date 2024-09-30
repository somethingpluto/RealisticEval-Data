import numpy as np

# Define the constant for conversion: Boltzmann constant in keV/K
k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K


def get_T_in_log10_Kelvin(T_keV):
    """
    Converts temperature from keV to log10(K) for a given input (scalar or tuple).

    Args:
        T_keV (float or tuple): The temperature in keV. Can be a scalar or a tuple of temperatures.

    Returns:
        float or tuple: The temperature(s) in log10(K) corresponding to the input.

    Raises:
        ValueError: If the input is not a scalar (int or float) or a tuple.
    """

    # Check if the input is a scalar (int or float)
    if isinstance(T_keV, (int, float)):
        # Calculate log10(K) for the scalar value
        return np.log10(T_keV / k_B_over_keV)

    # Check if the input is a tuple
    elif isinstance(T_keV, tuple):
        # Calculate log10(K) for each element in the tuple
        return tuple(np.log10(t / k_B_over_keV) for t in T_keV)

    # Raise an error for unsupported input types
    else:
        raise ValueError("Input must be a scalar (int or float) or a tuple of temperatures.")