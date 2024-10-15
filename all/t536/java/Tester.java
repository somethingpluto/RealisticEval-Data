package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

public class Tester {
    private Date originalDate;

    @Before
    public void setUp() {
        // Mock the current date
        originalDate = new Date();
        System.setProperty("current.test.date", "2024-10-01T00:00:00Z");
    }

    @After
    public void tearDown() {
        // Restore the original date if needed
        System.clearProperty("current.test.date");
    }

    private String getDate() {
        // Get the mocked date
        String testDate = System.getProperty("current.test.date");
        Date currentDate = new Date(testDate);
        
        // Define the date format
        SimpleDateFormat formatter = new SimpleDateFormat("MMMM d, yyyy", Locale.ENGLISH);
        
        // Return the formatted date string
        return formatter.format(currentDate);
    }

    @Test
    public void testReturnsDateInMonthDayYearFormat() {
        String result = getDate();
        assertEquals("October 1, 2024", result);
    }

    @Test
    public void testReturnsCorrectYear() {
        String result = getDate();
        assertTrue(result.matches(".*2024.*"));
    }

    @Test
    public void testReturnsCorrectMonth() {
        String result = getDate();
        assertTrue(result.matches(".*October.*"));
    }

    @Test
    public void testReturnsCorrectDay() {
        String result = getDate();
        assertTrue(result.matches(".*1.*"));
    }

    @Test
    public void testReturnsDateAsString() {
        String result = getDate();
        assertTrue(result instanceof String);
    }

    @Test
    public void testDoesNotReturnUndefined() {
        String result = getDate();
        assertNotNull(result);
    }
}