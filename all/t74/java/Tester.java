package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testBasic32BitConversion() {
        assertEquals("3.14 should be correctly converted to 32-bit binary",
                "01000000010010001111010111000011",
                convertDecimalToBinary(3.14, 32));
    }

    @Test
    public void testBasic64BitConversion() {
        assertEquals("3.14 should be correctly converted to 64-bit binary",
                "0100000000001001000111101011100001010001111010111000010100011111",
                convertDecimalToBinary(3.14, 64));
    }

    @Test
    public void testAdvance32BitConversion() {
        assertEquals("1.5 should be correctly converted to 32-bit binary",
                "00111111110000000000000000000000",
                convertDecimalToBinary(1.5, 32));
    }

    @Test
    public void testAdvance64BitConversion() {
        assertEquals("1.5 should be correctly converted to 64-bit binary",
                "0011111111111000000000000000000000000000000000000000000000000000",
                convertDecimalToBinary(1.5, 64));
    }
}
