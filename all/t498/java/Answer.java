package org.real.temp;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Answer {

    /**
     * Computes and returns the MD5 hash of the input string.
     *
     * @param inputString The string to be hashed
     * @return The MD5 hash of the input string in hexadecimal format
     */
    public static String computeMD5(String inputString) {
        try {
            // Create an MD5 MessageDigest instance
            MessageDigest md = MessageDigest.getInstance("MD5");

            // Update the digest using the specified array of bytes
            md.update(inputString.getBytes());

            // Complete the hash computation
            byte[] digest = md.digest();

            // Convert the byte array to a hex string
            StringBuilder hexString = new StringBuilder();
            for (byte b : digest) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }

            // Return the hexadecimal representation of the hash
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("MD5 algorithm not found", e);
        }
    }

    // Example usage
    public static void main(String[] args) {
        String input = "Hello, World!";
        System.out.println("MD5 hash of '" + input + "': " + computeMD5(input));
    }
}