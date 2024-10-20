package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Convert a time duration string in the format 'XhYminZs' to milliseconds.
     *
     * This function takes a string representing a time duration, where hours, minutes, and seconds
     * are optionally provided, and converts this duration into the equivalent number of milliseconds.
     *
     * @param timeStr A string representing the time duration, e.g., '1h20min30s'.
     * @return The equivalent duration in milliseconds, or null if the input is invalid.
     */
    public static Integer convertHmsToMilliseconds(String timeStr) {
        // Regex to match hours, minutes, and seconds
        Pattern pattern = Pattern.compile("^(?:(\\d+)h)?(?:(\\d+)min)?(?:(\\d+)s)?$");
        Matcher matcher = pattern.matcher(timeStr);

        if (!matcher.find()) {
            System.out.println("remindme.py: Cannot convert time string \"" + timeStr + "\" to milliseconds!");
            return null;
        }

        // Extract hours, minutes, and seconds from the regex groups, defaulting to 0 if not present
        int hours = matcher.group(1) != null ? Integer.parseInt(matcher.group(1)) : 0;
        int minutes = matcher.group(2) != null ? Integer.parseInt(matcher.group(2)) : 0;
        int seconds = matcher.group(3) != null ? Integer.parseInt(matcher.group(3)) : 0;

        // Calculate the total duration in milliseconds
        long totalMilliseconds = (hours * 60 * 60 + minutes * 60 + seconds) * 1000;

        return (int) totalMilliseconds;
    }

    public static void main(String[] args) {
        // Example usage
        String timeStr = "1h20min30s";
        Integer result = convertHmsToMilliseconds(timeStr);
        System.out.println("Converted time in milliseconds: " + result);
    }
}