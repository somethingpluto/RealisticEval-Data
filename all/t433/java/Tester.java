package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSingleParagraph() {
        String inputText = "This is a single paragraph.";
        Map<String, List<String>> expectedOutput = new HashMap<>();
        expectedOutput.put("paragraphs", Arrays.asList("This is a single paragraph."));
        expectedOutput.put("lines", Arrays.asList("This is a single paragraph."));

        Map<String, List<String>> actualOutput = extractParagraphsAndLines(inputText);
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testMultipleParagraphs() {
        String inputText = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.";
        Map<String, List<String>> expectedOutput = new HashMap<>();
        expectedOutput.put("paragraphs", Arrays.asList(
            "First paragraph.\nThis is the second line.",
            "Second paragraph.\nAnother line."
        ));
        expectedOutput.put("lines", Arrays.asList(
            "First paragraph.",
            "This is the second line.",
            "Second paragraph.",
            "Another line."
        ));

        Map<String, List<String>> actualOutput = extractParagraphsAndLines(inputText);
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testLeadingAndTrailingWhitespace() {
        String inputText = "   This paragraph has leading whitespace.\nAnd a line after.\n\n   This one has trailing whitespace.   ";
        Map<String, List<String>> expectedOutput = new HashMap<>();
        expectedOutput.put("paragraphs", Arrays.asList(
            "This paragraph has leading whitespace.\nAnd a line after.",
            "This one has trailing whitespace."
        ));
        expectedOutput.put("lines", Arrays.asList(
            "This paragraph has leading whitespace.",
            "And a line after.",
            "This one has trailing whitespace."
        ));

        Map<String, List<String>> actualOutput = extractParagraphsAndLines(inputText);
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testEmptyString() {
        String inputText = "";
        Map<String, List<String>> expectedOutput = new HashMap<>();
        expectedOutput.put("paragraphs", new ArrayList<>());
        expectedOutput.put("lines", new ArrayList<>());

        Map<String, List<String>> actualOutput = extractParagraphsAndLines(inputText);
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testMultipleEmptyParagraphs() {
        String inputText = "\n\n\n";
        Map<String, List<String>> expectedOutput = new HashMap<>();
        expectedOutput.put("paragraphs", new ArrayList<>());
        expectedOutput.put("lines", new ArrayList<>());

        Map<String, List<String>> actualOutput = extractParagraphsAndLines(inputText);
        assertEquals(expectedOutput, actualOutput);
    }
}