package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Convert an array of binary bits to an array of bytes.
     * Traverse through each bit, compose these bits into bytes, form a byte every 8 bits,
     * store these bytes in an array and return it. If the length of the bit array is not a multiple of 8,
     * the last incomplete byte will be discarded.
     *
     * @param bits The input array of bits (each element should be 0 or 1).
     * @return An array of bytes constructed from the bits.
     */
    public static byte[] bitsToBytes(List<Integer> bits) {
        int size = bits.size();
        if (size == 0 || size % 8 != 0) {
            throw new IllegalArgumentException("The number of bits must be a positive multiple of 8.");
        }

        byte[] result = new byte[size / 8];
        for (int i = 0; i < size; i++) {
            int indexByte = i / 8;
            int positionInByte = i % 8;

            // Shift the current bit into its correct position within the byte.
            result[indexByte] |= (bits.get(i) << (7 - positionInByte));
        }

        return result;
    }

    // Example usage:
    public static void main(String[] args) {
        List<Integer> bits = new ArrayList<>();
        bits.add(1);
        bits.add(0);
        bits.add(1);
        bits.add(0);
        bits.add(1);
        bits.add(0);
        bits.add(1);
        bits.add(0);
        bits.add(0);
        bits.add(1);
        bits.add(0);
        bits.add(1);
        bits.add(0);
        bits.add(1);
        bits.add(0);

        byte[] bytes = bitsToBytes(bits);
        for (byte b : bytes) {
            System.out.printf("%02X ", b); // Print each byte in hexadecimal format
        }
    }
}