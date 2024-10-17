package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for the formatStr method.
 */
public class Tester {

    /**
     * Tests a simple string input.
     */
    @Test
    public void testSimpleString() {
        String inputStr = "Hello, World!";
        String expectedOutput = "> Hello, World!";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests a multiline string input.
     */
    @Test
    public void testMultilineString() {
        String inputStr = "Line 1\nLine 2\nLine 3";
        String expectedOutput = "> Line 1\n> Line 2\n> Line 3";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests a string with an even number of code block delimiters.
     */
    @Test
    public void testCodeBlockDelimitersEven() {
        String inputStr = "Some code:\n```\nprint('Hello')\n```";
        String expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests a string with an odd number of code block delimiters.
     */
    @Test
    public void testCodeBlockDelimitersOdd() {
        String inputStr = "Some code:\n```\nprint('Hello')";
        String expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests non-string input (e.g., integer) to ensure it's converted.
     */
    @Test
    public void testNonStringInput() {
        Object inputValue = 123;
        String expectedOutput = "> 123";
        assertEquals(expectedOutput, formatStr(inputValue));
    }

    // The formatStr method implementation
    private String formatStr(Object x) {
        // Convert x to string if it's not already a string.
        String str = x.toString();

        // Ensure there is a matching number of code block delimiters.
        // If the count of delimiters is odd, append an additional one to balance.
        int delimiterCount = str.length() - str.replace("```", "").length();
        if (delimiterCount % 2 == 1) {
            str += "\n```";
        }

        // Format each line by prepending '> ' and join them with newlines.
        String[] lines = str.split("\n");
        StringBuilder formattedLines = new StringBuilder();
        for (String line : lines) {
            formattedLines.append("> ").append(line).append("\n");
        }

        // Return the final formatted string.
        return formattedLines.toString();
    }
}