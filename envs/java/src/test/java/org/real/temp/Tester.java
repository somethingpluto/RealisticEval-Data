package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.real.temp.Answer.getTime;

public class Tester {
    private static final String originalTimeZone = TimeZone.getDefault().getID();

    @Before
    public void setUp() {
        TimeZone.setDefault(TimeZone.getTimeZone("UTC")); // Set a consistent timezone for testing
    }

    @After
    public void tearDown() {
        TimeZone.setDefault(TimeZone.getTimeZone(originalTimeZone)); // Restore original timezone
    }

    private String mockDate(String dateString) {
        System.setProperty("current.time", dateString); // Simulate mock date (you would need to implement this in getTime)
        return getTime();
    }

    @Test
    public void shouldReturnAString() {
        String result = mockDate("2024-10-01T10:30:00");
        assertTrue(result instanceof String);
    }

    @Test
    public void shouldReturnFormattedTimeStringIncludingAMPM() {
        String result = mockDate("2024-10-01T15:45:00");
        assertTrue(result.matches("^\\d{1,2}:\\d{2} (AM|PM)$"));
    }

    @Test
    public void shouldReturnCorrectTimeDuringAMHours() {
        String result = mockDate("2024-10-01T08:15:00");
        assertEquals("8:15 AM", result);
    }

    @Test
    public void shouldReturnCorrectTimeDuringPMHours() {
        String result = mockDate("2024-10-01T17:20:00");
        assertEquals("5:20 PM", result);
    }

    @Test
    public void shouldReturn12AMAtMidnight() {
        String result = mockDate("2024-10-01T00:00:00");
        assertEquals("12:00 AM", result);
    }

    @Test
    public void shouldReturn12PMAtNoon() {
        String result = mockDate("2024-10-01T12:00:00");
        assertEquals("12:00 PM", result);
    }

    @Test
    public void shouldHandleSingleDigitMinutesCorrectly() {
        String result = mockDate("2024-10-01T09:05:00");
        assertEquals("9:05 AM", result);
    }
}