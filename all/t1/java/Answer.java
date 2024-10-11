package org.real.temp;

public class Answer {

    /**
     * Convert the input string. First, check if it is an integer; if it is, convert to an integer.
     * If it is not, check if it is a floating-point number; if yes, convert to a floating-point number.
     * If neither, return the original string.
     *
     * @param value input value string
     * @return converted value as Integer, Double, or String
     */
    public static Object numericalStrConvert(String value) {
        try {
            // Try to parse as an integer
            return Integer.parseInt(value);
        } catch (NumberFormatException e1) {
            try {
                // Try to parse as a double
                return Double.parseDouble(value);
            } catch (NumberFormatException e2) {
                // If neither, return the original string
                return value;
            }
        }
    }
}