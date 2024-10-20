package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class Tester {

    /**
     * Tests conversion of an integer string.
     */
    @Test
    public void testConvertInteger() {
        assertEquals("Should convert to integer", 123, numericalStrConvert("123"));
    }

    /**
     * Tests conversion of a float string.
     */
    @Test
    public void testConvertFloat() {
        assertEquals("Should convert to float", 123.45f, (Float) numericalStrConvert("123.45"), 0.001f);
    }

    /**
     * Tests conversion of a non-numeric string.
     */
    @Test
    public void testConvertNonNumericString() {
        assertEquals("Should remain a string", "abc", numericalStrConvert("abc"));
    }

    /**
     * Tests conversion of a negative integer string.
     */
    @Test
    public void testConvertNegativeInteger() {
        assertEquals("Should convert to negative integer", -456, numericalStrConvert("-456"));
    }

    /**
     * Tests conversion of a negative float string.
     */
    @Test
    public void testConvertNegativeFloat() {
        assertEquals("Should convert to negative float", -456.78f, (Float) numericalStrConvert("-456.78"), 0.001f);
    }
}