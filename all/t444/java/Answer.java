package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Formats a string into a commented block with a specified maximum line length.
     *
     * @param string      The input string to format.
     * @param maxLength   Maximum length of each line in the output.
     * @return            A formatted string with each line prefixed by "# " and not exceeding the specified maxLength.
     */
    public static String formatComment(String string, int maxLength) {
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
                if (currentLine.length() + word.length() > maxLength) {
                    formattedLines.add(currentLine.toString());
                    currentLine = new StringBuilder();
                }

                // If the current line is empty, add the word to the line
                // Otherwise, add a space and the word to the line
                if (currentLine.length() == 0) {
                    currentLine.append(word);
                } else {
                    currentLine.append(" ").append(word);
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

    public static void main(String[] args) {
        String testString = "This is a very long string that needs to be split into multiple lines to ensure it does not exceed the maximum length.";
        System.out.println(formatComment(testString, 30));
    }
}