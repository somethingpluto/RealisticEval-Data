package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Converts an ISO 8601 duration string into a more readable format.
     * 
     * @param duration The ISO 8601 duration string (e.g., "PT1H23M45.678S").
     * @returns A human-readable duration string (e.g., "1h23m45s678ms").
     */
    public static String convertTime(String duration) {
        String regex = "PT(?:(\\d+)H)?(?:(\\d+)M)?(?:(\\d+)(\\.\\d+)?S)?";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(duration);

        if (!matcher.matches()) {
            return ""; // Return an empty string if the input doesn't match the expected format
        }

        StringBuilder convertedTime = new StringBuilder();

        String hours = matcher.group(1);
        String minutes = matcher.group(2);
        String seconds = matcher.group(3);
        String fractionalSeconds = matcher.group(4);

        if (hours != null) {
            convertedTime.append(hours).append("h");
        }

        if (minutes != null) {
            convertedTime.append(minutes).append("m");
        }

        if (seconds != null) {
            convertedTime.append(seconds).append("s");
        }

        if (fractionalSeconds != null) {
            int milliseconds = Math.round(Float.parseFloat(fractionalSeconds) * 1000);
            if (milliseconds > 0) {
                convertedTime.append(milliseconds).append("ms");
            }
        }

        return convertedTime.toString();
    }

    public static void main(String[] args) {
        String duration = "PT1H23M45.678S";
        System.out.println(convertTime(duration)); // Output: 1h23m45s678ms
    }
}