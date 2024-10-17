package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test class for checking if a string contains an email address.
 */
public class Tester {

    /**
     * Test if a valid email is detected in the string.
     */
    @Test
    public void testContainsValidEmail() {
        String testString = "You can reach me at example@example.com for more info.";
        assertTrue(containsEmail(testString));
    }

    /**
     * Test if an email with special characters is detected.
     */
    @Test
    public void testContainsEmailWithSpecialCharacters() {
        String testString = "My email address is john.doe123+test@gmail.com!";
        assertTrue(containsEmail(testString));
    }

    /**
     * Test a string that does not contain any email address.
     */
    @Test
    public void testDoesNotContainEmail() {
        String testString = "This string does not have an email.";
        assertFalse(containsEmail(testString));
    }

    /**
     * Test a string containing multiple email addresses.
     */
    @Test
    public void testContainsMultipleEmails() {
        String testString = "You can contact me at example1@example.com or example2@example.com.";
        assertTrue(containsEmail(testString));
    }

    /**
     * Test a string with an invalid email format.
     */
    @Test
    public void testContainsInvalidEmailFormat() {
        String testString = "Please contact me at example@.com or test@domain.";
        assertFalse(containsEmail(testString));
    }
}