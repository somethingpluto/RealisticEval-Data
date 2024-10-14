package org.real.temp;

import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Finds the smallest window in the source string that contains all characters of the target string.
     *
     * @param source The source string in which to search for the window.
     * @param target The target string containing the characters to be matched.
     * @return The smallest window in the source string that contains all characters of the target string.
     *         Returns an empty string if no such window exists.
     */
    public static String findMinWindowSubstring(String source, String target) {
        if (source == null || target == null || source.isEmpty() || target.isEmpty()) {
            return "";
        }

        Map<Character, Integer> requiredChars = new HashMap<>();
        for (char c : target.toCharArray()) {
            requiredChars.put(c, requiredChars.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> windowChars = new HashMap<>();

        int left = 0; // Left boundary of the window
        int minLength = Integer.MAX_VALUE; // Initialize the minimum length as infinity
        String minWindow = ""; // Initialize the minimum window string

        // Iterate over the source string with the right boundary of the window
        for (int right = 0; right < source.length(); right++) {
            char charAtRight = source.charAt(right);
            if (requiredChars.containsKey(charAtRight)) {
                windowChars.put(charAtRight, windowChars.getOrDefault(charAtRight, 0) + 1);

                // Check if the current window contains all characters of the target string
                while (isWindowValid(requiredChars, windowChars)) {
                    int windowSize = right - left + 1;
                    if (windowSize < minLength) {
                        minLength = windowSize;
                        minWindow = source.substring(left, right + 1);
                    }

                    // Attempt to shrink the window from the left
                    char leftChar = source.charAt(left);
                    if (requiredChars.containsKey(leftChar)) {
                        windowChars.put(leftChar, windowChars.get(leftChar) - 1);
                    }
                    left++;
                }
            }
        }

        return minWindow;
    }

    private static boolean isWindowValid(Map<Character, Integer> requiredChars, Map<Character, Integer> windowChars) {
        for (Map.Entry<Character, Integer> entry : requiredChars.entrySet()) {
            char key = entry.getKey();
            int value = entry.getValue();
            if (windowChars.getOrDefault(key, 0) < value) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // Example usage
        String source = "ADOBECODEBANC";
        String target = "ABC";
        System.out.println(findMinWindowSubstring(source, target));
    }
}