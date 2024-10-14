package org.real.temp;
import java.util.regex.Pattern;

public class StringCleaner {
    /**
     * Removes all punctuation from a given string, converts the string to lowercase,
     * and trims whitespace from both ends.
     *
     * @param str The string from which to remove punctuation.
     * @return The cleaned and formatted string.
     */
    public static String removePunctuation(String str) {
        // Define a regex pattern that matches common punctuation characters.
        // This includes Unicode punctuation and ASCII punctuation.
        String punctuationRegex = "[\\u2000-\\u206F\\u2E00-\\u2E7F!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]+";
        
        return str.replaceAll(punctuationRegex, "").toLowerCase().trim();
    }

    public static void main(String[] args) {
        String testString = "Hello, World! This is a test.";
        String cleanedString = removePunctuation(testString);
        System.out.println(cleanedString); // Output: hello world this is a test
    }
}