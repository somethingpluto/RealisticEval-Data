package org.real.temp;

public class Answer {

    /**
     * Removes the common leading indentation from each line in a given multi-line string,
     * preserving the relative indentation of the text.
     *
     * @param multilineText The input string containing multiple lines.
     * @return The sanitized string with common leading indentation removed.
     */
    public static String removeCommonIndentation(String multilineText) {
        String[] lines = multilineText.split("\n");

        // Filter out lines that are empty or only whitespace, as they do not affect minimum indentation
        int minIndent = Integer.MAX_VALUE;
        for (String line : lines) {
            String trimmedLine = line.trim();
            if (!trimmedLine.isEmpty()) {
                int indent = line.length() - trimmedLine.length();
                minIndent = Math.min(minIndent, indent);
            }
        }

        // If there's no indentation or all lines are empty, return the original string
        if (minIndent == Integer.MAX_VALUE) {
            return multilineText;
        }

        // Remove the common leading indentation from each line
        StringBuilder sanitizedLines = new StringBuilder();
        for (String line : lines) {
            if (sanitizedLines.length() > 0) {
                sanitizedLines.append("\n");
            }
            sanitizedLines.append(line.substring(minIndent));
        }

        return sanitizedLines.toString();
    }

    public static void main(String[] args) {
        // Example usage
        String multilineText = "    This is a test.\n" +
                               "      This is another line.\n" +
                               "    And this is the last line.";
        System.out.println(removeCommonIndentation(multilineText));
    }
}
