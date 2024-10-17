package org.real.temp;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Class to check if a given text contains an email address.
 */
public class Answer {

    /**
     * Checks if the given text contains an email address.
     *
     * @param text The string to search for an email address.
     * @return true if an email address is found, false otherwise.
     */
    public static boolean containsEmail(String text) {
        // Define a regex pattern for validating an email address
        String emailPattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}";

        // Compile the regex pattern
        Pattern pattern = Pattern.compile(emailPattern);

        // Create a matcher for the input text
        Matcher matcher = pattern.matcher(text);

        // Search for the email pattern in the text
        return matcher.find();
    }

    // A simple check function to verify the correctness of the method
    public static void main(String[] args) {
        System.out.println(containsEmail("Hello, my email is example@example.com")); // Expected: true
        System.out.println(containsEmail("No email here")); // Expected: false
    }
}