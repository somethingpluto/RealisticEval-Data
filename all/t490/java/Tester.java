package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the formatStr method.
 */
public class Tester {

    /**
     * Tests a simple string input.
     */
    @Test
    public void testSimpleString() {
        String inputStr = "Hello, World!";
        String expectedOutput = "> Hello, World!";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests a multiline string input.
     */
    @Test
    public void testMultilineString() {
        String inputStr = "Line 1\nLine 2\nLine 3";
        String expectedOutput = "> Line 1\n> Line 2\n> Line 3";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests a string with an even number of code block delimiters.
     */
    @Test
    public void testCodeBlockDelimitersEven() {
        String inputStr = "Some code:\n```\nprint('Hello')\n```";
        String expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests a string with an odd number of code block delimiters.
     */
    @Test
    public void testCodeBlockDelimitersOdd() {
        String inputStr = "Some code:\n```\nprint('Hello')";
        String expectedOutput = "> Some code:\n> ```\n> print('Hello')\n> ```";
        assertEquals(expectedOutput, formatStr(inputStr));
    }

    /**
     * Tests non-string input (e.g., integer) to ensure it's converted.
     */
    @Test
    public void testNonStringInput() {
        Object inputValue = 123;
        String expectedOutput = "> 123";
        assertEquals(expectedOutput, formatStr(inputValue));
    }
}