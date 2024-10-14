package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testRemovesPunctuationFromSimpleSentence() {
        String input = "Hello, world!";
        String expected = "hello world";
        assertEquals(expected, StringCleaner.removePunctuation(input));
    }

    @Test
    public void testHandlesStringWithNoPunctuation() {
        String input = "Hello world";
        String expected = "hello world";
        assertEquals(expected, StringCleaner.removePunctuation(input));
    }

    @Test
    public void testConvertsMixedCaseLettersToLowercase() {
        String input = "HeLLo WoRLd!";
        String expected = "hello world";
        assertEquals(expected, StringCleaner.removePunctuation(input));
    }

    @Test
    public void testRemovesVarietyOfPunctuation() {
        String input = "Life, in a nutshell: eat, sleep, code!";
        String expected = "life in a nutshell eat sleep code";
        assertEquals(expected, StringCleaner.removePunctuation(input));
    }

    @Test
    public void testTrimsWhitespaceFromEndsOfString() {
        String input = "   What a wonderful world!   ";
        String expected = "what a wonderful world";
        assertEquals(expected, StringCleaner.removePunctuation(input));
    }
}