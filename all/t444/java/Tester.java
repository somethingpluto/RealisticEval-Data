package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testFormatComment() {
        String input = "This is a long string that needs to be formatted into multiple lines.";
        int maxLength = 60;
        String expectedOutput = "# This is a long string that\n# needs to be formatted into\n# multiple lines.";

        String actualOutput = formatComment(input, maxLength);

        assertEquals(expectedOutput, actualOutput);
    }

    private String formatComment(String string, int maxLength) {
        StringBuilder result = new StringBuilder();
        String[] words = string.split(" ");
        StringBuilder currentLine = new StringBuilder("# ");

        for (String word : words) {
            if ((currentLine.length() + word.length()) > maxLength) {
                result.append(currentLine).append("\n");
                currentLine = new StringBuilder("# ").append(word);
            } else {
                currentLine.append(word).append(" ");
            }
        }

        result.append(currentLine);
        return result.toString().trim();
    }
}