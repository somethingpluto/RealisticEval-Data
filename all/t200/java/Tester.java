package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testBasicExtraction() {
        String input = "This is a sample text with some data {data: \"value\"} and more text.";
        String result = Answer.extractStringFromBraces(input);
        assertEquals("{data: \"value\"}", result);
    }

    @Test
    public void testNoBraces() {
        String input = "This string has no braces.";
        String result = Answer.extractStringFromBraces(input);
        assertEquals("No opening brace found.", result);
    }

    @Test
    public void testOnlyOpeningBrace() {
        String input = "This string has an opening brace { but no closing brace.";
        String result = Answer.extractStringFromBraces(input);
        assertEquals("No closing brace found.", result);
    }

    @Test
    public void testOnlyClosingBrace() {
        String input = "This string has a closing brace } but no opening brace.";
        String result = Answer.extractStringFromBraces(input);
        assertEquals("No opening brace found.", result);
    }

    @Test
    public void testMultipleBraces() {
        String input = "First {first} and second {second} braces.";
        String result = Answer.extractStringFromBraces(input);
        assertEquals("{first}", result);
    }

    @Test
    public void testEmptyBraces() {
        String input = "This string has empty braces {} and some text.";
        String result = Answer.extractStringFromBraces(input);
        assertEquals("{}", result);
    }
}