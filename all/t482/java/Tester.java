package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for the extractOutermostBrackets method.
 */
public class Tester {

    /**
     * Tests extracting content from single parentheses.
     */
    @Test
    public void testSingleParentheses() {
        assertEquals("example", extractOutermostBrackets("Text (example) more text"));
    }

    /**
     * Tests extracting content from nested curly brackets.
     */
    @Test
    public void testNestedBrackets() {
        assertEquals("with some {nested} brackets", extractOuterMostBrackets("Text {with some {nested} brackets}"));
    }

    /**
     * Tests extracting content from square brackets.
     */
    @Test
    public void testSquareBrackets() {
        assertEquals("with [nested] brackets", extractOuterMostBrackets("Text [with [nested] brackets] and more text"));
    }

    /**
     * Tests extracting content from mixed bracket types.
     */
    @Test
    public void testMixedBracketTypes() {
        assertEquals("types {of brackets [in use]}", extractOuterMostBrackets("Mixed (types {of brackets [in use]})"));
    }

    /**
     * Tests extracting content when there are no brackets.
     */
    @Test
    public void testNoBrackets() {
        assertEquals("", extractOuterMostBrackets("No brackets here"));
    }
}