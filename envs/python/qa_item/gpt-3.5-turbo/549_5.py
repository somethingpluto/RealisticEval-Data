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
    if isinstance(T_keV, (int, float)):
        return np.log10(T_keV * k_B_over_keV)
    elif isinstance(T_keV, tuple):
        return tuple(np.log10(x * k_B_over_keV) for x in T_keV)
    else:
        raise ValueError("Input must be a scalar (int or float) or a tuple.")
import unittest

import numpy as np

k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K


class TestGetTInLog10Kelvin(unittest.TestCase):

    # Existing test cases here...

    def test_scalar_input_high_temperature(self):
        """Test with a high scalar input."""
        T_keV = 100.0
        expected_result = np.log10(T_keV / k_B_over_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_scalar_input_low_temperature(self):
        """Test with a low scalar input."""
        T_keV = 0.01
        expected_result = np.log10(T_keV / k_B_over_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_tuple_input_large_range(self):
        """Test with a tuple of temperatures over a large range."""
        T_keV = (0.1, 1.0, 10.0, 100.0, 1000.0)
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)

    def test_tuple_input_repeated_values(self):
        """Test with a tuple of repeated temperature values."""
        T_keV = (1.0, 1.0, 1.0)
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)

    def test_scalar_input_non_integer(self):
        """Test with a non-integer scalar input."""
        T_keV = 2.5
        expected_result = np.log10(T_keV / k_B_over_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_tuple_input_floating_point(self):
        """Test with a tuple of floating-point temperatures."""
        T_keV = (1.5, 2.5, 3.5)
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)


    def test_large_tuple_input(self):
        """Test with a large tuple of temperature values."""
        T_keV = tuple(np.arange(1, 1001, 1))  # Temperatures from 1 keV to 1000 keV
        expected_results = tuple(np.log10(t / k_B_over_keV) for t in T_keV)
        result = get_T_in_log10_Kelvin(T_keV)
        self.assertEqual(result, expected_results)

if __name__ == '__main__':
    unittest.main()