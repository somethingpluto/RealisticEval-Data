package org.real.temp;

import org.junit.jupiter.api.Test; // JUnit 5 Test annotation
import static org.junit.jupiter.api.Assertions.assertEquals; // JUnit 5 assertion method
import java.time.LocalDate;

public class Tester {

    @Test
    public void testRegularOccurrence() {
        // Test for the 2nd Monday of May 2023
        LocalDate result = findNthWeekdayOfSpecificYear(2023, 5, 2, 0);  // Monday is 0
        LocalDate expected = LocalDate.of(2023, 5, 8);
        assertEquals(expected, result);
    }

    @Test
    public void testLastOccurrence() {
        // Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        LocalDate result = findNthWeekdayOfSpecificYear(2023, 5, 5, 0);  // Monday is 0
        LocalDate expected = LocalDate.of(2023, 5, 29);
        assertEquals(expected, result);
    }

    @Test
    public void testFirstDayIsWeekday() {
        // Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        LocalDate result = findNthWeekdayOfSpecificYear(2023, 8, 1, 1);  // Tuesday is 1
        LocalDate expected = LocalDate.of(2023, 8, 1);
        assertEquals(expected, result);
    }

    @Test
    public void testEdgeYearTransition() {
        // Test for the 1st Friday of December 2023
        LocalDate result = findNthWeekdayOfSpecificYear(2023, 12, 1, 4);  // Friday is 4
        LocalDate expected = LocalDate.of(2023, 12, 1);
        assertEquals(expected, result);
    }
}