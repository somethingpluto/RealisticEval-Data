package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testRgbToHsvRed() {
        // Test conversion of pure red color
        int r = 255, g = 0, b = 0;
        double[] expectedResult = {0, 100, 100}; // Hue should be 0, Saturation 100%, Value 100%
        double[] result = rgbToHsv(r, g, b);
        assertArrayEquals(expectedResult, result, 0.01); // Assert with a delta for floating point comparison
    }

    @Test
    public void testRgbToHsvGreen() {
        // Test conversion of pure green color
        int r = 0, g = 255, b = 0;
        double[] expectedResult = {120, 100, 100}; // Hue should be 120, Saturation 100%, Value 100%
        double[] result = rgbToHsv(r, g, b);
        assertArrayEquals(expectedResult, result, 0.01); // Assert with a delta for floating point comparison
    }

    @Test
    public void testRgbToHsvBlue() {
        // Test conversion of pure blue color
        int r = 0, g = 0, b = 255;
        double[] expectedResult = {240, 100, 100}; // Hue should be 240, Saturation 100%, Value 100%
        double[] result = rgbToHsv(r, g, b);
        assertArrayEquals(expectedResult, result, 0.01); // Assert with a delta for floating point comparison
    }

    @Test
    public void testRgbToHsvWhite() {
        // Test conversion of white color
        int r = 255, g = 255, b = 255;
        double[] expectedResult = {0, 0, 100}; // Hue is undefined, typically 0; Saturation 0%, Value 100%
        double[] result = rgbToHsv(r, g, b);
        assertArrayEquals(expectedResult, result, 0.01); // Assert with a delta for floating point comparison
    }

    @Test
    public void testRgbToHsvBlack() {
        // Test conversion of black color
        int r = 0, g = 0, b = 0;
        double[] expectedResult = {0, 0, 0}; // Hue is undefined, typically 0; Saturation 0%, Value 0%
        double[] result = rgbToHsv(r, g, b);
        assertArrayEquals(expectedResult, result, 0.01); // Assert with a delta for floating point comparison
    }
}
