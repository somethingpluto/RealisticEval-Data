package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testValidSignificantNumberWithFiveDigits() {
        assertTrue(isSignificantNumber("12345"));
    }

    @Test
    public void testLeadingZero() {
        assertFalse(isSignificantNumber("01234"));
    }

    @Test
    public void testValidSignificantNumberWithEighteenDigits() {
        assertTrue(isSignificantNumber("123456789012345678"));
    }

    @Test
    public void testLessThanFiveDigits() {
        assertFalse(isSignificantNumber("123"));
    }

    @Test
    public void testMoreThanEighteenDigits() {
        assertFalse(isSignificantNumber("1234567890123456789"));
    }

    @Test
    public void testNonDigitCharacters() {
        assertFalse(isSignificantNumber("1234a"));
    }

    @Test
    public void testSingleZero() {
        assertFalse(isSignificantNumber("0"));
    }

    @Test
    public void testNonStringInput() {
        assertFalse(isSignificantNumber(String.valueOf(12345)));
    }
}