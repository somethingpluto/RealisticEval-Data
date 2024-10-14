package org.real.temp;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

@RunWith(JUnit4.class)
public class Tester {

    private static Map<String, List<String>> extract_paragraphs_and_lines(String text) {
        String[] paragraphs = text.split("\n\n");
        String[] lines = text.split("\n");

        List<String> paragraphsList = Arrays.asList(paragraphs);
        List<String> linesList = Arrays.asList(lines);

        return Map.of(
            "paragraphs", paragraphsList,
            "lines", linesList
        );
    }

    @Test
    public void testExtractParagraphsAndLines() {
        // Test data
        String text = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.";

        // Expected result
        Map<String, List<String>> expectedResult = Map.of(
            "paragraphs", Arrays.asList("First paragraph.\nThis is the second line.", "Second paragraph.\nAnother line."),
            "lines", Arrays.asList("First paragraph.", "This is the second line.", "Second paragraph.", "Another line.")
        );

        // Actual result
        Map<String, List<String>> actualResult = extract_paragraphs_and_lines(text);

        // Assertion
        assertEquals(expectedResult, actualResult);
    }
}