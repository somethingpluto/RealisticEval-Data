package org.real.temp;

public class Answer {

    /**
     * Determines whether the string contains a phone number;
     * a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234.
     *
     * @param s The input string which may contain a phone number.
     * @return true if the string contains a phone number, false otherwise.
     */
    public static boolean containsPhoneNumber(String s) {
        // Regular expression to match the phone number formats
        String regex = "\\+?\\d{1,3}-?\\d{3}-?\\d{3}-?\\d{4}|\\d{3} \\d{3} \\d{4}";

        return s.matches(regex);
    }
}