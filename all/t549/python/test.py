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
