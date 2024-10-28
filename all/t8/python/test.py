import unittest


class TestDecryptFunction(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(perform_polynomial_decryption(4, 5, [1, 2, 3, 4], [5, 6, 7, 8]), [4, 4, 4, 4])

    def test_zero_secret_key(self):
        self.assertEqual(perform_polynomial_decryption(3, 7, [0, 0, 0], [6, 13, 20]), [6, 6, 6])

    def test_zero_ciphertext(self):
        self.assertEqual(perform_polynomial_decryption(3, 9, [1, 2, 3], [0, 0, 0]), [8, 7, 6])

    def test_large_values(self):
        self.assertEqual(perform_polynomial_decryption(2, 1000, [500, 500], [1000, 1000]), [500, 500])