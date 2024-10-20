package org.real.temp;

import org.junit.Test;

import static junit.framework.TestCase.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Tests the edge case with an empty string.
     */
    @Test
    public void testEmptyString() {
        // Testing edge case with an empty string
        assertEquals("Should return an empty string", "", removeCommonIndentation(""));
    }

    /**
     * Tests a single line with no indentation.
     */
    @Test
    public void testSingleLineString() {
        // Testing a single line with no indentation
        assertEquals("Should return the same string as input", "No indentation here", removeCommonIndentation("No indentation here"));
    }

    /**
     * Tests basic logic with uniform indentation across multiple lines.
     */
    @Test
    public void testMultipleLinesWithUniformIndentation() {
        // Testing basic logic with uniform indentation across multiple lines
        String inputText = "    Line one\n    Line two\n    Line three";
        String expectedOutput = "Line one\nLine two\nLine three";
        assertEquals("Should remove common leading indentation", expectedOutput, removeCommonIndentation(inputText));
    }

    /**
     * Tests lines with mixed indentation levels.
     */
    @Test
    public void testMultipleLinesWithMixedIndentation() {
        // Testing lines with mixed indentation levels
        String inputText = "  Line one\n  Line two\n  Line three";
        String expectedOutput = "Line one\nLine two\nLine three";
        assertEquals("Should remove the minimum common indentation", expectedOutput, removeCommonIndentation(inputText));
    }
}