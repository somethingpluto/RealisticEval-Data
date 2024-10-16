package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class Tester {

    @Test
    public void testValidCamelCaseString() {
        assertTrue(isCamelCase("camelCase"));
    }

    @Test
    public void testValidCamelCaseStringWithMultipleWords() {
        assertTrue(isCamelCase("camelCaseExample"));
    }

    @Test
    public void testStringStartingWithUppercaseLetter() {
        assertFalse(isCamelCase("CamelCase"));
    }

    @Test
    public void testStringWithUnderscores() {
        assertFalse(isCamelCase("camel_case"));
    }

    @Test
    public void testEmptyString() {
        assertFalse(isCamelCase(""));
    }
}