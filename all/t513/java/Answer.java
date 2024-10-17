package org.real.temp;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Answer {

    /**
     * Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.
     *
     * @param phrase The phrase to search for in the string.
     * @param string The target string in which to search for the phrase.
     * @return True if the phrase is found as a whole word in the string, False otherwise.
     */
    public static boolean isPhraseInStringIgnoreCase(String phrase, String string) {
        // Convert both phrase and string to lower case
        phrase = phrase.toLowerCase();
        string = string.toLowerCase();

        // Escape special characters in the phrase
        String escapedPhrase = Pattern.quote(phrase);

        // Replace spaces in the phrase with \s+ to allow for any whitespace variations
        escapedPhrase = escapedPhrase.replace("\\ ", "\\s+");

        // Construct the regex pattern with word boundaries
        String pattern = "\\b" + escapedPhrase + "\\b";

        // Compile the pattern and create a matcher for the target string
        Pattern compiledPattern = Pattern.compile(pattern);
        Matcher matcher = compiledPattern.matcher(string);

        // Search for the pattern in the target string
        return matcher.find();
    }

    // Example usage
    public static void main(String[] args) {
        System.out.println(isPhraseInStringIgnoreCase("hello world", "Hello   World")); // true
        System.out.println(isPhraseInStringIgnoreCase("hello", "Hello World")); // false
    }
}