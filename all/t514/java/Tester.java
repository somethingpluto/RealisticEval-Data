package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test cases for the extractDateFromFilename method.
 */
public class Tester {

    /**
     * Test case where the date is successfully extracted.
     */
    @Test
    public void testDateExtractionSuccess() {
        String fileName = "report-2023-09-28.txt";
        String expectedDate = "2023-09-28";
        assertEquals(expectedDate, extractDateFromFilename(fileName));
    }

    /**
     * Test case where no date is present in the filename.
     */
    @Test
    public void testNoDateInFilename() {
        String fileName = "report.txt";
        assertNull(extractDateFromFilename(fileName));
    }

    /**
     * Test case where multiple dates are present, should return the first one.
     */
    @Test
    public void testMultipleDatesInFilename() {
        String fileName = "report-2023-09-28-backup-2023-10-01.txt";
        String expectedDate = "2023-09-28";
        assertEquals(expectedDate, extractDateFromFilename(fileName));
    }

    /**
     * Test case where the date is at the start of the filename.
     */
    @Test
    public void testDateAtStartOfFile() {
        String fileName = "2023-09-28-report.txt";
        String expectedDate = "2023-09-28";
        assertEquals(expectedDate, extractDateFromFilename(fileName));
    }

    /**
     * Test case where the date format is incorrect.
     */
    @Test
    public void testIncorrectDateFormat() {
        String fileName = "report-2023-99-99.txt";  // Invalid date
        String expectedDate = "2023-99-99";
        assertEquals(expectedDate, extractDateFromFilename(fileName));
    }

    // Utility method to extract the date from the filename
    private String extractDateFromFilename(String fileName) {
        // Define the regex pattern for matching a date in the format YYYY-MM-DD
        Pattern datePattern = Pattern.compile("\\d{4}-\\d{2}-\\d{2}");

        // Search for the date pattern in the file name
        Matcher matcher = datePattern.matcher(fileName);

        // If a match is found, return the matched date; otherwise, return null
        if (matcher.find()) {
            return matcher.group(0);
        } else {
            return null;
        }
    }
}