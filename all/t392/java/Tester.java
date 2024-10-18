package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class Tester {

    /**
     * Tests the 'lookAndSay' method with a single digit.
     */
    @Test
    public void testSingleDigit() {
        // Test with a single digit to see if it replicates correctly
        assertEquals("11", lookAndSay("1"));
    }

    /**
     * Tests the 'lookAndSay' method with a sequence of the same digits.
     */
    @Test
    public void testRepetitiveDigits() {
        // Test a sequence of the same digits
        assertEquals("31", lookAndSay("111"));
    }

    /**
     * Tests the 'lookAndSay' method with a sequence containing different digits.
     */
    @Test
    public void testMixedDigits() {
        // Test a sequence with different digits
        assertEquals("111221", lookAndSay("1211"));
    }

    /**
     * Tests the 'lookAndSay' method with a more complex sequence.
     */
    @Test
    public void testComplexSequence() {
        // Test a more complex sequence
        assertEquals("13112221", lookAndSay("312211"));
    }
}