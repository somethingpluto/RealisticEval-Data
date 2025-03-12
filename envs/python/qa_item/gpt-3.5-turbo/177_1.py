import hashlib
import os

def hash_password_with_salt(password: str) -> bytes:
    salt = os.urandom(16)
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(salt + password).digest()
    return salt + hashed_password
import unittest


class Tester(unittest.TestCase):
    def test_hashPasswordWithSaltLength(self):
        """Test that the hashPasswordWithSalt method returns a byte array with the correct length."""
        password = "testPassword"
        result = hash_password_with_salt(password)
        # SHA-256 hash length is 32 bytes, and the salt length is 16 bytes
        self.assertEqual(len(result), 48, "The combined salt and hashed password length should be 48 bytes.")

    def test_saltIsIncludedInResult(self):
        """Test that the salt is correctly generated and included in the hash result."""
        password = "testPassword"
        result = hash_password_with_salt(password)
        salt = result[:16]  # First 16 bytes represent the salt
        self.assertIsNotNone(salt, "Salt should not be None.")
        self.assertEqual(len(salt), 16, "Salt length should be 16 bytes.")

    def test_differentPasswordsProduceDifferentHashes(self):
        """Test that two different passwords produce different hashes, even with the same salt."""
        password1 = "password123"
        password2 = "password456"
        hash1 = hash_password_with_salt(password1)
        hash2 = hash_password_with_salt(password2)
        self.assertNotEqual(hash1, hash2, "Different passwords should produce different hashes.")

    def test_samePasswordDifferentSalts(self):
        """Test that the same password produces different hashes when hashed with different salts."""
        password = "password123"
        hash1 = hash_password_with_salt(password)
        hash2 = hash_password_with_salt(password)
        # The salt is generated randomly, so the hashes should be different.
        self.assertNotEqual(hash1, hash2, "The same password should produce different hashes with different salts.")
if __name__ == '__main__':
    unittest.main()