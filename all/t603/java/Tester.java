package org.real.temp;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;

public class Tester {

    @Test
    public void testLeapYearDivisibleBy4NotBy100() {
        // Years that are leap years
        assertTrue(isLeapYear(2024)); // 2024 is a leap year
        assertTrue(isLeapYear(2000)); // 2000 is a leap year (divisible by 400)
        assertTrue(isLeapYear(1996)); // 1996 is a leap year
        assertTrue(isLeapYear(2004)); // 2004 is a leap year
    }

    @Test
    public void testLeapYearDivisibleBy100NotBy400() {
        // Years that are not leap years
        assertFalse(isLeapYear(1900)); // 1900 is not a leap year
        assertFalse(isLeapYear(2100)); // 2100 is not a leap year
        assertFalse(isLeapYear(1800)); // 1800 is not a leap year
    }

    @Test
    public void testLeapYearDivisibleBy400() {
        // Years that are leap years
        assertTrue(isLeapYear(2400)); // 2400 is a leap year
        assertTrue(isLeapYear(1600)); // 1600 is a leap year
    }

    @Test
    public void testNormalYears() {
        // Years that are normal years
        assertFalse(isLeapYear(1997)); // 1997 is not a leap year
        assertFalse(isLeapYear(1998)); // 1998 is not a leap year
        assertFalse(isLeapYear(1999)); // 1999 is not a leap year
    }
}