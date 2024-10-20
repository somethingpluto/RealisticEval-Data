package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.real.temp.Answer;
/**
 * Test class for the calculateRedProportion method.
 */
public class Tester {

    /**
     * Test case for all fully red pixels.
     */
    @Test
    public void testAllRedPixels() {
        List<int[]> pixels = Arrays.asList(
                new int[]{255, 0, 0},
                new int[]{255, 0, 0},
                new int[]{255, 0, 0}
        );
        double result = Answer.calculateRedProportion(pixels);
        assertEquals(1.0, result, 0.001);
    }

    /**
     * Test case for no red component in any pixel.
     */
    @Test
    public void testNoRedPixels() {
        List<int[]> pixels = Arrays.asList(
                new int[]{0, 255, 0},
                new int[]{0, 0, 255},
                new int[]{0, 255, 255}
        );
        double result = Answer.calculateRedProportion(pixels);
        assertEquals(0.0, result, 0.001);
    }

    /**
     * Test case for an empty list of pixels.
     */
    @Test
    public void testEmptyPixelList() {
        List<int[]> pixels = new ArrayList<>();
        double result = Answer.calculateRedProportion(pixels);
        assertEquals(0.0, result, 0.001);
    }

    /**
     * Test case for all black pixels.
     */
    @Test
    public void testAllBlackPixels() {
        List<int[]> pixels = Arrays.asList(
                new int[]{0, 0, 0},
                new int[]{0, 0, 0},
                new int[]{0, 0, 0}
        );
        double result = Answer.calculateRedProportion(pixels);
        assertEquals(0.0, result, 0.001);
    }
}
