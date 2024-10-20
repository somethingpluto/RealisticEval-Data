package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    // Test rgbToHex function basic logic
    @Test
    public void testRgbToHex() {
        int[] rgb = {255, 99, 71};
        String result = rgbToHex(rgb);
        assertEquals("#ff6347", result); // Expected HEX code for RGB(255, 99, 71)
    }

    // Test hexToRgb function basic logic
    @Test
    public void testHexToRgb() {
        String hex = "#ff6347";
        int[] result = hexToRgb(hex);
        assertArrayEquals(new int[]{255, 99, 71}, result); // Expected RGB object for HEX #ff6347
    }
    // Test hexToRgb function for invalid HEX strings
    @Test
    public void testInvalidHexString() {
        String invalidHex = "#ggg123";
        int[] result = hexToRgb(invalidHex);
        assertNull(result); // Invalid HEX code should return null
    }

    // Test rgbToHex function boundary values
    @Test
    public void testBoundaryValuesInRgb() {
        int[] rgbBlack = {0, 0, 0};
        String resultBlack = rgbToHex(rgbBlack);
        assertEquals("#000000", resultBlack); // RGB(0, 0, 0) should convert to #000000

        int[] rgbWhite = {255, 255, 255};
        String resultWhite = rgbToHex(rgbWhite);
        assertEquals("#ffffff", resultWhite); // RGB(255, 255, 255) should convert to #ffffff
    }
}