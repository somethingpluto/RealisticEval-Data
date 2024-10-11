package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class Tester {
    @Test
    public void testNumericalStrConvert() {
        assertEquals(42, numericalStrConvert("42"));
        assertEquals(3.14, numericalStrConvert("3.14"));
        assertEquals("hello", numericalStrConvert("hello"));
        assertEquals(0, numericalStrConvert("0"));
        assertEquals(-5, numericalStrConvert("-5"));
        assertEquals(-2.71, numericalStrConvert("-2.71"));
        assertEquals("123abc", numericalStrConvert("123abc"));
    }
}