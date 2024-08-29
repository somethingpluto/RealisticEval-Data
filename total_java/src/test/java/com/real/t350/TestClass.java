package com.real.t350;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestClass {
    @Test
    void testEmptyByteArray() {
        byte[] input = new byte[0];
        assertEquals("", Adapted.byteArrayToHexString(input), "Empty array should return empty string");
    }

    @Test
    void testSingleByte() {
        byte[] input = {0x0F}; // 15 in decimal
        assertEquals("0F", Adapted.byteArrayToHexString(input), "Single byte array should return correct hex string");
    }

    @Test
    void testMultipleBytes() {
        byte[] input = {0x01, 0x0A, (byte) 0xFF};
        assertEquals("010AFF", Adapted.byteArrayToHexString(input), "Multiple bytes should be converted to correct hex string");
    }

    @Test
    void testZeroBytes() {
        byte[] input = {0x00, 0x00, 0x00};
        assertEquals("000000", Adapted.byteArrayToHexString(input), "Zero bytes should be converted to '000000'");
    }

    @Test
    void testNegativeBytes() {
        byte[] input = {(byte) 0x80, (byte) 0xFF}; // 128 and 255 in signed byte representation
        assertEquals("80FF", Adapted.byteArrayToHexString(input), "Negative bytes should be treated as unsigned and converted correctly");
    }
}
