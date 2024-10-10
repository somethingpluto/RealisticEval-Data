package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    public static Integer convertHmsToMilliseconds(String timeStr) {
        // Regular expression to match the time duration pattern
        Pattern pattern = Pattern.compile("(\\d+)h(\\d+)min(\\d+)s");
        Matcher matcher = pattern.matcher(timeStr);

        if (matcher.matches()) {
            int hours = Integer.parseInt(matcher.group(1));
            int minutes = Integer.parseInt(matcher.group(2));
            int seconds = Integer.parseInt(matcher.group(3));

            // Convert hours, minutes, and seconds to milliseconds
            return (hours * 60 * 60 * 1000) + (minutes * 60 * 1000) + (seconds * 1000);
        } else {
            // Return null if the input is invalid
            return null;
        }
    }

    public static void main(String[] args) {
        // Test the function with an example
        String timeStr = "1h20min30s";
        Integer milliseconds = convertHmsToMilliseconds(timeStr);
        System.out.println("Milliseconds: " + milliseconds);
    }
}