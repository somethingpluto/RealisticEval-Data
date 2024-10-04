package org.real.temp;

import java.util.regex.Pattern;

public class Answer {

    // Regular expression for validating an email address
    private static final String EMAIL_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
    private static final Pattern EMAIL_PATTERN = Pattern.compile(EMAIL_REGEX);

    /**
     * Checks whether the given string is a valid email address.
     *
     * @param email the string to be checked
     * @return true if the string is a valid email address, false otherwise
     */
    public static boolean isValidEmail(String email) {
        if (email == null) {
            return false; // null is not a valid email
        }
        return EMAIL_PATTERN.matcher(email).matches();
    }

    // Example usage
    public static void main(String[] args) {
        // Test the email validation function
        String email1 = "example@test.com";
        String email2 = "invalid-email@.com";

        System.out.println(email1 + " is valid: " + isValidEmail(email1)); // Should return true
        System.out.println(email2 + " is valid: " + isValidEmail(email2)); // Should return false
    }
}