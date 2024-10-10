package org.real.temp;

import java.time.LocalDate;
import java.time.DayOfWeek;
import java.time.temporal.TemporalAdjusters;

public class Answer {

    public static LocalDate findNthWeekdayOfSpecificYear(int y, int m, int n, int k) {
        LocalDate startDate = LocalDate.of(y, m, 1);
        DayOfWeek targetDayOfWeek = DayOfWeek.of(k + 1); // Days of week in java start from 1(Sunday) to 7(Saturday)
        
        LocalDate nthOccurrence = startDate.with(TemporalAdjusters.firstInMonth(targetDayOfWeek))
                .plusDays((n - 1) * 7);

        if (!nthOccurrence.getMonthValue() == m) { // If the nth occurrence is out of the current month
            return startDate.with(TemporalAdjusters.lastInMonth(targetDayOfWeek));
        }

        return nthOccurrence;
    }
}