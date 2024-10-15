package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testOriginalStringShorterThanMaxLength() {
        String input = "Short string";
        String result = StringCompressor.compressString(input);
        assertEquals(input, result);
    }

    @Test
    public void testOriginalStringEqualToMaxLength() {
        String input = "Exactly 18 chars";
        String result = StringCompressor.compressString(input);
        assertEquals(input, result);
    }

    @Test
    public void testTruncateStringExceedsMaxLength() {
        String input = "This is a long string that needs to be compressed.";
        String result = StringCompressor.compressString(input);
        assertEquals("This is a long ...", result);
    }

    @Test
    public void testTruncateWithSpecifiedMaxLength() {
        String input = "Another long string that is definitely too long.";
        String result = StringCompressor.compressString(input, 25);
        assertEquals("Another long string th...", result);
    }

    @Test
    public void testDefaultMaxLength() {
        String input = "This string is way too long.";
        String result = StringCompressor.compressString(input);
        assertEquals("This string is ...", result);
    }

    @Test
    public void testEmptyString() {
        String input = "";
        String result = StringCompressor.compressString(input);
        assertEquals(input, result);
    }
}