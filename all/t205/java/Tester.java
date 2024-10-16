package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Tester {

    @Test
    public void testGetCurrentDateFormat() {
        String currentDate = Answer.getCurrentDate();
        assertEquals(10, currentDate.length());
        assertEquals('-', currentDate.charAt(4));
        assertEquals('-', currentDate.charAt(7));
    }

    @Test
    public void testGetCurrentDateYear() {
        int currentYear = LocalDate.now().getYear();
        String currentDate = Answer.getCurrentDate();
        String yearPart = currentDate.substring(0, 4);
        assertEquals(currentYear, Integer.parseInt(yearPart));
    }

    @Test
    public void testGetCurrentDateMonth() {
        int currentMonth = LocalDate.now().getMonthValue();
        String currentDate = Answer.getCurrentDate();
        String monthPart = currentDate.substring(5, 7);
        assertEquals(currentMonth, Integer.parseInt(monthPart));
    }

    @Test
    public void testGetCurrentDateDay() {
        int currentDay = LocalDate.now().getDayOfMonth();
        String currentDate = Answer.getCurrentDate();
        String dayPart = currentDate.substring(8, 10);
        assertEquals(currentDay, Integer.parseInt(dayPart));
    }

    @Test
    public void testGetCurrentDateConsistency() {
        String firstCall = Answer.getCurrentDate();
        String secondCall = Answer.getCurrentDate();
        assertEquals(firstCall, secondCall);
    }
}