package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
/**
 * Test cases for the isCompliantFourDigit method.
 */
public class Tester {

    /**
     * Tests a standard positive four-digit number.
     */
    @Test
    public void testPositiveFourDigitNumber() {
        // Tests a standard positive four-digit number
        assertTrue("1234 should be a compliant four-digit number", isCompliantFourDigit(1234));
    }

    /**
     * Tests the boundary values of the range.
     */
    @Test
    public void testBoundaryValues() {
        // Tests the boundary values of the range
        assertTrue("1000 should be a compliant four-digit number", isCompliantFourDigit(1000));
        assertTrue("9999 should be a compliant four-digit number", isCompliantFourDigit(9999));
    }

    /**
     * Tests a negative four-digit number.
     */
    @Test
    public void testNegativeFourDigitNumber() {
        // Tests a negative four-digit number
        assertFalse("-1234 should not be a compliant four-digit number", isCompliantFourDigit(-1234));
    }

    /**
     * Tests numbers that are out of the four-digit range.
     */
    @Test
    public void testOutOfRangeNumber() {
        // Tests numbers that are out of the four-digit range
        assertFalse("999 should not be a compliant four-digit number", isCompliantFourDigit(999));
        assertFalse("10000 should not be a compliant four-digit number", isCompliantFourDigit(10000));
    }
}