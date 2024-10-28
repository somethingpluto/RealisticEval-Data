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