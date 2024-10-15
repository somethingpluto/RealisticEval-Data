package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testConvertH1ToMarkdown() {
        String input = "<h1>This is a Heading 1</h1>";
        String output = "# This is a Heading 1";
        assertEquals(output, HtmlToMarkdownConverter.convertHtmlHeadingsToMarkdown(input));
    }

    @Test
    public void testConvertH2ToMarkdown() {
        String input = "<h2>This is a Heading 2</h2>";
        String output = "## This is a Heading 2";
        assertEquals(output, HtmlToMarkdownConverter.convertHtmlHeadingsToMarkdown(input));
    }

    @Test
    public void testConvertH3ToMarkdown() {
        String input = "<h3>This is a Heading 3</h3>";
        String output = "### This is a Heading 3";
        assertEquals(output, HtmlToMarkdownConverter.convertHtmlHeadingsToMarkdown(input));
    }

    @Test
    public void testConvertH4ToMarkdown() {
        String input = "<h4>This is a Heading 4</h4>";
        String output = "#### This is a Heading 4";
        assertEquals(output, HtmlToMarkdownConverter.convertHtmlHeadingsToMarkdown(input));
    }

    @Test
    public void testConvertH5ToMarkdown() {
        String input = "<h5>This is a Heading 5</h5>";
        String output = "##### This is a Heading 5";
        assertEquals(output, HtmlToMarkdownConverter.convertHtmlHeadingsToMarkdown(input));
    }

    @Test
    public void testConvertH6ToMarkdown() {
        String input = "<h6>This is a Heading 6</h6>";
        String output = "###### This is a Heading 6";
        assertEquals(output, HtmlToMarkdownConverter.convertHtmlHeadingsToMarkdown(input));
    }
}