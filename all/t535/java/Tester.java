package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testRemoveNewlinesAndTabs() {
        String input = "\n            <div>\n                <p>Test paragraph.</p>\n            </div>\n        ";
        String expectedOutput = "<div><p>Test paragraph.</p></div>";
        assertEquals(expectedOutput, Answer.compressHtml(input));
    }

    @Test
    public void testReplaceMultipleSpaces() {
        String input = "<div>    <p>     Test with     multiple spaces.   </p></div>";
        String expectedOutput = "<div><p> Test with multiple spaces. </p></div>";
        assertEquals(expectedOutput, Answer.compressHtml(input));
    }

    @Test
    public void testRemoveSpacesBetweenTags() {
        String input = "<div> <p>Test</p> </div>";
        String expectedOutput = "<div><p>Test</p></div>";
        assertEquals(expectedOutput, Answer.compressHtml(input));
    }

    @Test
    public void testHandleEmptyInput() {
        String input = "";
        String expectedOutput = "";
        assertEquals(expectedOutput, Answer.compressHtml(input));
    }

    @Test
    public void testHandleSpacesAndNewlines() {
        String input = "\n            <div>      \n            </div>\n        ";
        String expectedOutput = "<div></div>";
        assertEquals(expectedOutput, Answer.compressHtml(input));
    }
}