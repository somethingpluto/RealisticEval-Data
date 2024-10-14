package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testValidSignificantNumberWithFiveDigits() {
        assertTrue(Signer.isSignificantNumber("12345"));
    }

    @Test
    public void testLeadingZero() {
        assertFalse(Signer.isSignificantNumber("01234"));
    }

    @Test
    public void testValidSignificantNumberWithEighteenDigits() {
        assertTrue(Signer.isSignificantNumber("123456789012345678"));
    }

    @Test
    public void testLessThanFiveDigits() {
        assertFalse(Signer.isSignificantNumber("123"));
    }

    @Test
    public void testMoreThanEighteenDigits() {
        assertFalse(Signer.isSignificantNumber("1234567890123456789"));
    }

    @Test
    public void testNonDigitCharacters() {
        assertFalse(Signer.isSignificantNumber("1234a"));
    }

    @Test
    public void testSingleZero() {
        assertFalse(Signer.isSignificantNumber("0"));
    }

    @Test
    public void testNonStringInput() {
        assertFalse(Signer.isSignificantNumber(String.valueOf(12345)));
    }
}