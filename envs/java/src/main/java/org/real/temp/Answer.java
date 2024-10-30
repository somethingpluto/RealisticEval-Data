package org.real.temp;

import java.util.List;
import java.util.Arrays;

public class Answer {

    /**
     * Calculate the proportion of red in a list of pixels.
     *
     * @param pixels A list of pixels, where each pixel is represented as an array of [R, G, B].
     * @return The proportion of red in the list of pixels, as a value between 0 and 1.
     */
    public static double calculateRedProportion(List<int[]> pixels) {
        if (pixels.isEmpty()) {
            return 0.0;
        }

        int totalRed = 0;
        int totalIntensity = 0;

        for (int[] pixel : pixels) {
            int r = pixel[0];
            int g = pixel[1];
            int b = pixel[2];

            totalRed += r;
            totalIntensity += (r + g + b);
        }

        // Avoid division by zero
        if (totalIntensity == 0) {
            return 0.0;
        }

        double redProportion = (double) totalRed / totalIntensity;
        return redProportion;
    }

    public static void main(String[] args) {
        List<int[]> pixels = Arrays.asList(
                new int[]{255, 0, 0}, // Red
                new int[]{0, 255, 0}, // Green
                new int[]{0, 0, 255}, // Blue
                new int[]{255, 255, 255} // White
        );

        double result = calculateRedProportion(pixels);
        System.out.println("Red Proportion: " + result);
    }
}