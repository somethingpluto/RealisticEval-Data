package org.real.temp;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

public class Answer {

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

    public static void main(String[] args) {
        // Example usage
        String dateStr = "Fri, 22 Sep 2023 15:45:30 +0000 (UTC)";
        String formattedDate = formatDateString(dateStr);
        System.out.println(formattedDate); // Output: 2023-09-22_15:45:30
    }
}