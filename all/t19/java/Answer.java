package org.real.temp;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Answer {

    /**
     * Determines whether the string contains a phone number; a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
     *
     * @param s the input string to check
     * @return true if the string contains a phone number, false otherwise
     */
    public static boolean containsPhoneNumber(String s) {
        // Regex pattern to identify phone numbers
        String pattern = "(\\+\\d{1,3}[- ]?)?(\\d{3}[- ]\\d{3}[- ]\\d{4})";
        
        // Compile the regex pattern
        Pattern compiledPattern = Pattern.compile(pattern);
        
        // Create a matcher for the input string
        Matcher matcher = compiledPattern.matcher(s);
        
        // Check if the matcher finds a match
        return matcher.find();
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(containsPhoneNumber("+1-800-555-1234")); // true
        System.out.println(containsPhoneNumber("555-555-1234")); // true
        System.out.println(containsPhoneNumber("555 555 1234")); // true
        System.out.println(containsPhoneNumber("No phone number here")); // false
    }
}