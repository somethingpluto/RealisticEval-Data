package org.real.temp;

import org.junit.Test;
import java.util.Arrays;
import java.util.List;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSplitStringRegularSentence() {
        String input = "Hello world from Catch2";
        List<String> expected = Arrays.asList("Hello", "world", "from", "Catch2");
        assertEquals(expected, splitString(input));
    }

    @Test
    public void testSplitStringMultipleSpaces() {
        String input = "Multiple   spaces between words";
        List<String> expected = Arrays.asList("Multiple", "spaces", "between", "words");
        assertEquals(expected, splitString(input));
    }

    @Test
    public void testSplitStringSingleWord() {
        String input = "Single";
        List<String> expected = Arrays.asList("Single");
        assertEquals(expected, splitString(input));
    }

    @Test
    public void testSplitStringEmpty() {
        String input = "";
        List<String> expected = Arrays.asList();
        assertEquals(expected, splitString(input));
    }

    @Test
    public void testSplitStringLeadingTrailingSpaces() {
        String input = "   Leading and trailing spaces   ";
        List<String> expected = Arrays.asList("Leading", "and", "trailing", "spaces");
        assertEquals(expected, splitString(input));
    }
}