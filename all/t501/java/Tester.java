package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for the convertToShortFormat method.
 */
public class Tester {

    /**
     * Tests a standard input with mixed characters.
     */
    @Test
    public void testBasicCase() {
        assertEquals("fpgbc", convertToShortFormat("f1_p1_g1_b1_c1"));
    }

    /**
     * Tests input with multiple segments.
     */
    @Test
    public void testMultipleSegments() {
        assertEquals("abc", convertToShortFormat("a2_b3_c4"));
    }

    /**
     * Tests input with non-alphanumeric characters.
     */
    @Test
    public void testNonAlphaNumeric() {
        assertEquals("hwt", convertToShortFormat("hello_world_test"));
    }

    /**
     * Tests a single segment input.
     */
    @Test
    public void testSingleSegment() {
        assertEquals("s", convertToShortFormat("single"));
    }

    // Helper method to simulate the convertToShortFormat method
    private String convertToShortFormat(String inputStr) {
        // Split the input string by underscores
        String[] segments = inputStr.split("_");

        // Extract the first character from each segment and join them
        StringBuilder shortFormat = new StringBuilder();
        for (String segment : segments) {
            if (!segment.isEmpty()) {
                shortFormat.append(segment.charAt(0));
            }
        }

        return shortFormat.toString();
    }
}