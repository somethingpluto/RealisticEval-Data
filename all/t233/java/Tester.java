package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSingleLineComment() {
        // Test string with a comment on a single line
        String inputString = "Hello, world!# This is a comment";
        String expectedOutput = "Hello, world!";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testNoComments() {
        // Test string with no comments
        String inputString = "Hello, world!\nPython is fun!";
        String expectedOutput = "Hello, world!\nPython is fun!";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testEmptyString() {
        // Test an empty string
        String inputString = "";
        String expectedOutput = "";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testCommentsOnly() {
        // Test string where all lines are comments
        String inputString = "# comment only line\n#another comment line";
        String expectedOutput = "\n";
        assertEquals(expectedOutput, removeComments(inputString));
    }
}