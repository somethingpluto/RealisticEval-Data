package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testGetDaysInMonthRegularMonths() {
        assertEquals(31, getDaysInMonth(2023, 1)); // January
        assertEquals(31, getDaysInMonth(2023, 3)); // March
        assertEquals(30, getDaysInMonth(2023, 4)); // April
        assertEquals(31, getDaysInMonth(2023, 5)); // May
        assertEquals(30, getDaysInMonth(2023, 6)); // June
        assertEquals(31, getDaysInMonth(2023, 7)); // July
        assertEquals(31, getDaysInMonth(2023, 8)); // August
        assertEquals(30, getDaysInMonth(2023, 9)); // September
        assertEquals(31, getDaysInMonth(2023, 10)); // October
        assertEquals(30, getDaysInMonth(2023, 11)); // November
        assertEquals(31, getDaysInMonth(2023, 12)); // December
    }

    @Test
    public void testGetDaysInMonthFebruaryLeapYear() {
        assertEquals(29, getDaysInMonth(2024, 2)); // Leap year
    }

    @Test
    public void testGetDaysInMonthFebruaryNonLeapYear() {
        assertEquals(28, getDaysInMonth(2023, 2)); // Non-leap year
    }
}