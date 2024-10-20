package org.real.temp;

import java.time.LocalDate;
import java.time.DayOfWeek;
import java.util.HashMap;
import java.util.Map;
import org.junit.Test; // JUnit 4 Test annotation
import static org.junit.Assert.assertEquals; // JUnit 4 assertion methods

public class Tester {


    @Test
    public void testBeginningOfMonth() {
        LocalDate testDate = LocalDate.of(2023, 1, 1);
        Map<String, Object> result = Answer.getCurrentDateInfo(testDate);
        Map<String, Object> expected = new HashMap<>();
        expected.put("year", 2023);
        expected.put("month", "January".toUpperCase());
        expected.put("week_of_the_month", 1);
        expected.put("day_of_the_week", "SUNDAY");
        assertEquals(expected, result);
    }

    @Test
    public void testMiddleOfMonth() {
        LocalDate testDate = LocalDate.of(2023, 1, 15);
        Map<String, Object> result = Answer.getCurrentDateInfo(testDate);
        Map<String, Object> expected = new HashMap<>();
        expected.put("year", 2023);
        expected.put("month", "January".toUpperCase());
        expected.put("week_of_the_month", 3);
        expected.put("day_of_the_week", "SUNDAY");
        assertEquals(expected, result);
    }

    @Test
    public void testLeapYear() {
        LocalDate testDate = LocalDate.of(2024, 2, 29);
        Map<String, Object> result = Answer.getCurrentDateInfo(testDate);
        Map<String, Object> expected = new HashMap<>();
        expected.put("year", 2024);
        expected.put("month", "FEBRUARY");
        expected.put("week_of_the_month", 5);
        expected.put("day_of_the_week", "THURSDAY");
        assertEquals(expected, result);
    }

    @Test
    public void testChangeOfYear() {
        LocalDate testDate = LocalDate.of(2022, 12, 31);
        Map<String, Object> result = Answer.getCurrentDateInfo(testDate);
        Map<String, Object> expected = new HashMap<>();
        expected.put("year", 2022);
        expected.put("month", "DECEMBER");
        expected.put("week_of_the_month", 5);
        expected.put("day_of_the_week", "SATURDAY");
        assertEquals(expected, result);
    }
}
