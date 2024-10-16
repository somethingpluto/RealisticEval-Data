package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class Tester {

    @Test
    public void testHueToRGB_Hue0_Red() {
        int[] rgb = Answer.hueToRGB(0);
        assertArrayEquals(new int[] {255, 0, 0}, rgb);
    }

    @Test
    public void testHueToRGB_Hue120_Green() {
        int[] rgb = Answer.hueToRGB(120);
        assertArrayEquals(new int[] {0, 255, 0}, rgb);
    }

    @Test
    public void testHueToRGB_Hue240_Blue() {
        int[] rgb = Answer.hueToRGB(240);
        assertArrayEquals(new int[] {0, 0, 255}, rgb);
    }

    @Test
    public void testHueToRGB_Hue60_Yellow() {
        int[] rgb = Answer.hueToRGB(60);
        assertArrayEquals(new int[] {255, 255, 0}, rgb);
    }

    @Test
    public void testHueToRGB_Hue180_Cyan() {
        int[] rgb = Answer.hueToRGB(180);
        assertArrayEquals(new int[] {0, 255, 255}, rgb);
    }

    @Test
    public void testHueToRGB_Hue300_Magenta() {
        int[] rgb = Answer.hueToRGB(300);
        assertArrayEquals(new int[] {255, 0, 255}, rgb);
    }
}