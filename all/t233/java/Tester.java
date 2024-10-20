package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testSingleLineComment() {
        // Test string with a comment on a single line
        String inputString = "Hello, world!# This is a comment";
        String expectedOutput = "Hello, world!";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testNoComments() {
        // Test string with no comments
        String inputString = "Hello, world!\nPython is fun!";
        String expectedOutput = "Hello, world!\nPython is fun!";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testEmptyString() {
        // Test an empty string
        String inputString = "";
        String expectedOutput = "";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testCommentsOnly() {
        // Test string where all lines are comments
        String inputString = "# comment only line\n#another comment line";
        String expectedOutput = "\n";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    // Utility method to remove comments from a string
    private String removeComments(String input) {
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
}