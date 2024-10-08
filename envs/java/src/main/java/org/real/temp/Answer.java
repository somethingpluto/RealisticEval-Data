package org.real.temp;

import java.security.SecureRandom;

public class Answer {
    private static final String LOWER_CASE = "abcdefghijklmnopqrstuvwxyz";
    private static final String UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final int LENGTH = 25;

    /**
     * Generates a random string of length 25 and must contain both upper case letters (A-Z) and lower case letters (a-z)
     *
     * @return random string
     */
    public static String generateRandomString() {
        SecureRandom random = new SecureRandom();
        StringBuilder sb = new StringBuilder(LENGTH);

        // Ensure at least one upper case and one lower case letter
        sb.append(LOWER_CASE.charAt(random.nextInt(LOWER_CASE.length())));
        sb.append(UPPER_CASE.charAt(random.nextInt(UPPER_CASE.length())));

        // Fill the rest of the string length with random characters
        String allCharacters = LOWER_CASE + UPPER_CASE;
        for (int i = 2; i < LENGTH; i++) {
            int randomIndex = random.nextInt(allCharacters.length());
            char randomChar = allCharacters.charAt(randomIndex);
            sb.append(randomChar);
        }

        // Shuffle the characters to ensure randomness
        return shuffleString(sb.toString());
    }

    private static String shuffleString(String input) {
        char[] characters = input.toCharArray();
        SecureRandom random = new SecureRandom();
        for (int i = characters.length - 1; i > 0; i--) {
            int j = random.nextInt(i + 1);
            // Swap characters
            char temp = characters[i];
            characters[i] = characters[j];
            characters[j] = temp;
        }
        return new String(characters);
    }

    public static void main(String[] args) {
        // Test the random string generator
        String randomString = generateRandomString();
        System.out.println("Generated Random String: " + randomString);
    }
}
