package org.real.temp;

public class Answer {

    /**
     * Formats a string by prepending '> ' to each line and ensuring proper
     * formatting of code blocks.
     *
     * @param x The input string to be formatted. If the input is not a
     *          string, it will be converted to one.
     * @return The formatted string with each line prefixed by '> ' and
     *         with balanced code block delimiters.
     */
    public static String formatStr(Object x) {
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
        String s = formattedLines.toString();
        s = s.replaceAll("[\r\n]+$", "");
        // Return the final formatted string.
        return s;
    }

    public static void main(String[] args) {
        // Example usage
        String result = formatStr("Hello\nWorld\n```code\n```");
        System.out.println(result);
    }
}