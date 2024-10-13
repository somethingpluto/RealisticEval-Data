package org.real.temp;

import java.time.LocalDate;
import java.time.DayOfWeek;
import java.util.Locale;
import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Returns the current time information including year, month, week of the month, and day of the week.
     * Optionally takes a date object for testing purposes.
     *
     * @param testDate The date to compute information for, defaults to today's date if not provided.
     * @return A map containing the year, month, week of the month, and day of the week.
     */
    public static Map<String, Object> getCurrentDateInfo(LocalDate testDate) {
        LocalDate today = (testDate == null) ? LocalDate.now() : testDate;

        int year = today.getYear();
        String month = today.getMonth().name();
        String dayOfWeek = today.getDayOfWeek().name();

        // Calculate the week of the month
        LocalDate firstDayOfMonth = today.withDayOfMonth(1);
        DayOfWeek firstDayWeekday = firstDayOfMonth.getDayOfWeek();
        int dayOfWeekInMonth = today.getDayOfMonth() + (firstDayWeekday.getValue() - 1);
        int weekOfMonth = (int) Math.ceil(dayOfWeekInMonth / 7.0);

        Map<String, Object> info = new HashMap<>();
        info.put("year", year);
        info.put("month", month);
        info.put("week_of_the_month", weekOfMonth);
        info.put("day_of_the_week", dayOfWeek);

        return info;
    }

    public static void main(String[] args) {
        Map<String, Object> dateInfo = getCurrentDateInfo(null);
        System.out.println(dateInfo);
    }
}