package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Counts the occurrences of consecutive identical letters in a given string.
     *
     * @param inputString The string to analyze for letter changes.
     * @returns A list of counts representing the number of consecutive
     *          identical letters before a different letter is found.
     */
    public static List<Integer> countLetterChanges(String inputString) {
        // List to hold counts of consecutive letters
        List<Integer> counts = new ArrayList<>();
        int currentCount = 1; // Initialize the count of the current letter

        // Iterate through the string starting from the second character
        for (int i = 1; i < inputString.length(); i++) {
            // If the current character is different from the previous one
            if (inputString.charAt(i) != inputString.charAt(i - 1)) {
                counts.add(currentCount); // Store the count of the previous letter
                currentCount = 1; // Reset count for the new letter
            } else {
                currentCount++; // Increment count for the current letter
            }
        }

        counts.add(currentCount); // Push the count of the last letter
        return counts;
    }

    public static void main(String[] args) {
        String input = "aaabbcddddee"; // Example input
        List<Integer> result = countLetterChanges(input);
        System.out.println(result); // Output the result
    }
}