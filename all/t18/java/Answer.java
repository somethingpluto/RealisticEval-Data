package org.real.temp;

public class Answer {

    /**
     * Convert a floating point number between 0 and 1 to a color from red to green in the color format RGB.
     *
     * @param value A float between 0 and 1.
     * @return A tuple representing the RGB color.
     */
    public static int[] floatToRGB(float value) {
        // Check if the input value is within the valid range
        if (value < 0 || value > 1) {
            throw new IllegalArgumentException("Value must be between 0 and 1");
        }

        // Calculate the RGB values based on the input value
        int r = (int)(255 * (1 - value));
        int g = (int)(255 * value);
        int b = 0; // Blue channel is always 0

        return new int[]{r, g, b};
    }
}