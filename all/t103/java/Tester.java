package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testOriginalStringShorterThanMaxLength() {
        String result = truncateStringWithReplacement("Hello World", 20);
        assertEquals("Hello World", result);
    }


    @Test
    public void testHandleEmptyString() {
        String result = truncateStringWithReplacement("", 10);
        assertEquals("", result);
    }

    @Test
    public void testOriginalStringEqualToMaxLength() {
        String result = truncateStringWithReplacement("Exact length", 12);
        assertEquals("Exact length", result);
    }


    @Test
    public void testMaxLengthZeroReturnsEllipsis() {
        String result = truncateStringWithReplacement("Hello, world!", 0);
        assertEquals("...", result);
    }
}