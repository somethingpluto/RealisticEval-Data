package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.real.temp.Answer;
/**
 * Test class for the Colors utility class.
 */
public class Tester {

    @Test
    public void testRed() {
        String inputText = "Hello";
        String expectedOutput = "\033[91mHello\033[0m";
        assertEquals("Test the red color method", expectedOutput, Answer.red(inputText));
    }

    @Test
    public void testGreen() {
        String inputText = "Hello";
        String expectedOutput = "\033[92mHello\033[0m";
        assertEquals("Test the green color method", expectedOutput, Answer.green(inputText));
    }

    @Test
    public void testBlue() {
        String inputText = "Hello";
        String expectedOutput = "\033[94mHello\033[0m";
        assertEquals("Test the blue color method", expectedOutput, Answer.blue(inputText));
    }

    @Test
    public void testYellow() {
        String inputText = "Hello";
        String expectedOutput = "\033[93mHello\033[0m";
        assertEquals("Test the yellow color method", expectedOutput, Answer.yellow(inputText));
    }

    @Test
    public void testMagenta() {
        String inputText = "Hello";
        String expectedOutput = "\033[95mHello\033[0m";
        assertEquals("Test the magenta color method", expectedOutput, Answer.magenta(inputText));
    }

    @Test
    public void testCyan() {
        String inputText = "Hello";
        String expectedOutput = "\033[96mHello\033[0m";
        assertEquals("Test the cyan color method", expectedOutput, Answer.cyan(inputText));
    }

    @Test
    public void testCombinedColors() {
        String inputTextRed = Answer.red("Red");
        String inputTextBlue = Answer.blue("Blue");
        String inputTextCombined = inputTextRed + " and " + inputTextBlue;
        String expectedOutput = "\033[91mRed\033[0m and \033[94mBlue\033[0m";
        assertEquals("Test combining different color methods", expectedOutput, inputTextCombined);
    }
}