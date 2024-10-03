package com.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {
    @Test
    void testNormalHexString() {
        String hex = "1a3f";
        byte[] expected = { (byte) 0x1A, (byte) 0x3F };
        assertArrayEquals(expected, Answer.hexStringToByteArray(hex), "Should correctly convert a normal hex string");
    }

    @Test
    void testOddLengthHexString() {
        String hex = "123";
        byte[] expected = { (byte) 0x01, (byte) 0x23 };
        assertArrayEquals(expected, Answer.hexStringToByteArray(hex), "Should handle odd-length hex strings by prepending zero");
    }

    @Test
    void testEmptyString() {
        String hex = "";
        byte[] expected = new byte[0];
        assertArrayEquals(expected, Answer.hexStringToByteArray(hex), "Should return an empty array for an empty string");
    }

    @Test
    void testHexStringWithUppercase() {
        String hex = "1A3F";
        byte[] expected = { (byte) 0x1A, (byte) 0x3F };
        assertArrayEquals(expected, Answer.hexStringToByteArray(hex), "Should correctly handle hex strings with uppercase letters");
    }

    @Test
    void testInvalidHexString() {
        String hex = "1A3G"; // 'G' is not a valid hex character
        assertThrows(NumberFormatException.class, () -> Answer.hexStringToByteArray(hex), "Should throw NumberFormatException for non-hex characters");
    }
}
