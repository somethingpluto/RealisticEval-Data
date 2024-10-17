package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Extracts the date in the format YYYY-MM-DD from the given file name.
     *
     * @param fileName The name of the file which may contain a date.
     * @return The extracted date string in YYYY-MM-DD format if found, else null.
     */
    public static String extractDateFromFilename(String fileName) {
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

    public static void main(String[] args) {
        // Example usage
        String fileName = "report_2023-04-15.txt";
        String date = extractDateFromFilename(fileName);
        System.out.println("Extracted Date: " + date);
    }
}