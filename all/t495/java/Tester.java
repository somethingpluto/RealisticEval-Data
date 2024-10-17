package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testSingleKeywordMatch() {
        String content = "Line one.\n" +
                         "This line contains a keyword.\n" +
                         "Line three.";
        List<String> keywords = Arrays.asList("keyword");
        String expectedOutput = "Line one.\n" +
                                "This line contains a keyword.\n" +
                                "Line three.";
        String result = Answer.filterContentWithContext(content, keywords, 1, 1);
        assertEquals(expectedOutput.strip(), result.strip(), "Failed to filter content for a single keyword.");
    }

    @Test
    public void testNoKeywordMatch() {
        String content = "Line one.\n" +
                         "Line two.\n" +
                         "Line three.";
        List<String> keywords = Arrays.asList("missing");
        String expectedOutput = "";
        String result = Answer.filterContentWithContext(content, keywords, 1, 1);
        assertEquals(expectedOutput.strip(), result.strip(), "Failed to return empty string for no matches.");
    }

    @Test
    public void testLinesBeforeAndAfter() {
        String content = "Line one.\n" +
                         "This line contains a keyword.\n" +
                         "Line three.\n" +
                         "Line four.\n" +
                         "Line five.";
        List<String> keywords = Arrays.asList("keyword");
        String expectedOutput = "Line one.\n" +
                                "This line contains a keyword.\n" +
                                "Line three.";
        String result = Answer.filterContentWithContext(content, keywords, 1, 1);
        assertEquals(expectedOutput.strip(), result.strip(), "Failed to correctly include context lines.");
    }
}