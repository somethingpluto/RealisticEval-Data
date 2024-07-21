import unittest

from total.t8.adapted import perform_polynomial_decryption


class TestPolynomialDecryption(unittest.TestCase):

    def test_basic_decryption(self):
        # Test basic decryption functionality
        self.assertEqual(
            perform_polynomial_decryption(3, 5, [1, 2, 3], [4, 0, 2]),
            [3, 3, 4]
        )

    def test_with_zero_modulus(self):
        # Test with modulus as zero (should handle modulus zero case, but here just for logical completeness)
        self.assertEqual(
            perform_polynomial_decryption(3, 0, [1, 1, 1], [1, 1, 1]),
            [0, 0, 0]
        )

    def test_with_large_numbers(self):
        # Test with larger numbers and wrap-around functionality
        self.assertEqual(
            perform_polynomial_decryption(2, 100, [50, 75], [150, 200]),
            [100, 25]
        )
