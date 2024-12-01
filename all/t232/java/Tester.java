package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test cases for the convertHmsToMilliseconds function.
 */
public class Tester {

    @Test
    public void testBasicConversion() {
        assertEquals("Should convert 1h20min30s to 4830000 milliseconds",
                4830000L, convertHmsToMilliseconds("1h20min30s").orElse(-1L));
    }

    @Test
    public void testNoHoursOrMinutes() {
        assertEquals("Should convert 30s to 30000 milliseconds",
                30000L, convertHmsToMilliseconds("30s").orElse(-1L));
    }

    @Test
    public void testInvalidFormat() {
        assertNull("Should return null for invalid time format",
                convertHmsToMilliseconds("1hour20minutes"));
    }

    @Test
    public void testEdgeCaseMaxOneDay() {
        assertEquals("Should convert 23h59min59s to 86399000 milliseconds",
                86399000L, convertHmsToMilliseconds("23h59min59s").orElse(-1L));
    }

    @Test
    public void testExceedingOneDay() {
        assertEquals("Should correctly convert 24h1min to 86460000 milliseconds",
                86460000L, convertHmsToMilliseconds("24h1min").orElse(-1L));
    }

    // Method to be tested
    private Optional<Long> convertHmsToMilliseconds(String timeStr) {
        // Regex to match hours, minutes, and seconds
        Pattern pattern = Pattern.compile("^(?:(\\d+)h)?(?:(\\d+)min)?(?:(\\d+)s)?$");
        Matcher matcher = pattern.matcher(timeStr);

        if (!matcher.find()) {
            System.out.println("remindme.py: Cannot convert time string \"" + timeStr + "\" to milliseconds!");
            return Optional.empty();
        }

        // Extract hours, minutes, and seconds from the regex groups, defaulting to 0 if not present
        int hours = matcher.group(1) != null ? Integer.parseInt(matcher.group(1)) : 0;
        int minutes = matcher.group(2) != null ? Integer.parseInt(matcher.group(2)) : 0;
        int seconds = matcher.group(3) != null ? Integer.parseInt(matcher.group(3)) : 0;

        // Calculate the total duration in milliseconds
        long totalMilliseconds = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

        return Optional.of(totalMilliseconds);
    }
}