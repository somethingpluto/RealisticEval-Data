package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class Tester {

    @Test
    public void testRgbToHslPureRed() {
        assertArrayEquals(new int[]{0, 100, 50}, ColorConverter.rgbToHsl(255, 0, 0));
    }

    @Test
    public void testRgbToHslBlack() {
        assertArrayEquals(new int[]{0, 0, 0}, ColorConverter.rgbToHsl(0, 0, 0));
    }

    @Test
    public void testRgbToHslWhite() {
        assertArrayEquals(new int[]{0, 0, 100}, ColorConverter.rgbToHsl(255, 255, 255));
    }

    @Test
    public void testRgbToHslCyan() {
        assertArrayEquals(new int[]{180, 100, 50}, ColorConverter.rgbToHsl(0, 255, 255));
    }
}