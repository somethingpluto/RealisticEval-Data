package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testRemoveLeadingAndTrailingSpacesAroundTags() {
        String input = "  <div>  <p>Test</p>  </div>  ";
        String expected = "<div><p>Test</p></div>";
        assertEquals(expected, compressHTML(input));
    }

    @Test
    public void testReplaceMultipleNewlinesWithSingleSpace() {
        String input = "<div>\n\n<p>Test</p>\n\n</div>";
        String expected = "<div> <p>Test</p> </div>";
        assertEquals(expected, compressHTML(input));
    }

    @Test
    public void testRemoveUnnecessarySpacesWithinText() {
        String input = "<p>This    is a test</p>";
        String expected = "<p>This is a test</p>";
        assertEquals(expected, compressHTML(input));
    }

    @Test
    public void testHandleEmptyStrings() {
        String input = "";
        String expected = "";
        assertEquals(expected, compressHTML(input));
    }

    @Test
    public void testProcessComplexNestedHTMLCorrectly() {
        String input = "<div>   <span>    Text <i>    Italic </i> more text </span>   </div>";
        String expected = "<div><span>Text <i>Italic</i> more text</span></div>";
        assertEquals(expected, compressHTML(input));
    }

    @Test
    public void testDoNotDisruptContentWithinPreAndTextareaTags() {
        String input = "<pre>\n    function example() {\n        console.log(\"example\");\n    }\n</pre>";
        String expected = "<pre>\n    function example() {\n        console.log(\"example\");\n    }\n</pre>"; // assuming no changes in <pre> and <textarea>
        assertEquals(expected, compressHTML(input));
    }

    @Test
    public void testHandleHTMLWithAttributesCorrectly() {
        String input = "<a href=\"http://example.com\"    title=\"Example\" >Link</a>";
        String expected = "<a href=\"http://example.com\" title=\"Example\">Link</a>";
        assertEquals(expected, compressHTML(input));
    }
}