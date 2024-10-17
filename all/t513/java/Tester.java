package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test class for verifying the functionality of the isPhraseInStringIgnoreCase method.
 */
public class Tester {

    /**
     * Tests that an exact match is found when ignoring case.
     */
    @Test
    public void testExactMatchCaseInsensitive() {
        assertTrue(isPhraseInStringIgnoreCase("hello world", "Hello World"));
    }

    /**
     * Tests that a partial word match is found when ignoring case.
     */
    @Test
    public void testPartialWordMatchCaseInsensitive() {
        assertTrue(isPhraseInStringIgnoreCase("Hello", "saying Hello there"));
    }

    /**
     * Tests different cases where the phrase is present but with varying capitalization.
     */
    @Test
    public void testDifferentCases() {
        assertTrue(isPhraseInStringIgnoreCase("HELLO", "hello there!"));
        assertTrue(isPhraseInStringIgnoreCase("world", "WORLD is great"));
    }

    /**
     * Tests cases where the phrase does not exist in the string.
     */
    @Test
    public void testNonExistentPhrase() {
        assertFalse(isPhraseInStringIgnoreCase("goodbye", "Hello world"));
        assertFalse(isPhraseInStringIgnoreCase("hello", "goodbye world"));
    }
}

// The isPhraseInStringIgnoreCase method remains the same as before
public class Answer {

    /**
     * Checks if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.
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