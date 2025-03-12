import numpy as np

def perform_polynomial_decryption(degree: int, modulus: int, key: List[int], encrypted_data: List[int]) -> List[int]:
    # Convert the key and encrypted data to numpy arrays
    key = np.array(key)
    encrypted_data = np.array(encrypted_data)

    # Compute the polynomial coefficients
    coefficients = np.polydiv(key, encrypted_data)[0]

    # Compute the decrypted data
    decrypted_data = np.polyval(coefficients, encrypted_data) % modulus

    # Return the decrypted data as a list
    return decrypted_data.tolist()
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