package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class Tester {

    @Test
    public void testConvertsBlack() {
        assertArrayEquals(new int[]{0, 0, 0}, ColorConverter.hslToRgb(0, 0, 0));
    }

    @Test
    public void testConvertsWhite() {
        assertArrayEquals(new int[]{255, 255, 255}, ColorConverter.hslToRgb(0, 0, 1));
    }

    @Test
    public void testConvertsRed() {
        assertArrayEquals(new int[]{255, 0, 0}, ColorConverter.hslToRgb(0, 1, 0.5));
    }

    @Test
    public void testConvertsGreen() {
        assertArrayEquals(new int[]{0, 255, 0}, ColorConverter.hslToRgb(120, 1, 0.5));
    }

    @Test
    public void testConvertsBlue() {
        assertArrayEquals(new int[]{0, 0, 255}, ColorConverter.hslToRgb(240, 1, 0.5));
    }

    @Test
    public void testHandlesEdgeCaseMaxHue() {
        assertArrayEquals(new int[]{255, 0, 0}, ColorConverter.hslToRgb(360, 1, 0.5));
    }
}