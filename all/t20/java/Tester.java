package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testBasicCase() {
        String text = "Hello (*wo*rld*)!";
        String expected = "Hello (*world*)!";
        assertEquals(expected, removeInnerAsterisks(text));
    }

    @Test
    public void testMultipleAsterisks() {
        String text = "(*he*l*lo*)";
        String expected = "(*hello*)";
        assertEquals(expected, removeInnerAsterisks(text));
    }

    @Test
    public void testNoAsterisksInside() {
        String text = "(*hello*)";
        String expected = "(*hello*)";
        assertEquals(expected, removeInnerAsterisks(text));
    }

    @Test
    public void testMultiplePatterns() {
        String text = "(*hi*), (*there*), (*world*)!";
        String expected = "(*hi*), (*there*), (*world*)!";
        assertEquals(expected, removeInnerAsterisks(text));
    }

    @Test
    public void testNoMatchingPattern() {
        String text = "This is a test without matching parentheses.";
        String expected = "This is a test without matching parentheses.";
        assertEquals(expected, removeInnerAsterisks(text));
    }
}
