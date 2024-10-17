package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Test cases for the formatDateString method.
 */
public class Tester {

    /**
     * Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
     * to the format '%Y-%m-%d_%H:%M:%S'.
     *
     * @param dateStr The input date string.
     * @return The formatted date string in the format '%Y-%m-%d_%H:%M:%S', or null if the input date string is invalid.
     */
    public static String formatDateString(String dateStr) {
        SimpleDateFormat inputFormat = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss zzz (Z)");
        SimpleDateFormat outputFormat = new SimpleDateFormat("yyyy-MM-dd_HH:mm:ss");

        try {
            // Parse the input date string to a Date object
            Date dateObject = inputFormat.parse(dateStr);

            // Format the Date object to the desired output format
            String formattedDate = outputFormat.format(dateObject);

            return formattedDate;
        } catch (ParseException e) {
            System.out.println("Error parsing date: " + e.getMessage());
            return null;
        }
    }

    @Test
    public void testValidDateConversion() {
        String dateStr = "Fri, 28 Sep 2023 14:45:00 +0000 (UTC)";
        String expectedDate = "2023-09-28_14:45:00";
        assertEquals(expectedDate, formatDateString(dateStr));
    }

    @Test
    public void testInvalidDateFormat() {
        String dateStr = "Invalid date format";
        assertNull(formatDateString(dateStr));
    }

    @Test
    public void testMissingComponents() {
        String dateStr = "Fri, 28 Sep 2023 14:45:00 +0000";
        assertNull(formatDateString(dateStr));
    }

    @Test
    public void testEdgeCaseDate() {
        String dateStr = "Sun, 29 Feb 2024 14:45:00 +0000 (UTC)";
        String expectedDate = "2024-02-29_14:45:00";
        assertEquals(expectedDate, formatDateString(dateStr));
    }
}