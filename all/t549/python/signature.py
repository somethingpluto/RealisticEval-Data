from typing import Union, Tuple

import numpy as np

k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K


def get_T_in_log10_Kelvin(T_keV: Union[float, Tuple]):
    """
    Converts temperature from keV to log10(K) for a given input (scalar or tuple).k_B_over_keV = 8.617333262145e-5

    Args:
        T_keV (float or tuple): The temperature in keV. Can be a scalar or a tuple of temperatures.

    Returns:
        float or tuple: The temperature(s) in log10(K) corresponding to the input.

    Raises:
        ValueError: If the input is not a scalar (int or float) or a tuple.
    """
