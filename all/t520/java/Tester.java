package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for the computeOutputIndex method.
 */
public class Tester {

    /**
     * Tests the computeOutputIndex method with two standard positive integers.
     */
    @Test
    public void testStandardCase() {
        int idx1 = 3;  // binary: 11
        int idx2 = 5;  // binary: 101
        int expected = 6;  // 3 XOR 5 = 6
        int result = computeOutputIndex(idx1, idx2);
        assertEquals(expected, result);
    }

    /**
     * Tests the computeOutputIndex method with identical indices (should return 0).
     */
    @Test
    public void testIdenticalIndices() {
        int idx1 = 7;  // binary: 111
        int idx2 = 7;  // binary: 111
        int expected = 0;  // 7 XOR 7 = 0
        int result = computeOutputIndex(idx1, idx2);
        assertEquals(expected, result);
    }

    /**
     * Tests the computeOutputIndex method with one index as zero.
     */
    @Test
    public void testZeroIndex() {
        int idx1 = 0;  // binary: 0
        int idx2 = 5;  // binary: 101
        int expected = 5;  // 0 XOR 5 = 5
        int result = computeOutputIndex(idx1, idx2);
        assertEquals(expected, result);
    }

    /**
     * Tests the computeOutputIndex method with large integer values.
     */
    @Test
    public void testLargeNumbers() {
        int idx1 = 1024;  // binary: 10000000000
        int idx2 = 2048;  // binary: 100000000000
        int expected = 3072;  // 1024 XOR 2048 = 3072
        int result = computeOutputIndex(idx1, idx2);
        assertEquals(expected, result);
    }

    // Utility method to compute the output index
    private int computeOutputIndex(int idx1, int idx2) {
        // Perform bitwise XOR between the two indices
        int result = idx1 ^ idx2;

        // Convert result to little-endian byte representation
        byte[] resultBytes = intToLittleEndianBytes(result);

        // Convert little-endian bytes back to an integer
        int resultInt = littleEndianBytesToInt(resultBytes);

        return resultInt;
    }

    // Helper method to convert an integer to a little-endian byte array
    private byte[] intToLittleEndianBytes(int value) {
        byte[] bytes = new byte[4];
        for (int i = 0; i < 4; i++) {
            bytes[i] = (byte) (value & 0xFF);
            value >>>= 8;
        }
        return bytes;
    }

    // Helper method to convert a little-endian byte array back to an integer
    private int littleEndianBytesToInt(byte[] bytes) {
        int result = 0;
        for (int i = 0; i < bytes.length; i++) {
            result |= (bytes[i] & 0xFF) << (i * 8);
        }
        return result;
    }
}