package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Test case for a valid 3-digit number with the ".bit" suffix.
     * Expected to return true.
     */
    @Test
    public void testValidThreeDigitNumber() {
        String input = "123.bit";
        boolean result = assert999(input);
        assertTrue(result);
    }

    /**
     * Test case for a valid 2-digit number with the ".bit" suffix.
     * Expected to return true.
     */
    @Test
    public void testValidTwoDigitNumber() {
        String input = "12.bit";
        boolean result = assert999(input);
        assertTrue(result);
    }

    /**
     * Test case for a string containing non-numeric characters after removing ".bit".
     * Expected to return false.
     */
    @Test
    public void testNonNumericCharacters() {
        String input = "12a.bit";
        boolean result = assert999(input);
        assertFalse(result);
    }

    /**
     * Test case for the lower boundary value "0.bit".
     * Expected to return true.
     */
    @Test
    public void testLowerBoundaryValue() {
        String input = "0.bit";
        boolean result = assert999(input);
        assertTrue(result);
    }

    /**
     * Test case for the upper boundary value "999.bit".
     * Expected to return true.
     */
    @Test
    public void testUpperBoundaryValue() {
        String input = "999.bit";
        boolean result = assert999(input);
        assertTrue(result);
    }
}