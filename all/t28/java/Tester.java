package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testPrintMemoryBitsSingleByte() {
        byte[] memorySection = {0b10101010};
        String expectedOutput = "10101010";
        assertEquals(expectedOutput, printMemoryBits(memorySection));
    }

    @Test
    public void testPrintMemoryBitsMultipleBytes() {
        byte[] memorySection = {0b11001100, 0b11110000};
        String expectedOutput = "11001100\n11110000";
        assertEquals(expectedOutput, printMemoryBits(memorySection));
    }

    @Test
    public void testPrintMemoryBitsEmptyArray() {
        byte[] memorySection = {};
        String expectedOutput = "";
        assertEquals(expectedOutput, printMemoryBits(memorySection));
    }

    @Test
    public void testPrintMemoryBitsNullInput() {
        assertThrows(NullPointerException.class, () -> printMemoryBits(null));
    }

    private String printMemoryBits(byte[] memorySection) {
        if (memorySection == null) {
            throw new NullPointerException("Memory section cannot be null");
        }

        StringBuilder result = new StringBuilder();
        for (byte b : memorySection) {
            result.append(String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0'));
            if (result.length() > 8) {
                result.append('\n');
            }
        }
        return result.toString().trim();
    }
}