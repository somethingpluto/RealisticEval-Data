package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testGenerateUUIDShouldReturnAString() {
        String result = generateUUID();
        assertTrue(result instanceof String);
    }

    @Test
    public void testGenerateUUIDShouldReturnStringOfLength36() {
        String result = generateUUID();
        assertEquals(36, result.length());
    }

    @Test
    public void testGenerateUUIDShouldGenerateDifferentUUIDsOnConsecutiveCalls() {
        String uuid1 = generateUUID();
        String uuid2 = generateUUID();
        assertNotEquals(uuid1, uuid2);
    }

    @Test
    public void testGenerateUUIDShouldIncludeUppercase() {
        String result = generateUUID();
        assertTrue(result.matches(".*[A-Z].*")); // At least one uppercase letter
    }

    @Test
    public void testGenerateUUIDShouldIncludeLowercase() {
        String result = generateUUID();
        assertTrue(result.matches(".*[a-z].*")); // At least one lowercase letter
    }

    @Test
    public void testGenerateUUIDShouldIncludeDigits() {
        String result = generateUUID();
        assertTrue(result.matches(".*[0-9].*")); // At least one digit
    }
}