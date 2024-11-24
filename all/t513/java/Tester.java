package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
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
