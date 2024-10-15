package org.real.temp;

import java.util.Random;

public class Answer {
    /**
     * Shuffles the characters in a given string randomly.
     *
     * @param inputString The string to shuffle.
     * @return A new string with the characters shuffled.
     */
    public static String shuffleString(String inputString) {
        char[] charArray = inputString.toCharArray();
        int length = charArray.length;
        Random random = new Random();

        for (int i = length - 1; i > 0; i--) {
            int randomIndex = random.nextInt(i + 1);
            // Swap the current character with the character at the random index
            char temp = charArray[i];
            charArray[i] = charArray[randomIndex];
            charArray[randomIndex] = temp;
        }

        return new String(charArray);
    }
}