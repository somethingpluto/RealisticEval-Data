const crypto = require('crypto');

/**
 * Generates a 16-byte random salt value, hashes the provided password with that salt
 * using the SHA-256 hash algorithm, and returns the combined salt and hashed password.
 *
 * @param {string} password - The password to be hashed.
 * @returns {Buffer} A byte array containing the salt followed by the hashed password.
 */
function hashPasswordWithSalt(password) {
  // Generate a 16-byte random salt
  const salt = crypto.randomBytes(16);

  // Hash the password with the salt using SHA-256
  const hash = crypto.createHash('sha256').update(password + salt.toString('hex')).digest();

  // Combine the salt and the hashed password
  const saltedHash = Buffer.concat([salt, hash]);

  return saltedHash;
}
describe('Hashing Tests', () => {
    test('hashPasswordWithSalt returns a byte array with the correct length', () => {
        // Test that the hashPasswordWithSalt method returns a byte array with the correct length.
        const password = "testPassword";
        const result = hashPasswordWithSalt(password);
        // SHA-256 hash length is 32 bytes, and the salt length is 16 bytes
        expect(result.length).toBe(48);
    });

    test('salt is included in result', () => {
        // Test that the salt is correctly generated and included in the hash result.
        const password = "testPassword";
        const result = hashPasswordWithSalt(password);
        const salt = result.slice(0, 16); // First 16 bytes represent the salt
        expect(salt).not.toBeNull();
        expect(salt.length).toBe(16);
    });

    test('different passwords produce different hashes', () => {
        // Test that two different passwords produce different hashes, even with the same salt.
        const password1 = "password123";
        const password2 = "password456";
        const hash1 = hashPasswordWithSalt(password1);
        const hash2 = hashPasswordWithSalt(password2);
        expect(hash1.equals(hash2)).toBe(false); // Comparing Buffers
    });

    test('same password different salts', () => {
        // Test that the same password produces different hashes when hashed with different salts.
        const password = "password123";
        const hash1 = hashPasswordWithSalt(password);
        const hash2 = hashPasswordWithSalt(password);
        expect(hash1.equals(hash2)).toBe(false); // The salt is generated randomly, so the hashes should be different.
    });
});
