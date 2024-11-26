package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for the formatComment function.
 */
public class Tester {

    /**
     * Test with a short string that fits within max_length.
     */
    @Test
    public void testShortString() {
        String inputString = "This is a test.";
        String expectedOutput = "# This is a test.";
        assertEquals(expectedOutput, formatComment(inputString));
    }

    /**
     * Test with a longer string that exceeds max_length.
     */
    @Test
    public void testLongString() {
        String inputString = "This is a test of the format_comment function which should wrap long lines correctly.";
        String expectedOutput = 
            "# This is a test of the format_comment function which should\n" +
            "# wrap long lines correctly.";
        assertEquals(expectedOutput, formatComment(inputString, 60));
    }

    /**
     * Test with multiple lines of input.
     */
    @Test
    public void testMultipleLines() {
        String inputString = "First line.\nSecond line that is quite long and needs to be wrapped.";
        String expectedOutput = 
            "# First line.\n" +
            "# Second line that is quite long and needs to be wrapped.";
        assertEquals(expectedOutput, formatComment(inputString, 60));
    }

    /**
     * Test with a line that is exactly max_length characters long.
     */
    @Test
    public void testExactMaxLength() {
        String inputString = "A".repeat(60);  // 60 characters long
        String expectedOutput = "# " + "A".repeat(60);
        assertEquals(expectedOutput, formatComment(inputString, 60));
    }

    /**
     * Test with an empty string.
     */
    @Test
    public void testEmptyString() {
        String inputString = "";
        String expectedOutput = "# ";
        assertEquals(expectedOutput, formatComment(inputString));
    }

    // Utility method to simulate the formatComment function
    private String formatComment(String string, int maxLength) {
        // Split the string into lines
        String[] lines = string.split("\n");

        // Initialize a list to store the formatted lines
        List<String> formattedLines = new ArrayList<>();

        // Iterate through the lines
        for (String line : lines) {
            // Split the line into words
            String[] words = line.split(" ");

            // Initialize a variable to keep track of the current line
            StringBuilder currentLine = new StringBuilder();

            // Iterate through the words
            for (String word : words) {
                // If the current line plus the next word would be too long,
                // append the current line to the list of formatted lines and start a new line
                if (currentLine.length() + word.length() + 1 > maxLength) {
                    formattedLines.add(currentLine.toString());
                    currentLine = new StringBuilder(word);
                } else {
                    // If the current line is empty, add the word to the line
                    // Otherwise, add a space and the word to the line
                    if (currentLine.length() == 0) {
                        currentLine.append(word);
                    } else {
                        currentLine.append(" ").append(word);
                    }
                }
            }

            // Add the remaining line to the list of formatted lines
            formattedLines.add(currentLine.toString());
        }

        // Return the formatted comment
        StringBuilder result = new StringBuilder();
        for (String line : formattedLines) {
            result.append("# ").append(line).append("\n");
        }

        return result.toString();
    }

    // Utility method to simulate the formatComment function with default max_length
    private String formatComment(String string) {
        return formatComment(string, 60);
    }
}