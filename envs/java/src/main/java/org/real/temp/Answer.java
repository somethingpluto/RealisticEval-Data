package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Extracts a numeric value from the input string based on the given regex pattern.
     *
     * @param x       The input from which to extract the value. It will be converted to a string.
     * @param pattern The regular expression pattern to use for matching.
     * @return The extracted weight value as a float if a match is found, otherwise an empty string.
     */
    public static String cleanPattern(Object x, String pattern) {
        // Convert input to string
        String input = x.toString();

        // Compile the pattern
        Pattern compiledPattern = Pattern.compile(pattern);
        Matcher matcher = compiledPattern.matcher(input);

        if (matcher.find()) {
            // Extract the weight value from the first matching group
            String weight = matcher.group(1);  // Can also use matcher.group(3) if needed

            try {
                // Convert the weight to a float and return it as a string
                float weightValue = Float.parseFloat(weight);
                return Float.toString(weightValue);
            } catch (NumberFormatException e) {
                // Handle cases where conversion to float fails
                System.out.println("Warning: Unable to convert '" + weight + "' to float.");
                return "";
            }
        } else {
            return "";  // Return empty string if no match is found
        }
    }

    public static void main(String[] args) {
        // Example usage
        Object input = "The weight is 123.45 kg";
        String pattern = "(\\d+\\.\\d+)";
        String result = cleanPattern(input, pattern);
        System.out.println("Extracted Value: " + result);
    }
}