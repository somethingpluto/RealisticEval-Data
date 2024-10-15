package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.time.LocalDate;

public class Tester {

    @Test
    public void testGetCurrentDateFormat() {
        String date = Tester.getCurrentDate();
        assertTrue(date instanceof String);
        assertTrue(date.matches("^\\d{4}-\\d{2}-\\d{2}$"));
    }

    @Test
    public void testGetCurrentDateCorrectness() {
        String expectedDate = LocalDate.now().toString();
        String actualDate = Tester.getCurrentDate();
        assertEquals(expectedDate, actualDate);
    }

    @Test
    public void testGetCurrentDateYearPart() {
        String currentYear = String.valueOf(LocalDate.now().getYear());
        String actualDate = Tester.getCurrentDate();
        assertTrue(actualDate.startsWith(currentYear));
    }

    @Test
    public void testGetCurrentDateMonthPart() {
        String currentMonth = String.format("%02d", LocalDate.now().getMonthValue());
        String actualDate = Tester.getCurrentDate();
        assertEquals(currentMonth, actualDate.substring(5, 7));
    }

    @Test
    public void testGetCurrentDateDayPart() {
        String currentDay = String.format("%02d", LocalDate.now().getDayOfMonth());
        String actualDate = Tester.getCurrentDate();
        assertEquals(currentDay, actualDate.substring(8, 10));
    }
}