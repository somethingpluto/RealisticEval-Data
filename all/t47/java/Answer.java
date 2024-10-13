package org.real.temp;

import java.time.LocalDate;
import java.time.DayOfWeek;
import java.time.format.DateTimeFormatter;
import java.time.temporal.TemporalAdjusters;

public class Answer {

    /**
     * Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
     * If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
     * This function extends the capability to handle edge cases where the nth weekday might not be present,
     * by providing the closest previous weekday in such cases.
     *
     * @param y The year for which the date is to be calculated.
     * @param m The month for which the date is to be calculated, where January is 1 and December is 12.
     * @param n The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
     * @param k The weekday, where Monday is 0 and Sunday is 6.
     * @return LocalDate: The calculated date of the nth occurrence of the weekday in the given month and year.
     *         If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
     */
    public static LocalDate findNthWeekdayOfSpecificYear(int y, int m, int n, int k) {
        LocalDate firstDayOfMonth = LocalDate.of(y, m, 1);
        DayOfWeek targetDayOfWeek = DayOfWeek.of(k);

        // Calculate the first occurrence of the target weekday in the month
        LocalDate firstKWeekdayOfMonth = firstDayOfMonth.with(TemporalAdjusters.nextOrSame(targetDayOfWeek));
        LocalDate nthKWeekdayOfMonth = firstKWeekdayOfMonth.plusWeeks(n - 1);

        // Calculate the last day of the month
        LocalDate lastDayOfMonth = firstDayOfMonth.lengthOfMonth() == 28 ?
                firstDayOfMonth.plusMonths(1).minusDays(1) :
                firstDayOfMonth.with(TemporalAdjusters.lastDayOfMonth());

        if (nthKWeekdayOfMonth.isAfter(lastDayOfMonth)) {
            // Find the last occurrence of the target weekday in the month
            LocalDate lastKWeekdayOfMonth = lastDayOfMonth.with(TemporalAdjusters.previous(targetDayOfWeek));
            return lastKWeekdayOfMonth;
        }

        return nthKWeekdayOfMonth;
    }

    public static void main(String[] args) {
        // Example usage
        LocalDate result = findNthWeekdayOfSpecificYear(2023, 4, 5, 1); // Example parameters
        System.out.println(result.format(DateTimeFormatter.ISO_LOCAL_DATE));
    }
}