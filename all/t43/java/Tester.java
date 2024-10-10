package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testRgbToHsv() {
        // Test case 1
        assertEquals(new Integer[]{240, 100, 100}, rgbToHsv(0, 0, 255));

        // Add more test cases as needed
    }

    /**
     * Convert RGB color to HSV color.
     *
     * @param r The red component of the RGB color (0-255)
     * @param g The green component of the RGB color (0-255)
     * @param b The blue component of the RGB color (0-255)
     * @return An array containing the HSV values [hue, saturation, value]
     */
    private Integer[] rgbToHsv(int r, int g, int b) {
        double max = Math.max(r, Math.max(g, b));
        double min = Math.min(r, Math.min(g, b));
        double delta = max - min;

        int hue = 0;
        if (delta != 0) {
            if (max == r) {
                hue = (int) ((60 * ((g - b) / delta)) % 360);
            } else if (max == g) {
                hue = (int) (60 * ((b - r) / delta + 2));
            } else if (max == b) {
                hue = (int) (60 * ((r - g) / delta + 4));
            }
        }

        int saturation = (int) (max == 0 ? 0 : (delta / max) * 100);
        int value = (int) (max / 255 * 100);

        return new Integer[]{hue, saturation, value};
    }
}