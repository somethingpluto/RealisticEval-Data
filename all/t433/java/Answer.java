package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {

    /**
     * Extracts paragraphs and lines from the given text.
     *
     * @param text The input text from which paragraphs and lines will be extracted.
     * @return A Map containing:
     *         - 'paragraphs': A List of paragraphs extracted from the text.
     *         - 'lines': A List of lines extracted from the text.
     */
    public static Map<String, List<String>> extractParagraphsAndLines(String text) {
        // Split the text into paragraphs
        String[] paragraphs = text.split("\n\n");

        // Split each paragraph into lines
        List<String> lines = new ArrayList<>();
        for (String paragraph : paragraphs) {
            String[] paragraphLines = paragraph.split("\n");
            for (String line : paragraphLines) {
                lines.add(line);
            }
        }

        // Remove empty paragraphs and lines
        List<String> filteredParagraphs = new ArrayList<>();
        for (String paragraph : paragraphs) {
            if (!paragraph.trim().isEmpty()) {
                filteredParagraphs.add(paragraph.trim());
            }
        }

        List<String> filteredLines = new ArrayList<>();
        for (String line : lines) {
            if (!line.trim().isEmpty()) {
                filteredLines.add(line.trim());
            }
        }

        // Return the extracted paragraphs and lines in a Map
        Map<String, List<String>> result = new HashMap<>();
        result.put("paragraphs", filteredParagraphs);
        result.put("lines", filteredLines);

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        String text = "This is a paragraph.\n\nThis is another paragraph.\nIt has multiple lines.\n\n";
        Map<String, List<String>> result = extractParagraphsAndLines(text);
        System.out.println(result);
    }
}