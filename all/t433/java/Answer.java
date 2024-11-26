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
        String[] paragraphsArray = text.split("\n\n");
        
        // Initialize lists to store paragraphs and lines
        List<String> paragraphs = new ArrayList<>();
        List<String> lines = new ArrayList<>();

        // Process each paragraph
        for (String paragraph : paragraphsArray) {
            String trimmedParagraph = paragraph.trim();
            if (!trimmedParagraph.isEmpty()) {
                paragraphs.add(trimmedParagraph);

                // Split each paragraph into lines
                String[] linesArray = paragraph.split("\n");
                for (String line : linesArray) {
                    String trimmedLine = line.trim();
                    if (!trimmedLine.isEmpty()) {
                        lines.add(trimmedLine);
                    }
                }
            }
        }

        // Create and return the map with extracted paragraphs and lines
        Map<String, List<String>> result = new HashMap<>();
        result.put("paragraphs", paragraphs);
        result.put("lines", lines);

        return result;
    }

    // Example usage
    public static void main(String[] args) {
        String text = "This is the first paragraph.\nIt has multiple lines.\n\nThis is the second paragraph.";
        Map<String, List<String>> result = extractParagraphsAndLines(text);
        System.out.println(result);
    }
}