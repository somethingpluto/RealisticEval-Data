package org.real.temp;

import java.time.LocalDate;
import java.time.Month;
import java.time.DayOfWeek;
import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Returns the current time information including year, month, week of the month, and day of the week.
     *
     * @param testDate The date to compute information for, defaults to today's date if not provided.
     * @return A map containing the year, month, week of the month, and day of the week.
     */
    public static Map<String, Object> getCurrentDateInfo(LocalDate testDate) {
        if (testDate == null) {
            testDate = LocalDate.now();
        }
        
        int year = testDate.getYear();
        Month month = testDate.getMonth();
        int dayOfMonth = testDate.getDayOfMonth();
        DayOfWeek dayOfWeek = testDate.getDayOfWeek();
        int weekOfMonth = testDate.get(java.time.temporal.WeekFields.of(Locale.getDefault()).weekOfMonth());

        Map<String, Object> result = new HashMap<>();
        result.put("year", year);
        result.put("month", month.toString());
        result.put("week_of_the_month", weekOfMonth);
        result.put("day_of_the_week", dayOfWeek.toString());

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        LocalDate testDate = LocalDate.of(2024, 2, 1); // February 1, 2024
        Map<String, Object> dateInfo = getCurrentDateInfo(testDate);
        System.out.println(dateInfo);
    }
}