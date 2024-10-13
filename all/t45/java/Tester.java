package org.real.temp;

import java.time.LocalDate;
import java.time.DayOfWeek;
import java.util.Map;
import org.junit.jupiter.api.Test; // JUnit 5 Test annotation
import static org.junit.jupiter.api.Assertions.assertEquals; // JUnit 5 assertion methods

public class Tester {

    private static final Map<String, Object> getExpectedResult(LocalDate date) {
        int year = date.getYear();
        String month = date.getMonth().name();
        String dayOfWeek = date.getDayOfWeek().name();

        // Calculate the week of the month
        LocalDate firstDayOfMonth = date.withDayOfMonth(1);
        DayOfWeek firstDayWeekday = firstDayOfMonth.getDayOfWeek();
        int dayOfWeekInMonth = date.getDayOfMonth() + (firstDayWeekday.getValue() - 1);
        int weekOfMonth = (int) Math.ceil(dayOfWeekInMonth / 7.0);

        Map<String, Object> info = new HashMap<>();
        info.put("year", year);
        info.put("month", month);
        info.put("week_of_the_month", weekOfMonth);
        info.put("day_of_the_week", dayOfWeek);

        return info;
    }

    @Test
    public void testBeginningOfMonth() {
        LocalDate testDate = LocalDate.of(2023, 1, 1);
        Map<String, Object> result = getExpectedResult(testDate);
        Map<String, Object> expected = Map.of(
            "year", 2023,
            "month", "January",
            "week_of_the_month", 1,
            "day_of_the_week", "SUNDAY"
        );
        assertEquals(expected, result);
    }

    @Test
    public void testMiddleOfMonth() {
        LocalDate testDate = LocalDate.of(2023, 1, 15);
        Map<String, Object> result = getExpectedResult(testDate);
        Map<String, Object> expected = Map.of(
            "year", 2023,
            "month", "January",
            "week_of_the_month", 3,
            "day_of_the_week", "SUNDAY"
        );
        assertEquals(expected, result);
    }

    @Test
    public void testLeapYear() {
        LocalDate testDate = LocalDate.of(2024, 2, 29);
        Map<String, Object> result = getExpectedResult(testDate);
        Map<String, Object> expected = Map.of(
            "year", 2024,
            "month", "FEBRUARY",
            "week_of_the_month", 5,
            "day_of_the_week", "THURSDAY"
        );
        assertEquals(expected, result);
    }

    @Test
    public void testChangeOfYear() {
        LocalDate testDate = LocalDate.of(2022, 12, 31);
        Map<String, Object> result = getExpectedResult(testDate);
        Map<String, Object> expected = Map.of(
            "year", 2022,
            "month", "DECEMBER",
            "week_of_the_month", 5,
            "day_of_the_week", "SATURDAY"
        );
        assertEquals(expected, result);
    }
}