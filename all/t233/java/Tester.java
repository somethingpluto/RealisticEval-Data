package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {
    @Test
    public void testSingleLineComment() {
        String inputString = "Hello, world!# This is a comment";
        String expectedOutput = "Hello, world!";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testNoComments() {
        String inputString = "Hello, world!\nPython is fun!";
        String expectedOutput = "Hello, world!\nPython is fun!";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testEmptyString() {
        String inputString = "";
        String expectedOutput = "";
        assertEquals(expectedOutput, removeComments(inputString));
    }

    @Test
    public void testCommentsOnly() {
        String inputString = "# comment only line\n#another comment line";
        String expectedOutput = "\n"; // Result should include a newline since lines are comments only
        assertEquals(expectedOutput, removeComments(inputString));
    }
}
