package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;

public class Tester {
    @Test
    public void testContainsPhoneNumber() {
        assertTrue(containsPhoneNumber("+1-800-555-1234"));
        assertTrue(containsPhoneNumber("555-555-1234"));
        assertTrue(containsPhoneNumber("555 555 1234"));
        assertFalse(containsPhoneNumber("This is not a phone number"));
        assertFalse(containsPhoneNumber("1234567890"));
    }
}