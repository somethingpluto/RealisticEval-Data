package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    /**
     * Test the byteCountToDisplaySize function with various inputs.
     */

    @Test
    public void testZeroBytes() {
        // Test case for 0 bytes
        long input = 0L;
        String expected = "0 bytes";
        assertEquals(expected, Answer.byteCountToDisplaySize(input));
    }

    @Test
    public void testBytesLessThanKB() {
        // Test case for bytes less than 1KB
        long input = 500L;
        String expected = "500 bytes";
        assertEquals(expected, Answer.byteCountToDisplaySize(input));
    }

    @Test
    public void testExactlyOneKB() {
        // Test case for exactly 1KB
        long input = 1024L;
        String expected = "1 KB";
        assertEquals(expected, Answer.byteCountToDisplaySize(input));
    }

    @Test
    public void testBetweenKBAndMB() {
        // Test case for a size between 1KB and 1MB
        long input = 5000L;
        String expected = "4.88 KB";
        assertEquals(expected, Answer.byteCountToDisplaySize(input));
    }

    @Test
    public void testExactlyOneMB() {
        // Test case for exactly 1MB
        long input = 1048576L; // 1024 * 1024
        String expected = "1 MB";
        assertEquals(expected, Answer.byteCountToDisplaySize(input));
    }

    @Test
    public void testLargeSize() {
        // Test case for a large size (1TB)
        long input = 1099511627776L; // 1024 * 1024 * 1024 * 1024
        String expected = "1 TB";
        assertEquals(expected, Answer.byteCountToDisplaySize(input));
    }
}