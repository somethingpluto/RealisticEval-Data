package org.real.temp;

public class Answer {

    /**
     * Formats a string into a commented block with specified maximum line length.
     *
     * @param string      the input string to format
     * @param maxLength   maximum length of each line in the output
     * @return            a formatted string with each line prefixed by '# ' and not exceeding the specified max_length
     */
    public static String formatComment(String string, int maxLength) {
        if (string == null || string.isEmpty()) return "";

        StringBuilder sb = new StringBuilder();
        String[] words = string.split(" ");
        StringBuilder currentLine = new StringBuilder("# ");

        for (String word : words) {
            if ((currentLine.length() + word.length()) > maxLength) {
                sb.append(currentLine.toString()).append("\n");
                currentLine = new StringBuilder("# ").append(word);
            } else {
                currentLine.append(word).append(" ");
            }
        }

        sb.append(currentLine.toString());
        return sb.toString();
    }
}
