package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Tests a basic case where the minimum window exists.
     */
    @Test
    public void testBasicCase() {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        String expectedOutput = "BANC";
        assertEquals(expectedOutput, minWindow(s, t));
    }

    /**
     * Tests a case where no window can satisfy the condition.
     */
    @Test
    public void testNoWindowExists() {
        String s = "A";
        String t = "AA";
        String expectedOutput = "";
        assertEquals(expectedOutput, minWindow(s, t));
    }

    /**
     * Tests a case with an empty input string s.
     */
    @Test
    public void testEmptyString() {
        String s = "";
        String t = "ABC";
        String expectedOutput = "";
        assertEquals(expectedOutput, minWindow(s, t));
    }

    /**
     * Tests a case with multiple valid windows to ensure the smallest one is returned.
     */
    @Test
    public void testMultipleValidWindows() {
        String s = "AA";
        String t = "AA";
        String expectedOutput = "AA";
        assertEquals(expectedOutput, minWindow(s, t));
    }
}