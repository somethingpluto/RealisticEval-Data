package org.real.temp;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class Tester {
    @Test
    void testEmptyByteArray() {
        byte[] input = new byte[0];
        assertEquals("", Answer.byteArrayToHexString(input), "Empty array should return empty string");
    }

    @Test
    void testSingleByte() {
        byte[] input = {0x0F}; // 15 in decimal
        String result = Answer.byteArrayToHexString(input);
        assertTrue(result.equals("0F") || result.equals("0f"));
    }

    @Test
    void testMultipleBytes() {
        byte[] input = {0x01, 0x0A, (byte) 0xFF};
        String result = Answer.byteArrayToHexString(input);
        assertTrue(result.equals("010aff") || result.equals("010AFF"));
    }

    @Test
    void testZeroBytes() {
        byte[] input = {0x00, 0x00, 0x00};
        assertEquals("000000", Answer.byteArrayToHexString(input), "Zero bytes should be converted to '000000'");
    }

    @Test
    void testNegativeBytes() {
        byte[] input = {(byte) 0x80, (byte) 0xFF}; // 128 and 255 in signed byte representation
        String result = Answer.byteArrayToHexString(input);
        assertTrue(result.equals("80FF") || result.equals("80ff"));
    }
}
