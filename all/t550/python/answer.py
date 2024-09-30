import numpy as np

# Define the constant for conversion: Boltzmann constant in keV/K
k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K


def convert_log10_K_to_keV(T_log10_K):
    """
    Converts temperature from log10(K) to keV for a given input (scalar or tuple).

    Args:
        T_log10_K (float or tuple): The temperature in log10(K). Can be a scalar or a tuple of temperatures.

    Returns:
        float or tuple: The temperature(s) in keV corresponding to the input.

    Raises:
        ValueError: If the input is not a scalar (int or float) or a tuple.
    """

    # Check if the input is a scalar (int or float)
    if isinstance(T_log10_K, (int, float)):
        T_kelvin = 10 ** T_log10_K  # Convert log10(K) to K
        return T_kelvin * k_B_over_keV  # Convert K to keV

    # Check if the input is a tuple
    elif isinstance(T_log10_K, tuple):
        return tuple(10 ** t * k_B_over_keV for t in T_log10_K)  # Convert each value

    # Raise an error for unsupported input types
    else:
        raise ValueError("Input must be a scalar (int or float) or a tuple of temperatures.")