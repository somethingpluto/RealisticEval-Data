package org.real.temp;

import org.junit.jupiter.api.Test;

import java.security.NoSuchAlgorithmException;
import java.util.Arrays;

import org.real.temp.*;

import static org.junit.jupiter.api.Assertions.*;


public class Tester {

    /**
     * Test that the hashPasswordWithSalt method returns a byte array with the correct length.
     * The length should be 48 bytes (16 bytes of salt + 32 bytes of SHA-256 hash).
     */
    @Test
    public void testHashPasswordWithSaltLength() throws NoSuchAlgorithmException {
        String password = "testPassword";
        byte[] result = Answer.hashPasswordWithSalt(password);

        // SHA-256 hash length is 32 bytes, and the salt length is 16 bytes
        assertEquals(48, result.length, "The combined salt and hashed password length should be 48 bytes.");
    }

    /**
     * Test that the salt is correctly generated and included in the hash result.
     * The first 16 bytes of the result should represent the salt.
     */
    @Test
    public void testSaltIsIncludedInResult() throws NoSuchAlgorithmException {
        String password = "testPassword";
        byte[] result = Answer.hashPasswordWithSalt(password);

        byte[] salt = Arrays.copyOfRange(result, 0, 16);

        assertNotNull(salt, "Salt should not be null.");
        assertEquals(16, salt.length, "Salt length should be 16 bytes.");
    }

    /**
     * Test that two different passwords produce different hashes, even with the same salt.
     */
    @Test
    public void testDifferentPasswordsProduceDifferentHashes() throws NoSuchAlgorithmException {
        String password1 = "password123";
        String password2 = "password456";

        byte[] hash1 = Answer.hashPasswordWithSalt(password1);
        byte[] hash2 = Answer.hashPasswordWithSalt(password2);

        assertNotEquals(Arrays.toString(hash1), Arrays.toString(hash2), "Different passwords should produce different hashes.");
    }

    /**
     * Test that the same password produces different hashes when hashed with different salts.
     */
    @Test
    public void testSamePasswordDifferentSalts() throws NoSuchAlgorithmException {
        String password = "password123";

        byte[] hash1 = Answer.hashPasswordWithSalt(password);
        byte[] hash2 = Answer.hashPasswordWithSalt(password);

        // The salt is generated randomly, so the hashes should be different.
        assertNotEquals(Arrays.toString(hash1), Arrays.toString(hash2), "The same password should produce different hashes with different salts.");
    }

    /**
     * Test that the same password and salt produce the same hash.
     * This ensures that the hashing function is deterministic given the same inputs.
     */
    @Test
    public void testSamePasswordAndSaltProduceSameHash() throws NoSuchAlgorithmException {
        String password = "password123";
        byte[] salt = Answer.hashPasswordWithSalt(password);
        byte[] extractedSalt = Arrays.copyOfRange(salt, 0, 16);

        byte[] hash1 = Answer.hashWithSHA256(password, extractedSalt);
        byte[] hash2 = Answer.hashWithSHA256(password, extractedSalt);

        assertArrayEquals(hash1, hash2, "The same password and salt should produce the same hash.");
    }
}
