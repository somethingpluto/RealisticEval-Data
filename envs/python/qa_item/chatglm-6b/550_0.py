
from typing import Tuple, Union
import numpy as np

# Define the constant for conversion: Boltzmann constant in keV/K
k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K

def convert_log10_K_to_keV(T_log10_K: Union[float, Tuple]) -> float or Tuple:
    """
    Converts temperature from log10(K) to keV for a given input ( scalar or tuple).k_B_over_keV = 8.617333262145e-5

    Args:
        T_log10_K (float or tuple): The temperature in log10(K). Can be a scalar or a tuple of temperatures.

    Returns:
        float or tuple: The temperature(s) in keV corresponding to the input.

    Raises:
        ValueError: If the input is not a scalar (int or float) or a tuple.
    """
    if T_log10_K is not Union[float, Tuple]:
        raise ValueError("Input must be a scalar (int or float) or a tuple.")

    if T_log10_K is not float:
        raise ValueError("Input must be a float.")

    if len(T_log10_K)!= 2 or T_log10_K[0]!= T_log10_K[1]:
        raise ValueError("Invalid input format.")

    # Convert log10(K) to Kelvin
    T_K = np.log10(np.exp(-k_B_over_keV * T_log10_K))

    # Convert Kelvin to keV
    return T_K / k_B_over_keV

import unittest

k_B_over_keV = 8.617333262145e-5  # eV/K to keV/K
class TestConvertLog10KToKeV(unittest.TestCase):

    def test_scalar_input(self):
        """Test conversion of a single scalar log10(K) value."""
        T_log10_K = 3.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_tuple_input(self):
        """Test conversion of a tuple of log10(K) values."""
        T_log10_K = (2.0, 3.0, 4.0)
        expected_results = tuple(10 ** t * k_B_over_keV for t in T_log10_K)
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertEqual(result, expected_results)

    def test_zero_input(self):
        """Test conversion of log10(K) = 0."""
        T_log10_K = 0.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_negative_input(self):
        """Test conversion of a negative log10(K) value."""
        T_log10_K = -1.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_large_tuple_input(self):
        """Test conversion of a large tuple of log10(K) values."""
        T_log10_K = (1.0, 2.0, 3.0, 4.0, 5.0)
        expected_results = tuple(10 ** t * k_B_over_keV for t in T_log10_K)
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertEqual(result, expected_results)

    def test_single_large_value(self):
        """Test conversion of a large log10(K) value."""
        T_log10_K = 10.0
        expected_result = 10 ** T_log10_K * k_B_over_keV
        result = convert_log10_K_to_keV(T_log10_K)
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_invalid_input(self):
        """Test conversion with invalid input (string)."""
        T_log10_K = "invalid"
        with self.assertRaises(ValueError):
            convert_log10_K_to_keV(T_log10_K)

if __name__ == '__main__':
    unittest.main()