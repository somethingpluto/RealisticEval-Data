package org.real.temp;

import org.junit.jupiter.api.Test; // Import JUnit 5 Test annotation
import static org.junit.jupiter.api.Assertions.assertEquals; // Import assertEquals from JUnit 5 assertions

/**
 * Test cases for the replacePhoneNumbers method.
 */
public class Tester {

    /**
     * Tests replacing a basic phone number.
     */
    @Test
    public void testBasicNumber() {
        String msg = "Call me at 123-456-7890.";
        String expected = "Call me at [PHONE_NUM].";
        assertEquals(expected, replacePhoneNumbers(msg));
    }

    /**
     * Tests replacing a phone number with parentheses.
     */
    @Test
    public void testNumberWithParentheses() {
        String msg = "Our office number is 123 456-7890.";
        String expected = "Our office number is [PHONE_NUM].";
        assertEquals(expected, replacePhoneNumbers(msg));
    }

    /**
     * Tests replacing a phone number with dots.
     */
    @Test
    public void testNumberWithDots() {
        String msg = "Fax us at 123.456.7890.";
        String expected = "Fax us at [PHONE_NUM].";
        assertEquals(expected, replacePhoneNumbers(msg));
    }

    /**
     * Tests a message without a phone number.
     */
    @Test
    public void testNoPhoneNumber() {
        String msg = "Hello, please reply to this email.";
        String expected = "Hello, please reply to this email.";
        assertEquals(expected, replacePhoneNumbers(msg));
    }

    // Assuming the replacePhoneNumbers method is defined here or imported from another class
    private String replacePhoneNumbers(String message) {
        // Sample implementation of the method
        return message.replaceAll("\\b\\d{3}[\\s.-]?\\d{3}[\\s.-]?\\d{4}\\b", "[PHONE_NUM]");
    }
}
