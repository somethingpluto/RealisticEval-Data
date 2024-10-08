package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.real.temp.*;

public class Tester {

    @Test
    public void testSimpleLineBreak() {
        String input = "Hello<br>World";
        String expectedOutput = "Hello\nWorld";
        assertEquals(expectedOutput, Answer.convert(input));
    }


    @Test
    public void testStrongTags() {
        String input = "This is <strong>important</strong> text.";
        String expectedOutput = "This is **important** text.";
        assertEquals(expectedOutput, Answer.convert(input));
    }

    @Test
    public void testEmphasisTags() {
        String input = "This is <em>emphasized</em> text.";
        String expectedOutput = "This is *emphasized* text.";
        assertEquals(expectedOutput, Answer.convert(input));
    }

    @Test
    public void testUnorderedList() {
        String input = "<ul><li>Item 1</li><li>Item 2</li></ul>";
        String expectedOutput = "* Item 1\n* Item 2";
        assertEquals(expectedOutput, Answer.convert(input));
    }

    @Test
    public void testAnchorTags() {
        String input = "Check this link: <a href=\"http://example.com\">Example</a>.";
        String expectedOutput = "Check this link: [Example](http://example.com).";
        assertEquals(expectedOutput, Answer.convert(input));
    }
}
