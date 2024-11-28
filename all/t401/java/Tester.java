package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;

/**
 * Test class for the findPlaceholders method.
 */
public class Tester {

    /**
     * Test string with multiple placeholders.
     */
    @Test
    public void testMultiplePlaceholders() {
        String inputText = "Here are some placeholders: {{ placeholder1 }}, {{ placeholder2 }}, and {{ placeholder3 }}.";
        List<String> expectedOutput = Arrays.asList("placeholder1", "placeholder2", "placeholder3");
        assertEquals(expectedOutput, Answer.findPlaceholders(inputText));
    }

    /**
     * Test string with no placeholders.
     */
    @Test
    public void testNoPlaceholders() {
        String inputText = "This string has no placeholders.";
        List<String> expectedOutput = Arrays.asList();
        assertEquals(expectedOutput, Answer.findPlaceholders(inputText));
    }

    /**
     * Test string with a single placeholder.
     */
    @Test
    public void testSinglePlaceholder() {
        String inputText = "The only placeholder is {{ singlePlaceholder }}.";
        List<String> expectedOutput = Arrays.asList("singlePlaceholder");
        assertEquals(expectedOutput, Answer.findPlaceholders(inputText));
    }

    /**
     * Test string with placeholders that have extra spaces.
     */
    @Test
    public void testPlaceholderWithSpaces() {
        String inputText = "Placeholders with spaces: {{  placeholder_with_spaces  }} and {{ placeholder2 }}.";
        List<String> expectedOutput = Arrays.asList("placeholder_with_spaces", "placeholder2");
        assertEquals(expectedOutput, Answer.findPlaceholders(inputText));
    }
}