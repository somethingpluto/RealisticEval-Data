package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testNumericalStrConvert() {
        // Test cases for different types of inputs
        assertEquals(123, numericalStrConvert("123"));
        assertEquals(456.78, numericalStrConvert("456.78"));
        assertEquals("abc", numericalStrConvert("abc"));
        assertEquals(0, numericalStrConvert("0"));
        assertEquals(-123, numericalStrConvert("-123"));
        assertEquals(-456.78, numericalStrConvert("-456.78"));
        assertEquals("", numericalStrConvert(""));
        assertEquals(" ", numericalStrConvert(" "));
    }

    private Object numericalStrConvert(String value) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            try {
                return Double.parseDouble(value);
            } catch (NumberFormatException ex) {
                return value;
            }
        }
    }
}