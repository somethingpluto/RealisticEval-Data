package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class Tester {

    @Test
    public void testBitsToBytes() {
        // Test data
        int[] bits = {1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0};
        byte[] expectedOutput = {(byte) 0xAA};

        // Call the method under test
        byte[] actualOutput = bitsToBytes(bits);

        // Verify the output
        assertArrayEquals(expectedOutput, actualOutput);
    }

    /**
     * Convert an array of binary bits to an array of bytes. Traversing through each bit,
     * composing these bits into bytes, forming a byte every 8 bits, and then storing
     * these bytes in an array and returning it. If the length of the bit array is not a
     * multiple of 8, the last incomplete byte will be discarded.
     *
     * @param bits The input array of bits (each element should be 0 or 1).
     * @return An array of bytes constructed from the bits.
     */
    public byte[] bitsToBytes(int[] bits) {
        if (bits == null || bits.length % 8 != 0) {
            return new byte[0];
        }

        int numBytes = bits.length / 8;
        byte[] bytes = new byte[numBytes];

        for (int i = 0; i < numBytes; i++) {
            int byteValue = 0;
            for (int j = 0; j < 8; j++) {
                byteValue = (byteValue << 1) | bits[i * 8 + j];
            }
            bytes[i] = (byte) byteValue;
        }

        return bytes;
    }
}