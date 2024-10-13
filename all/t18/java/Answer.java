package org.real.temp;

public class Answer {

    /**
     * Converts a floating-point number between 0 and 1 to a color from red to green in RGB format.
     * 
     * @param value A float between 0 and 1.
     * @return An array representing the RGB color.
     * @throws IllegalArgumentException If the value is not between 0 and 1 inclusive.
     */
    public static int[] floatToRGB(float value) {
        if (value < 0.0f || value > 1.0f) {
            throw new IllegalArgumentException("Value must be between 0 and 1 inclusive.");
        }

        // Calculate the red and green components
        int red = (int) ((1.0f - value) * 255);
        int green = (int) (value * 255);

        // Blue component is always 0 for the red-to-green gradient
        int blue = 0;

        return new int[]{red, green, blue};
    }

    public static void main(String[] args) {
        // Example usage
        try {
            int[] rgbColor = floatToRGB(0.5f);
            System.out.println("RGB Color: (" + rgbColor[0] + ", " + rgbColor[1] + ", " + rgbColor[2] + ")");
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}