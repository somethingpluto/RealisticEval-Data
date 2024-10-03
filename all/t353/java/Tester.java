package org.real.temp;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.real.temp.Answer.*;

public class Tester {
    @Test
    public void testEmptyArray() {
        byte[] emptyArray = {};
        String result = Answer.bytesToHex(emptyArray);
        assertEquals("", result, "Empty array should return an empty string");
    }

    @Test
    public void testSingleByte() {
        byte[] singleByte = {0x0F};
        String result = Answer.bytesToHex(singleByte);
        assertEquals("0f", result, "Single byte 0x0F should return '0f'");
    }

    @Test
    public void testMultipleBytes() {
        byte[] byteArray = {0x01, 0x2A, (byte) 0xFF, 0x4C};
        String result = Answer.bytesToHex(byteArray);
        assertEquals("012aff4c", result, "Array {0x01, 0x2A, 0xFF, 0x4C} should return '012aff4c'");
    }

    @Test
    public void testLeadingZeroes() {
        byte[] byteArray = {0x00, 0x01, 0x0A};
        String result = Answer.bytesToHex(byteArray);
        assertEquals("00010a", result, "Array {0x00, 0x01, 0x0A} should return '00010a'");
    }

    @Test
    public void testAllPossibleBytes() {
        byte[] byteArray = {0x00, 0x7F, (byte) 0x80, (byte) 0xFF};
        String result = Answer.bytesToHex(byteArray);
        assertEquals("007f80ff", result, "Array {0x00, 0x7F, 0x80, 0xFF} should return '007f80ff'");
    }
}
