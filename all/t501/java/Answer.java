package org.real.temp;

public class Answer {

    /**
     * Converts a string concatenated with underscores to a short format.
     *
     * @param inputStr The input string with segments separated by underscores.
     * @return A short format string derived from the first characters of each segment.
     */
    public static String convertToShortFormat(String inputStr) {
        // Split the input string by underscores
        String[] segments = inputStr.split("_");

        // Extract the first character from each segment and join them
        StringBuilder shortFormat = new StringBuilder();
        for (String segment : segments) {
            if (!segment.isEmpty()) {
                shortFormat.append(segment.charAt(0));
            }
        }

        return shortFormat.toString();
    }

    // Example usage
    public static void main(String[] args) {
        String exampleInput = "example_input_string";
        System.out.println(convertToShortFormat(exampleInput)); // Output: eis
    }
}