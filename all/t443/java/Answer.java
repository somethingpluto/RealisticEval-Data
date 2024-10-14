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

    // A simple check function to test the method with some sample data points.
    public static void main(String[] args) {
        System.out.println(compressWhitespace("This    is  a   test")); // Should print "This is a test"
        System.out.println(compressWhitespace("  Leading and trailing  ")); // Should print "Leading and trailing"
    }
}
