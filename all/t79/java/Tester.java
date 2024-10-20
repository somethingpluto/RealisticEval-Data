package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import java.text.ParseException;

import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testSameMonth() throws ParseException {
        // Test dates within the same month
        String result = dateRangeString("2023-08-01", "2023-08-15");
        assertEquals("August 1 to 15, 2023", result);
    }

    @Test
    public void testSameMonthStartToEnd() throws ParseException {
        // Test dates within the same month
        String result = dateRangeString("2023-08-01", "2023-08-31");
        assertEquals("August 1 to 31, 2023", result);
    }

    @Test
    public void testDifferentMonthsSameYear() throws ParseException {
        // Test dates across different months within the same year
        String result = dateRangeString("2023-08-30", "2023-09-05");
        assertEquals("August 30, 2023 to September 5, 2023", result);
    }

    @Test
    public void testDifferentYears() throws ParseException {
        // Test dates across different years
        String result = dateRangeString("2023-12-30", "2024-01-02");
        assertEquals("December 30, 2023 to January 2, 2024", result);
    }
}