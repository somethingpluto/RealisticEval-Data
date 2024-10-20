package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSingleCodeBlock() {
        String markdown = "This is a markdown with a code block.\n\n```python\nprint(\"Hello, World!\")\n```\n\nEnd of markdown.";
        List<String> expected = Arrays.asList("print(\"Hello, World!\")");
        List<String> result = codeBlockRemover(markdown);
        assertEquals(expected, result);
    }

    @Test
    public void testMultipleCodeBlocks() {
        String markdown = "First code block:\n\n```python\nprint(\"Hello, World!\")\n```\n\nSecond code block:\n\n```javascript\nconsole.log(\"Hello, World!\");\n```\n";
        List<String> expected = Arrays.asList(
            "print(\"Hello, World!\")",
            "console.log(\"Hello, World!\");"
        );
        List<String> result = codeBlockRemover(markdown);
        assertEquals(expected, result);
    }

    @Test
    public void testNoCodeBlock() {
        String markdown = "This markdown has no code blocks.\n\nJust some plain text.";
        List<String> expected = Arrays.asList();
        List<String> result = codeBlockRemover(markdown);
        assertEquals(expected, result);
    }

    @Test
    public void testEmptyCodeBlock() {
        String markdown = "Here is an empty code block:\n\n```python\n```\n\nEnd of markdown.";
        List<String> expected = Arrays.asList("");
        List<String> result = codeBlockRemover(markdown);
        assertEquals(expected, result);
    }

    @Test
    public void testMalformedCodeBlock() {
        String markdown = "This code block is missing ending:\n\n```python\nprint(\"Hello, World!\")\n\nAnd some more text.";
        List<String> expected = Arrays.asList();
        List<String> result = codeBlockRemover(markdown);
        assertEquals(expected, result);
    }
}