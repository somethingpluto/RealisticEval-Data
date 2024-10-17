package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Wrap the text content to the specified maximum width and return a list of wrapped lines.
     *
     * @param content The content to be wrapped.
     * @param width The maximum width of the lines, default is 80 characters.
     * @return A List containing each line of the content wrapped to the specified width.
     */
    public static List<String> wrapContentGenerator(String content, int width) {
        if (width <= 0) {
            width = 80; // Default width
        }

        List<String> wrappedLines = new ArrayList<>();
        String[] lines = content.split("(?<=\n)|(?<=\r\n)");

        for (String line : lines) {
            if (line.trim().isEmpty()) {  // Check if the line is essentially empty.
                wrappedLines.add("\n");
            } else {
                List<String> subWrappedLines = wrapLine(line, width);
                wrappedLines.addAll(subWrappedLines);
            }
        }

        return wrappedLines;
    }

    private static List<String> wrapLine(String line, int width) {
        List<String> subWrappedLines = new ArrayList<>();
        int start = 0;

        while (start < line.length()) {
            int end = Math.min(start + width, line.length());
            while (end < line.length() && line.charAt(end) != ' ') {
                end--; // Move back to the last space character
            }

            if (end == start) { // No spaces found, just break at width
                end = start + width;
            }

            subWrappedLines.add(line.substring(start, end));
            start = end;
        }

        return subWrappedLines;
    }

    public static void main(String[] args) {
        String content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
        List<String> wrappedContent = wrapContentGenerator(content, 40);
        for (String line : wrappedContent) {
            System.out.println(line);
        }
    }
}