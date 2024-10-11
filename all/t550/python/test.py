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
