package org.real.temp;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.Locale;

public class Answer {

    /**
     * Convert a UNIX timestamp to a formatted datetime string using the system's local timezone.
     *
     * @param mtime UNIX timestamp.
     * @param format Format string for `DateTimeFormatter`.
     * @return Formatted datetime string.
     */
    public static String formatDateTimeStr(long mtime, String format) {
        if (mtime < 0) {
            throw new IllegalArgumentException("mtime cannot be negative");
        }

        ZoneId localTz;
        try {
            // Get the local system timezone
            localTz = ZoneId.systemDefault();
        } catch (Exception e) {
            // Fallback to UTC if the local timezone is not found
            localTz = ZoneId.of("UTC");
        }

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(format, Locale.US);

        try {
            // Convert the UNIX timestamp to a ZonedDateTime object with timezone
            ZonedDateTime dateTime = ZonedDateTime.ofInstant(ZonedDateTime.ofInstant(
                    java.time.Instant.ofEpochSecond(mtime), localTz).toInstant(), localTz);
            // Return the formatted datetime string
            return dateTime.format(formatter);
        } catch (DateTimeParseException e) {
            // Handle any other unexpected errors
            throw new IllegalArgumentException("Error formatting the datetime: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Example usage
        long mtime = 1688235600L; // Example UNIX timestamp
        String format = "%a %b %d %I:%M:%S %p %z %Y"; // Example format string
        System.out.println(formatDateTimeStr(mtime, format));
    }
}