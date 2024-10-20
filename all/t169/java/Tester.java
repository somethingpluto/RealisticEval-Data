package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testConvertToRomanTypicalNumber() {
        String result = convertToRoman(1987);
        assertEquals("MCMLXXXVII", result); // 1987 = M + CM + LXXX + VII
    }

    @Test
    public void testConvertToRomanMinimumValue() {
        String result = convertToRoman(1);
        assertEquals("I", result); // 1 = I
    }

    @Test
    public void testConvertToRomanLargeNumber() {
        String result = convertToRoman(3999);
        assertEquals("MMMCMXCIX", result); // 3999 = MMM + CM + XC + IX
    }

    @Test
    public void testConvertToRomanNumeralRepeats() {
        String result = convertToRoman(1666);
        assertEquals("MDCLXVI", result); // 1666 = M + D + CLX + VI
    }

    @Test
    public void testConvertToRomanNoFivesAndOnes() {
        String result = convertToRoman(2000);
        assertEquals("MM", result); // 2000 = MM
    }
}