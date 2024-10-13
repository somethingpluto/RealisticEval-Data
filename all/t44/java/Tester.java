package org.real.temp;

import org.junit.jupiter.api.Test; // Updated import for JUnit 5 Test annotation
import static org.junit.jupiter.api.Assertions.assertEquals; // Updated import for assertEquals in JUnit 5


/**
 * Test class for aligning strings to the left.
 */
public class Tester {

    /**
     * Tests aligning strings of equal length.
     */
    @Test
    public void testEqualLengthStrings() {
        String str1 = "Hello";
        String str2 = "World";
        String expectedStr1 = "Hello";
        String expectedStr2 = "World";
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }

    /**
     * Tests aligning strings where the first string is longer.
     */
    @Test
    public void testFirstStringLonger() {
        String str1 = "Hello, World!";
        String str2 = "Hi";
        String expectedStr1 = "Hello, World!";
        String expectedStr2 = "Hi           ";  // 14 spaces after "Hi"
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }

    /**
     * Tests aligning strings where the second string is longer.
     */
    @Test
    public void testSecondStringLonger() {
        String str1 = "Hey";
        String str2 = "Goodbye, friend!";
        String expectedStr1 = "Hey             ";  // 15 spaces after "Hey"
        String expectedStr2 = "Goodbye, friend!";
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }

    /**
     * Tests aligning strings where the first string is empty.
     */
    @Test
    public void testEmptyFirstString() {
        String str1 = "";
        String str2 = "World";
        String expectedStr1 = "     ";  // 5 spaces
        String expectedStr2 = "World";
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }

    /**
     * Tests aligning strings where the second string is empty.
     */
    @Test
    public void testEmptySecondString() {
        String str1 = "Hello";
        String str2 = "";
        String expectedStr1 = "Hello";
        String expectedStr2 = "     ";  // 5 spaces
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }

    /**
     * Tests aligning strings where both strings are empty.
     */
    @Test
    public void testBothStringsEmpty() {
        String str1 = "";
        String str2 = "";
        String expectedStr1 = "";
        String expectedStr2 = "";
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }

    /**
     * Tests aligning strings with trailing spaces.
     */
    @Test
    public void testStringsWithSpaces() {
        String str1 = "Hello ";
        String str2 = "World  ";
        String expectedStr1 = "Hello  ";
        String expectedStr2 = "World  ";
        String[] alignedStrings = alignLinesLeft(str1, str2);
        assertEquals(expectedStr1, alignedStrings[0]);
        assertEquals(expectedStr2, alignedStrings[1]);
    }
}