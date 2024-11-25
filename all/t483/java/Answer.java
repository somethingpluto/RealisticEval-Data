package org.real.temp;

import java.util.regex.Pattern;

public class Answer {

    /**
     * Verifies if the provided string is a valid email address.
     *
     * @param email The email address to validate.
     * @return true if the email address is valid, false otherwise.
     */
    public static boolean isValidEmail(String email) {
        // Regular expression pattern for validating an email address
        String emailPattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        Pattern pattern = Pattern.compile(emailPattern);

        // Check if the email matches the pattern
        return pattern.matcher(email).matches();
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(isValidEmail("example@example.com")); // true
        System.out.println(isValidEmail("invalid-email")); // false
    }
}