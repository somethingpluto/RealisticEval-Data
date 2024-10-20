package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
/**
 * Test class for the splitIntoSentences method.
 */
public class Tester {

    /**
     * Tests splitting a basic text with clear punctuation.
     */
    @Test
    public void testBasicSplitting() {
        String text = "Hello world! How are you? I am fine.";
        List<String> expected = Arrays.asList("Hello world!", "How are you?", "I am fine.");
        List<String> result = splitIntoSentences(text);
        assertEquals(expected, result);
    }

    /**
     * Tests splitting text that includes quotes and commas.
     */
    @Test
    public void testComplexPunctuation() {
        String text = "He said, This is amazing! Then he left.";
        List<String> expected = Arrays.asList("He said, This is amazing!", "Then he left.");
        List<String> result = splitIntoSentences(text);
        assertEquals(expected, result);
    }

    /**
     * Tests text that has no punctuation marks.
     */
    @Test
    public void testWithNoPunctuation() {
        String text = "Hello world how are you";
        List<String> expected = Arrays.asList("Hello world how are you");
        List<String> result = splitIntoSentences(text);
        assertEquals(expected, result);
    }

    /**
     * Tests empty string input.
     */
    @Test
    public void testEmptyString() {
        String text = "";
        List<String> expected = Arrays.asList();
        List<String> result = splitIntoSentences(text);
        assertEquals(expected, result);
    }
}