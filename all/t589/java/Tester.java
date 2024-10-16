package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testExtractJsonReturnsEmptyStringForInputWithoutBrace() {
        String input = "No braces here";
        assertEquals("", Answer.extractJson(input));
    }

    @Test
    public void testExtractJsonExtractsSingleJsonObject() {
        String input = "Here is some text before { \"key\": \"value\" } and some text after.";
        assertEquals("{ \"key\": \"value\" }", Answer.extractJson(input));
    }

    @Test
    public void testExtractJsonHandlesNestedJsonObjects() {
        String input = "Some text { \"outer\": { \"inner\": \"value\" } } more text.";
        assertEquals("{ \"outer\": { \"inner\": \"value\" } }", Answer.extractJson(input));
    }

    @Test
    public void testExtractJsonReturnsEmptyStringForUnmatchedBraces() {
        String input = "Here is an incomplete JSON { \"key\": \"value\" ";
        assertEquals("", Answer.extractJson(input));
    }

    @Test
    public void testExtractJsonReturnsCorrectJsonWhenMultipleBracesPresent() {
        String input = "Start { { \"key\": \"value\" } and some other text { \"another\": \"object\" }} end.";
        assertEquals("{ { \"key\": \"value\" } and some other text { \"another\": \"object\" }}", Answer.extractJson(input));
    }

    @Test
    public void testExtractJsonExtractsFirstJsonObjectWhenMultiplePresent() {
        String input = "Text before { \"first\": \"value1\" } text in between { \"second\": \"value2\" }";
        assertEquals("{ \"first\": \"value1\" }", Answer.extractJson(input));
    }
}