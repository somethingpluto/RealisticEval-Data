package org.real.temp;
public class Answer {
    public static boolean isSignificantNumber(String input) {
        // Check if input is null or empty
        if (input == null || input.trim().isEmpty()) {
            return false;
        }

        // Trim whitespace from the input
        input = input.trim();

        // Check the length
        int length = input.length();
        if (length < 5 || length > 18) {
            return false;
        }

        // Check for significant number: all characters must be digits
        // and cannot start with '0' if the length is greater than 1
        if (!input.matches("\\d+") || (length > 1 && input.charAt(0) == '0')) {
            return false;
        }

        return true;
    }
}