package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.real.temp.*;

public class Tester {
    @Test
    public void testSimpleParagraph() {
        String html = "<p>This is a test.</p>";
        String expected = "This is a test.\n\n";
        assertEquals(expected, Answer.convert(html));
    }

    @Test
    public void testComplexNestedTags() {
        String html = "<p>This is <strong>bold and <em>italic</em></strong> text.</p>";
        String expected = "This is **bold and *italic*** text.\n\n";
        assertEquals(expected, Answer.convert(html));
    }

    @Test
    public void testLinks() {
        String html = "<p>Check out this <a href='http://example.com'>link</a>.</p>";
        String expected = "Check out this <a href='http://example.com'>link</a>.\n\n";
        assertEquals(expected, Answer.convert(html));
    }

    @Test
    public void testListItems() {
        String html = "<ul><li>Item 1</li><li>Item 2</li></ul>";
        String expected = "* Item 1\n* Item 2\n";
        assertEquals(expected, Answer.convert(html));
    }

    @Test
    public void testEmptyString() {
        String html = "";
        String expected = "";
        assertEquals(expected, Answer.convert(html));
    }
}
