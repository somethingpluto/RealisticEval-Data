package org.real.temp;

public class Answer {

    /**
     * Converts a numerical value into a string representation with appropriate
     * suffixes ('k' for thousands, 'm' for millions) or returns the number as a string
     * if the value is below 1000. Returns an empty string for non-numeric or invalid inputs.
     *
     * @param value - The value to convert.
     * @return - The formatted string or an empty string if the input is invalid.
     */
    public static String setEurValue(Object value) {
        // Check for null inputs directly
        if (value == null) return "";

        // Attempt to parse the input value to an integer
        int number;
        try {
            number = Integer.parseInt(value.toString());
        } catch (NumberFormatException e) {
            return "";
        }

        // Determine the suffix and division based on the size of the number
        if (number >= 1_000_000) {
            return String.format("%.1fm", number / 1_000_000.0);  // Format for millions
        } else if (number >= 1_000) {
            return String.format("%.1fk", number / 1_000.0);      // Format for thousands
        } else {
            return Integer.toString(number);                       // Return as string for smaller numbers
        }
    }
}