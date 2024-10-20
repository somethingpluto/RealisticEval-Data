package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the moveEmojisToEnd function.
 */
public class Tester {

    /**
     * Tests the case where the input string contains no emojis.
     */
    @Test
    public void testNoEmojis() {
        String inputText = "This is a test.";
        String expectedOutput = "This is a test.";
        assertEquals(expectedOutput, moveEmojisToEnd(inputText));
    }

    /**
     * Tests the case where the input string contains only emojis.
     */
    @Test
    public void testAllEmojis() {
        String inputText = "😀😃😄😁";
        String expectedOutput = "😀😃😄😁";
        assertEquals(expectedOutput, moveEmojisToEnd(inputText));
    }

    /**
     * Tests the case where emojis are at the start of the text.
     */
    @Test
    public void testEmojisAtStart() {
        String inputText = "😀😃Hello world!";
        String expectedOutput = "Hello world!😀😃";
        assertEquals(expectedOutput, moveEmojisToEnd(inputText));
    }

    /**
     * Tests the case where emojis are already at the end of the text.
     */
    @Test
    public void testEmojisAtEnd() {
        String inputText = "Hello world!😀😃";
        String expectedOutput = "Hello world!😀😃";
        assertEquals(expectedOutput, moveEmojisToEnd(inputText));
    }

    /**
     * Tests the case where emojis are in the middle of the text.
     */
    @Test
    public void testEmojisInMiddle() {
        String inputText = "Hello 😀world😃!";
        String expectedOutput = "Hello world!😀😃";
        assertEquals(expectedOutput, moveEmojisToEnd(inputText));
    }

    /**
     * Tests the case where the input string contains mixed characters and emojis.
     */
    @Test
    public void testMixedCharacters() {
        String inputText = "Hi! 😀 How are you? 😃";
        String expectedOutput = "Hi!  How are you? 😀😃";
        assertEquals(expectedOutput, moveEmojisToEnd(inputText));
    }
}