package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.real.temp.Answer;

public class Tester {

    @Test
    public void testRgbToHsvRed() {
        // Test conversion of pure red color
        int r = 255, g = 0, b = 0;
        Tuple<Double, Double, Double> expectedResult = new Answer.Tuple<>(0.0, 100.0, 100.0);
        Tuple<Double, Double, Double> result = Answer.rgbToHsv(r, g, b);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testRgbToHsvGreen() {
        // Test conversion of pure green color
        int r = 0, g = 255, b = 0;
        Tuple<Double, Double, Double> expectedResult = new Answer.Tuple<>(120.0, 100.0, 100.0);
        Tuple<Double, Double, Double> result = Answer.rgbToHsv(r, g, b);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testRgbToHsvBlue() {
        // Test conversion of pure blue color
        int r = 0, g = 0, b = 255;
        Tuple<Double, Double, Double> expectedResult = new Answer.Tuple<>(240.0, 100.0, 100.0);
        Tuple<Double, Double, Double> result = Answer.rgbToHsv(r, g, b);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testRgbToHsvWhite() {
        // Test conversion of white color
        int r = 255, g = 255, b = 255;
        Tuple<Double, Double, Double> expectedResult = new Answer.Tuple<>(0.0, 0.0, 100.0);
        Tuple<Double, Double, Double> result = Answer.rgbToHsv(r, g, b);
        assertEquals(expectedResult, result);
    }

    @Test
    public void testRgbToHsvBlack() {
        // Test conversion of black color
        int r = 0, g = 0, b = 0;
        Tuple<Double, Double, Double> expectedResult = new Answer.Tuple<>(0.0, 0.0, 0.0);
        Tuple<Double, Double, Double> result = Answer.rgbToHsv(r, g, b);
        assertEquals(expectedResult, result);
    }
}
