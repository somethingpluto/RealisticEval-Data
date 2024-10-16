package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    private List<String> result;

    @Before
    public void setUp() {
        result = new ArrayList<>();
    }

    @Test
    public void testBasicCommaSeparatedValues() {
        Answer.splitComma("apple,banana,orange", result);
        assertEquals(3, result.size());
        assertEquals("apple", result.get(0));
        assertEquals("banana", result.get(1));
        assertEquals("orange", result.get(2));
    }

    @Test
    public void testLeadingAndTrailingWhitespace() {
        Answer.splitComma("  apple , banana , orange  ", result);
        assertEquals(3, result.size());
        assertEquals("apple", result.get(0));
        assertEquals("banana", result.get(1));
        assertEquals("orange", result.get(2));
    }

    @Test
    public void testMultipleConsecutiveCommas() {
        Answer.splitComma("apple,,banana,,,orange", result);
        assertEquals(3, result.size());
        assertEquals("apple", result.get(0));
        assertEquals("banana", result.get(1));
        assertEquals("orange", result.get(2));
    }

    @Test
    public void testEmptyInputString() {
        Answer.splitComma("", result);
        assertEquals(0, result.size());
    }

    @Test
    public void testOnlyWhitespaceInput() {
        Answer.splitComma("   ", result);
        assertEquals(0, result.size());
    }

    @Test
    public void testTrailingCommas() {
        Answer.splitComma("apple,banana,orange,", result);
        assertEquals(3, result.size());
        assertEquals("apple", result.get(0));
        assertEquals("banana", result.get(1));
        assertEquals("orange", result.get(2));
    }
}