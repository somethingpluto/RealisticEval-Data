package org.real.temp;

import java.nio.ByteBuffer;

public class Answer {

    public static String convertDecimalToBinary(double decimalValue, int bitLength) {
        if (bitLength == 32) {
            // Convert the decimal to a 32-bit binary representation
            int packedValue = Float.floatToIntBits((float) decimalValue);
            String binaryRepresentation = Integer.toBinaryString(packedValue);
            return String.format("%32s", binaryRepresentation).replace(' ', '0');
        } else if (bitLength == 64) {
            // Convert the decimal to a 64-bit binary representation
            long packedValue = Double.doubleToLongBits(decimalValue);
            String binaryRepresentation = Long.toBinaryString(packedValue);
            return String.format("%64s", binaryRepresentation).replace(' ', '0');
        } else {
            throw new IllegalArgumentException("Invalid bit length. Please specify either 32 or 64.");
        }
    }
}