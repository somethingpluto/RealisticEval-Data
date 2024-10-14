package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testConvertsPureRedHueCorrectly() {
        RGB result = ColorConverter.hslToRgb(0, 100, 50);
        assertEquals(255, result.r);
        assertEquals(0, result.g);
        assertEquals(0, result.b);
    }

    @Test
    public void testReturnsGrayForZeroSaturation() {
        RGB result = ColorConverter.hslToRgb(240, 0, 50);
        assertEquals(128, result.r);
        assertEquals(128, result.g);
        assertEquals(128, result.b);
    }

    @Test
    public void testReturnsWhiteForFullLightness() {
        RGB result = ColorConverter.hslToRgb(120, 50, 100);
        assertEquals(255, result.r);
        assertEquals(255, result.g);
        assertEquals(255, result.b);
    }

    @Test
    public void testConvertsFullSaturationMidLightnessBlueCorrectly() {
        RGB result = ColorConverter.hslToRgb(240, 100, 50);
        assertEquals(0, result.r);
        assertEquals(0, result.g);
        assertEquals(255, result.b);
    }

    @Test
    public void testHandlesEdgeHueAt360DegreesCorrectly() {
        RGB result = ColorConverter.hslToRgb(360, 100, 50);
        assertEquals(255, result.r);
        assertEquals(0, result.g);
        assertEquals(0, result.b); // Should be the same as hue 0
    }
}