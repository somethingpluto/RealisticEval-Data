package org.real.temp;

public class Answer {

    /**
     * Compresses multiple consecutive whitespace characters in a string into a single space.
     *
     * @param inputString The string to be processed.
     * @return The processed string with compressed whitespace.
     */
    public static String compressWhitespace(String inputString) {
        // Split the input string by whitespace and join with a single space
        return String.join(" ", inputString.split("\\s+"));
    }

    // A simple check function to test the method
    public static void main(String[] args) {
        String testString = "This   is  a    test";
        System.out.println(compressWhitespace(testString));
    }
}