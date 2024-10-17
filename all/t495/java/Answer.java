package org.real.temp;

import java.util.*;

public class Answer {
    /**
     * Filters website content to include lines containing any of the specified keywords as whole words,
     * along with a specified number of lines before and after for context. This version uses regular expressions
     * to ensure exact, whole word matching and respects case sensitivity.
     *
     * @param content       The full text content of the website.
     * @param keywords      A list of strings to search for within the content.
     * @param linesBefore   Number of lines to include before a matching line.
     * @param linesAfter    Number of lines to include after a matching line.
     * @return              A string containing the filtered content with additional context.
     */
    public static String filterContentWithContext(String content, List<String> keywords, int linesBefore, int linesAfter) {
        // Split the content into individual lines
        String[] lines = content.split("\\R");
        Set<Integer> matchedLines = new HashSet<>();  // Use a set to avoid duplicate lines

        // Compile the regular expression pattern for whole word matching
        Pattern pattern = Pattern.compile("\\b(" + String.join("|", keywords.stream().map(Pattern::quote).toArray(String[]::new)) + ")\\b");

        // Iterate over each line to find matches
        for (int i = 0; i < lines.length; i++) {
            Matcher matcher = pattern.matcher(lines[i]);
            if (matcher.find()) {
                // Determine the range of lines to include for context
                int start = Math.max(i - linesBefore, 0);
                int end = Math.min(i + linesAfter + 1, lines.length);

                // Add the context lines to the set
                for (int j = start; j < end; j++) {
                    matchedLines.add(j);
                }
            }
        }

        // Extract the matched lines and their context, sorted by their original order
        List<String> filteredLines = new ArrayList<>();
        for (int i : matchedLines) {
            filteredLines.add(lines[i]);
        }

        // Join the filtered lines back into a single string
        return String.join("\n", filteredLines);
    }

    public static void main(String[] args) {
        // Example usage
        String content = "This is a sample text.\nIt contains some keywords like hello and world.\nhello\nworld";
        List<String> keywords = Arrays.asList("hello", "world");
        String filteredContent = filterContentWithContext(content, keywords, 1, 1);
        System.out.println(filteredContent);
    }
}