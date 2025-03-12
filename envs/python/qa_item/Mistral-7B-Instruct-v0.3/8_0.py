from sympy import symbols, poly, gcd_list
from functools import reduce

def perform_polynomial_decryption(degree: int, modulus: int, key: List[int], encrypted_data: List[int]) -> List[int]:
    # Define the symbol for the variable
    x = symbols('x')

    # Convert the key and encrypted_data to Sympy polynomials
    key_poly = poly(key[0], x, domain='ZZ/{}'.format(modulus))
    for k in key[1:]:
        key_poly *= x - k

    encrypted_poly = poly(encrypted_data[0], x, domain='ZZ/{}'.format(modulus))
    for e in encrypted_data[1:]:
        encrypted_poly *= x - e

    # Find the generating polynomial using the Berlekamp-Massey algorithm
    coefficients, _ = gcd_list(key_poly.all_coeffs(), encrypted_poly.all_coeffs())
    generating_poly = poly(coefficients[::-1], x, domain='ZZ/{}'.format(modulus))

    # Calculate the decrypted data
    decrypted_data = [(key_poly / generating_poly).subs(x, i) for i in range(degree)]

    return decrypted_data
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


def perform_polynomial_decryption(degree, modulus, key, encrypted_data):
    # Decrypts the polynomial based encryption by reversing the encryption steps
    decrypted_data = [0] * degree

    for index in range(degree):
        # Reversing encryption: subtract key and take modulo
        decrypted_data[index] = (encrypted_data[index] - key[index]) % modulus

    return decrypted_data

if __name__ == '__main__':
    unittest.main()