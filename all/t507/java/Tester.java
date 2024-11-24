package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Test a strong password that meets all criteria.
     */
    @Test
    public void testValidPassword() {
        assertTrue(isStrongPassword("StrongPass1"));
    }

    /**
     * Test a password missing a lowercase letter.
     */
    @Test
    public void testMissingLowercase() {
        assertFalse(isStrongPassword("STRONGPASS1"));
    }

    /**
     * Test a password missing an uppercase letter.
     */
    @Test
    public void testMissingUppercase() {
        assertFalse(isStrongPassword("strongpass1"));
    }

    /**
     * Test a password missing a number.
     */
    @Test
    public void testMissingNumber() {
        assertFalse(isStrongPassword("StrongPassword"));
    }

    /**
     * Test a password that is too short.
     */
    @Test
    public void testTooShort() {
        assertFalse(isStrongPassword("Short1"));
    }

    /**
     * Test a password that includes special characters but is still strong.
     */
    @Test
    public void testValidWithSpecialCharacters() {
        assertTrue(isStrongPassword("Strong!Password1"));
    }
}