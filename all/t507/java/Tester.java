package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

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

    // Utility method to check if a password is strong
    private boolean isStrongPassword(String password) {
        // Check password length
        if (password.length() < 8) {
            return false;
        }

        // Check for at least one lowercase letter
        if (!password.matches(".*[a-z].*")) {
            return false;
        }

        // Check for at least one uppercase letter
        if (!password.matches(".*[A-Z].*")) {
            return false;
        }

        // Check for at least one number
        if (!password.matches(".*\\d.*")) {
            return false;
        }

        // If all checks passed, return true
        return true;
    }
}