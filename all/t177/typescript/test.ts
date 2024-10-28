describe('Tester', () => {
    test('hashPasswordWithSalt returns correct length', () => {
        const password = 'testPassword';
        const result = hashPasswordWithSalt(password);
        // SHA-256 hash length is 32 bytes, and the salt length is 16 bytes
        expect(result.length).toBe(48);
    });

    test('salt is included in result', () => {
        const password = 'testPassword';
        const result = hashPasswordWithSalt(password);
        const salt = result.slice(0, 16); // First 16 bytes represent the salt
        expect(salt).not.toBeNull();
        expect(salt.length).toBe(16);
    });

    test('different passwords produce different hashes', () => {
        const password1 = 'password123';
        const password2 = 'password456';
        const hash1 = hashPasswordWithSalt(password1);
        const hash2 = hashPasswordWithSalt(password2);
        expect(hash1).not.toEqual(hash2);
    });

    test('same password different salts', () => {
        const password = 'password123';
        const hash1 = hashPasswordWithSalt(password);
        const hash2 = hashPasswordWithSalt(password);
        // The salt is generated randomly, so the hashes should be different.
        expect(hash1).not.toEqual(hash2);
    });
});