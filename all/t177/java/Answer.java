package org.real.temp;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Arrays;

public class Answer {
    /**
     * Generates a 16-byte random salt value, hashes the provided password with that salt
     * using the SHA-256 hash algorithm, and returns the combined salt and hashed password.
     *
     * @param password The password to be hashed.
     * @return A byte array containing the salt followed by the hashed password.
     * @throws NoSuchAlgorithmException If the SHA-256 algorithm is not available.
     */
    public static byte[] hashPasswordWithSalt(String password) throws NoSuchAlgorithmException {
        // Generate a 16-byte random salt
        byte[] salt = generateRandomSalt(16);

        // Hash the password with the salt using SHA-256
        byte[] hashedPassword = hashWithSHA256(password, salt);

        // Combine the salt and the hashed password
        byte[] saltAndHashedPassword = new byte[salt.length + hashedPassword.length];
        System.arraycopy(salt, 0, saltAndHashedPassword, 0, salt.length);
        System.arraycopy(hashedPassword, 0, saltAndHashedPassword, salt.length, hashedPassword.length);

        return saltAndHashedPassword;
    }

    /**
     * Generates a random salt of the specified length.
     *
     * @param length The length of the salt in bytes.
     * @return A byte array containing the generated salt.
     */
    private static byte[] generateRandomSalt(int length) {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[length];
        random.nextBytes(salt);
        return salt;
    }

    /**
     * Hashes the provided password with the given salt using the SHA-256 hash algorithm.
     *
     * @param password The password to be hashed.
     * @param salt     The salt to be used in the hashing process.
     * @return A byte array containing the hashed password.
     * @throws NoSuchAlgorithmException If the SHA-256 algorithm is not available.
     */
    static byte[] hashWithSHA256(String password, byte[] salt) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        digest.update(salt);
        byte[] hashedPassword = digest.digest(password.getBytes());
        return hashedPassword;
    }

    /**
     * Main method for testing the hashPasswordWithSalt function.
     */
    public static void main(String[] args) {
        try {
            String password = "examplePassword123";
            byte[] saltAndHashedPassword = hashPasswordWithSalt(password);
            System.out.println("Salt and Hashed Password: " + Arrays.toString(saltAndHashedPassword));
        } catch (NoSuchAlgorithmException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
