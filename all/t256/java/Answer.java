package org.real.temp;

import java.util.List;

public class Answer {

    /**
     * Convert an array of binary bits to an array of bytes. Every 8 bits are converted
     * into one byte. If the length of the bit array is not a multiple of 8, the last
     * incomplete byte will be discarded.
     *
     * @param bits The input array of bits (each element should be 0 or 1).
     * @return A byte array constructed from the bits.
     */
    public static byte[] bitsToBytes(List<Integer> bits) {
        // Ensure that the number of bits is a multiple of 8
        int numFullBytes = bits.size() / 8;

        // Create a byte array to store the byte values
        byte[] byteArray = new byte[numFullBytes];

        // Process each group of 8 bits
        for (int i = 0; i < numFullBytes; i++) {
            // Slice the bits list to get 8 bits
            List<Integer> byteBits = bits.subList(i * 8, (i + 1) * 8);
            // Convert the list of bits to a string of bits
            StringBuilder byteStrBuilder = new StringBuilder();
            for (Integer bit : byteBits) {
                byteStrBuilder.append(bit);
            }
            String byteStr = byteStrBuilder.toString();
            // Convert the string of bits to an integer and then to a byte
            int byteValue = Integer.parseInt(byteStr, 2);
            // Append the byte to the byte array
            byteArray[i] = (byte) byteValue;
        }

        return byteArray;
    }

    public static void main(String[] args) {
        // Example usage
        List<Integer> bits = List.of(1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0);
        byte[] byteArray = bitsToBytes(bits);
        for (byte b : byteArray) {
            System.out.printf("%d ", b);
        }
    }
}