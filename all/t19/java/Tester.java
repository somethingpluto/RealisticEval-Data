package org.real.temp;
import org.junit.Test;  
import static org.junit.Assert.*; 
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testWithInternationalPrefix() {
        assertTrue("Should detect international prefix", containsPhoneNumber("+1-800-555-1234"));
    }

    @Test
    public void testWithStandardDashes() {
        assertTrue("Should detect standard format with dashes",containsPhoneNumber("800-555-1234"));
    }

    @Test
    public void testWithSpaces() {
        assertTrue("Should detect standard format with spaces",containsPhoneNumber("800 555 1234"));
    }

    @Test
    public void testWithoutPhoneNumber() {
        assertFalse("Should not detect any phone number",containsPhoneNumber("Hello, world!"));
    }

    @Test
    public void testWithTextContainingNumbers() {
        assertTrue("Should detect phone number in text", containsPhoneNumber("Call me at 800-555-1234 today!"));
    }
}
