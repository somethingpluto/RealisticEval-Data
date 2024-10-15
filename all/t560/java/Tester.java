package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testGetLineNumber_FirstCharacter() {
        assertEquals(1, getLineNumber("Line 1\nLine 2\nLine 3", 0));
    }

    @Test
    public void testGetLineNumber_LastCharacterOfFirstLine() {
        assertEquals(1, getLineNumber("Line 1\nLine 2\nLine 3", 5));
    }

    @Test
    public void testGetLineNumber_LastCharacterOfThirdLine() {
        assertEquals(3, getLineNumber("Line 1\nLine 2\nLine 3", 18));
    }

    @Test
    public void testGetLineNumber_SingleLineString() {
        assertEquals(1, getLineNumber("Single line string", 0));
    }

    @Test
    public void testGetLineNumber_MultilineStringWithTrailingNewlines() {
        assertEquals(3, getLineNumber("Line 1\nLine 2\nLine 3\n\n", 15));
    }
}