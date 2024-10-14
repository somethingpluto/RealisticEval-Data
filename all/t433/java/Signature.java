import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class TextProcessor {

    /**
     * Extracts paragraphs and lines from the given text. Paragraphs end with \n\n and lines end with \n.
     *
     * Example usage:
     * Input: "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line."
     * Output: A Map where:
     *         - Key 'paragraphs' maps to a List of paragraphs extracted from the text.
     *         - Key 'lines' maps to a List of lines extracted from the text.
     *
     * @param text The input text from which paragraphs and lines will be extracted.
     * @return A Map containing:
     *         - 'paragraphs': A List of paragraphs extracted from the text.
     *         - 'lines': A List of lines extracted from the text.
     */
    public static Map<String, List<String>> extractParagraphsAndLines(String text) {
        // Method implementation goes here
        return new HashMap<>();
    }
}