package org.real.temp;

import java.security.SecureRandom;

public class Answer {
    public static void main(String[] args) {
        System.out.println(generateUUID());
    }

    /**
     * Generate a random UUID of length 36
     * The UUID includes at least one uppercase letter, one lowercase letter, and one digit.
     *
     * @returns A 36-character UUID string.
     */
    public static String generateUUID() {
        // Define the characters that can appear in the UUID
        String possibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        SecureRandom random = new SecureRandom();
        StringBuilder uuid = new StringBuilder(36);

        // Generate characters for the UUID
        while (uuid.length() < 36) {
            int index = random.nextInt(possibleChars.length());
            uuid.append(possibleChars.charAt(index));
        }

        // Ensure at least one uppercase letter, one lowercase letter, and one digit
        if (!uuid.toString().matches(".*[A-Z].*") ||
            !uuid.toString().matches(".*[a-z].*") ||
            !uuid.toString().matches(".*[0-9].*")) {
            return generateUUID(); // Retry if the conditions are not met
        }

        // Return the generated UUID
        return uuid.toString();
    }
}