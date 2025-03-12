import * as crypto from 'crypto';

/**
 * Generates a 16-byte random salt value, hashes the provided password with that salt
 * using the SHA-256 hash algorithm, and returns the combined salt and hashed password.
 * 
 * @param password - The password to be hashed.
 * @returns A Buffer containing the salt followed by the hashed password.
 */
function hashPasswordWithSalt(password: string): Buffer {
    const salt = crypto.randomBytes(16);
    const hash = crypto.createHash('sha256').update(password + salt.toString('hex')).digest();
    return Buffer.concat([salt, hash]);
}

// Unit tests
import { expect } from 'chai';
import 'mocha';

describe('hashPasswordWithSalt', () => {
    it('should return a buffer of length 32', () => {
        const result = hashPasswordWithSalt('testPassword');
        expect(result.length).to.equal(32);
    });

    it('should return a different hash for the same password', () => {
        const hash1 = hashPasswordWithSalt('testPassword');
        const hash2 = hashPasswordWithSalt('testPassword');
        expect(hash1).to.not.equal(hash2);
    });
});
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
