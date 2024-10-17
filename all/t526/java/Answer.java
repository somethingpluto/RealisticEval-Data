package org.real.temp;

import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Finds the minimum window substring in `s` that contains all characters of `t`.
     *
     * @param s The input string in which to search for the substring.
     * @param t The target string whose characters must be included in the substring.
     * @return The minimum window substring of `s` that contains all characters of `t`.
     *         Returns an empty string if no such substring exists.
     */
    public static String minWindow(String s, String t) {
        // If the length of s is less than t, return an empty string
        if (s.length() < t.length()) {
            return "";
        }

        // Count characters in t
        Map<Character, Integer> substringCounter = new HashMap<>();
        for (char c : t.toCharArray()) {
            substringCounter.put(c, substringCounter.getOrDefault(c, 0) + 1);
        }

        // Counter for the current window
        Map<Character, Integer> counter = new HashMap<>();

        // Initialize pointers and variables for the minimum window
        int l = 0, r = 0;
        int minLength = Integer.MAX_VALUE;
        String minString = "";

        // Iterate over s using the right pointer
        while (r < s.length()) {
            char charAtR = s.charAt(r);

            // If the character is in the substringCounter, update the current counter
            if (substringCounter.containsKey(charAtR)) {
                counter.put(charAtR, counter.getOrDefault(charAtR, 0) + 1);
            }

            // Check if the current window contains all characters in t
            while (isCurrentWindowValid(counter, substringCounter)) {
                // Update the minimum window if a smaller one is found
                if (r - l + 1 < minLength) {
                    minLength = r - l + 1;
                    minString = s.substring(l, r + 1);
                }

                // Move the left pointer to try to shrink the window
                char leftChar = s.charAt(l);
                if (substringCounter.containsKey(leftChar)) {
                    counter.put(leftChar, counter.get(leftChar) - 1);
                }
                l++;
            }

            r++;
        }

        // Return the minimum window found or an empty string if none exists
        return minString;
    }

    private static boolean isCurrentWindowValid(Map<Character, Integer> counter, Map<Character, Integer> substringCounter) {
        for (Map.Entry<Character, Integer> entry : substringCounter.entrySet()) {
            if (counter.getOrDefault(entry.getKey(), 0) < entry.getValue()) {
                return false;
            }
        }
        return true;
    }

    // Example usage
    public static void main(String[] args) {
        System.out.println(minWindow("ADOBECODEBANC", "ABC")); // Output: "BANC"
    }
}