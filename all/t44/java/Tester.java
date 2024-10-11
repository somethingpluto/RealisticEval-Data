package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testAlignLinesLeft() {
        // Test case 1: Both strings have equal length
        String result1 = alignLinesLeft("hello", "world");
        assertEquals("hello world", result1);

        // Test case 2: First string is longer than second string
        String result2 = alignLinesLeft("hello", "hi");
        assertEquals("hello hi   ", result2);

        // Test case 3: Second string is longer than first string
        String result3 = alignLinesLeft("hi", "hello");
        assertEquals("hi   hello", result3);

        // Test case 4: Both strings are empty
        String result4 = alignLinesLeft("", "");
        assertEquals("       ", result4);

        // Test case 5: One string is empty and the other has content
        String result5 = alignLinesLeft("hello", "");
        assertEquals("hello      ", result5);
    }

    private String alignLinesLeft(String str1, String str2) {
        int maxLength = Math.max(str1.length(), str2.length());
        return String.format("%-" + maxLength + "s %-" + maxLength + "s", str1, str2).replaceAll("\\s+$", "");
    }
}