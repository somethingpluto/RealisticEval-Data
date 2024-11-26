package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the compressWhitespace method.
 */
public class Tester {

    /**
     * Tests the compressWhitespace method with a string containing single spaces.
     */
    @Test
    public void testSingleSpaces() {
        String input = "This is a test string.";
        String expected = "This is a test string.";
        assertEquals(expected, compressWhitespace(input));
    }

    /**
     * Tests the compressWhitespace method with a string containing multiple spaces.
     */
    @Test
    public void testMultipleSpaces() {
        String input = "This    is  a   test   string.";
        String expected = "This is a test string.";
        assertEquals(expected, compressWhitespace(input));
    }

    /**
     * Tests the compressWhitespace method with a string containing leading and trailing spaces.
     */
    @Test
    public void testLeadingTrailingSpaces() {
        String input = "Leading and trailing spaces   ";
        String expected = "Leading and trailing spaces";
        assertEquals(expected, compressWhitespace(input));
    }

    /**
     * Tests the compressWhitespace method with a string containing only spaces.
     */
    @Test
    public void testOnlySpaces() {
        String input = "       ";
        String expected = "";
        assertEquals(expected, compressWhitespace(input));
    }

    /**
     * Tests the compressWhitespace method with an empty string.
     */
    @Test
    public void testEmptyString() {
        String input = "";
        String expected = "";
        assertEquals(expected, compressWhitespace(input));
    }
}