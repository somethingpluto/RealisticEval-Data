package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testRgbToHslPureRed() {
        assertArrayEquals(new int[]{0, 100, 50}, rgbToHsl(255, 0, 0));
    }

    @Test
    public void testRgbToHslBlack() {
        assertArrayEquals(new int[]{0, 0, 0}, rgbToHsl(0, 0, 0));
    }

    @Test
    public void testRgbToHslWhite() {
        assertArrayEquals(new int[]{0, 0, 100}, rgbToHsl(255, 255, 255));
    }

    @Test
    public void testRgbToHslCyan() {
        assertArrayEquals(new int[]{180, 100, 50}, rgbToHsl(0, 255, 255));
    }
}