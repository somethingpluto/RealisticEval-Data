package org.real.temp;

import java.time.Duration;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Converts a time duration string into a Duration object.
     * The input string can include days (d), hours (h), minutes (m), seconds (s), and milliseconds (ms).
     * e.g. "1d 2h 3m 4s 500ms"
     * Each unit should be specified by an integer followed by its corresponding unit letter.
     *
     * @param timeString A string representing the time duration.
     * @return Duration An object representing the input duration.
     */
    public static Duration genTimeoutDuration(String timeString) {
        Pattern pattern = Pattern.compile("(\\d+)([dhms])");
        Matcher matcher = pattern.matcher(timeString);

        long totalDuration = 0;
        while (matcher.find()) {
            int value = Integer.parseInt(matcher.group(1));
            char unit = matcher.group(2).charAt(0);

            switch (unit) {
                case 'd':
                    totalDuration += value * 24 * 60 * 60 * 1000; // Convert days to milliseconds
                    break;
                case 'h':
                    totalDuration += value * 60 * 60 * 1000; // Convert hours to milliseconds
                    break;
                case 'm':
                    totalDuration += value * 60 * 1000; // Convert minutes to milliseconds
                    break;
                case 's':
                    totalDuration += value * 1000; // Convert seconds to milliseconds
                    break;
                case 'ms':
                    totalDuration += value; // Already in milliseconds
                    break;
                default:
                    throw new IllegalArgumentException("Invalid unit: " + unit);
            }
        }

        return Duration.ofMillis(totalDuration);
    }

    public static void main(String[] args) {
        String timeString = "1d 2h 3m 4s 500ms";
        Duration duration = genTimeoutDuration(timeString);
        System.out.println(duration.toDays() + " days, " +
                           duration.toHoursPart() + " hours, " +
                           duration.toMinutesPart() + " minutes, " +
                           duration.getSeconds() + " seconds, " +
                           duration.getNano() / 1_000_000 + " milliseconds");
    }
}