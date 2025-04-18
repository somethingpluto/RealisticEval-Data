package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {


    @Test
    public void testSingleLineContent() {
        List<String> result = wrapContentGenerator("Hello, world!", 80);
        assertEquals(result, List.of("Hello, world!"));
    }

    @Test
    public void testMultiLineContent() {
        String content = "Hello\nWorld\nPython";
        List<String> result = wrapContentGenerator(content, 80);
        assertEquals(result, List.of("Hello\n", "World\n", "Python"));
    }

    @Test
    public void testLongLine() {
        String content = "This is a very long line that should definitely be wrapped around the default width of 80 characters.";
        List<String> result = wrapContentGenerator(content, 80);
        assertTrue(result.stream().allMatch(line -> line.length() <= 80));
    }

    @Test
    public void testCustomWidth() {
        String content = "This is a test for custom width setting.";
        List<String> result = wrapContentGenerator(content, 10);
        assertTrue(result.stream().allMatch(line -> line.length() <= 10));
    }

    @Test
    public void testOnlyWhitespaces() {
        List<String> result = wrapContentGenerator("     ", 80);
        assertEquals(result, List.of("\n"));
    }
}