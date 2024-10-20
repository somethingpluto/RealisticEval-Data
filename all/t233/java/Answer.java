package org.real.temp;

public class Answer {

    /**
     * Removes comments from the provided string. Comments start with a '#' and end at the newline.
     *
     * @param input The input string containing potential comments.
     * @return The string with all comments removed.
     */
    public static String removeComments(String input) {
        // Split the string into lines
        String[] lines = input.split("\n");

        // Remove the comment part from each line
        StringBuilder cleanedString = new StringBuilder();
        for (String line : lines) {
            int commentIndex = line.indexOf('#');
            if (commentIndex != -1) {
                line = line.substring(0, commentIndex);
            }
            cleanedString.append(line).append("\n");
        }

        // Remove the last newline character added during the loop
        if (cleanedString.length() > 0) {
            cleanedString.setLength(cleanedString.length() - 1);
        }

        return cleanedString.toString();
    }

    public static void main(String[] args) {
        // Example usage
        String input = "This is a line\n# This is a comment\nAnother line without comment";
        String output = removeComments(input);
        System.out.println(output);
    }
}