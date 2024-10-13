package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    @Test
    public void testWithInternationalPrefix() {
        assertTrue(containsPhoneNumber("+1-800-555-1234"), "Should detect international prefix");
    }

    @Test
    public void testWithStandardDashes() {
        assertTrue(containsPhoneNumber("800-555-1234"), "Should detect standard format with dashes");
    }

    @Test
    public void testWithSpaces() {
        assertTrue(containsPhoneNumber("800 555 1234"), "Should detect standard format with spaces");
    }

    @Test
    public void testWithoutPhoneNumber() {
        assertFalse(containsPhoneNumber("Hello, world!"), "Should not detect any phone number");
    }

    @Test
    public void testWithTextContainingNumbers() {
        assertTrue(containsPhoneNumber("Call me at 800-555-1234 today!"), "Should detect phone number in text");
    }

    // Assuming this method exists as part of the class or is defined elsewhere
    private boolean containsPhoneNumber(String text) {
        // Placeholder for the actual implementation
        return text.matches(".*\\+?\\d{1,3}[-\\s]?\\d{3}[-\\s]?\\d{3}[-\\s]?\\d{4}.*");
    }
}
