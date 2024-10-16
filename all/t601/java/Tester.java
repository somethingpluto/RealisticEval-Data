package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Tester {

    @Test
    public void testCountWordsInVariousStrings() {
        // Empty string
        assertEquals(0, Answer.countWords(""));

        // String with only spaces
        assertEquals(0, Answer.countWords("     "));

        // Single word
        assertEquals(1, Answer.countWords("Hello"));

        // Multiple words with single spaces
        assertEquals(5, Answer.countWords("This is a test string"));

        // Multiple spaces between words
        assertEquals(5, Answer.countWords("This    is   a   test   string"));

        // Leading and trailing spaces
        assertEquals(2, Answer.countWords("   Hello world!   "));
    }
}