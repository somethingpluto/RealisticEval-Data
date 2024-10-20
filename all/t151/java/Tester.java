package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testRgbToHslRed() {
        HSL result = rgbToHsl(255, 0, 0);
        assertEquals(0, result.h);
        assertEquals(100, result.s);
        assertEquals(50, result.l);
    }

    @Test
    public void testRgbToHslMiddleGray() {
        HSL result = rgbToHsl(128, 128, 128);
        assertEquals(0, result.h);
        assertEquals(0, result.s);
        assertEquals(50, result.l);
    }

    @Test
    public void testRgbToHslWhite() {
        HSL result = rgbToHsl(255, 255, 255);
        assertEquals(0, result.h);
        assertEquals(0, result.s);
        assertEquals(100, result.l);
    }

    @Test
    public void testRgbToHslBlack() {
        HSL result = rgbToHsl(0, 0, 0);
        assertEquals(0, result.h);
        assertEquals(0, result.s);
        assertEquals(0, result.l);
    }

    @Test
    public void testRgbToHslVibrantGreen() {
        HSL result = rgbToHsl(0, 255, 0);
        assertEquals(120, result.h);
        assertEquals(100, result.s);
        assertEquals(50, result.l);
    }

    @Test
    public void testRgbToHslDeepBlue() {
        HSL result = rgbToHsl(0, 0, 255);
        assertEquals(240, result.h);
        assertEquals(100, result.s);
        assertEquals(50, result.l);
    }
}