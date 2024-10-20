package org.real.temp;

import org.junit.Test; // Import JUnit 4 Test annotation
import static org.junit.Assert.assertEquals; // Import assertEquals from JUnit 4 assertions
import org.real.temp.Answer;
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
        assertEquals(expected, Answer.replacePhoneNumbers(msg));
    }

    /**
     * Tests replacing a phone number with spaces.
     */
    @Test
    public void testNumberWithSpaces() {
        String msg = "Our office number is 123 456-7890.";
        String expected = "Our office number is [PHONE_NUM].";
        assertEquals(expected, Answer.replacePhoneNumbers(msg));
    }

    /**
     * Tests replacing a phone number with dots.
     */
    @Test
    public void testNumberWithDots() {
        String msg = "Fax us at 123.456.7890.";
        String expected = "Fax us at [PHONE_NUM].";
        assertEquals(expected, Answer.replacePhoneNumbers(msg));
    }

    /**
     * Tests a message without a phone number.
     */
    @Test
    public void testNoPhoneNumber() {
        String msg = "Hello, please reply to this email.";
        String expected = "Hello, please reply to this email.";
        assertEquals(expected, Answer.replacePhoneNumbers(msg));
    }
}
