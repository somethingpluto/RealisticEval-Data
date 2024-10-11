package org.real.temp;

public class Answer {

    public static int[] rgbToHsv(int r, int g, int b) {
        // Convert RGB values to float between 0 and 1
        float rf = r / 255f;
        float gf = g / 255f;
        float bf = b / 255f;

        // Find the maximum and minimum of RGB values
        float max = Math.max(Math.max(rf, gf), bf);
        float min = Math.min(Math.min(rf, gf), bf);

        // Calculate the hue
        float h = 0;
        if (max == min) {
            h = 0; // No saturation
        } else if (max == rf) {
            h = 60 * ((gf - bf) / (max - min));
        } else if (max == gf) {
            h = 60 * ((bf - rf) / (max - min)) + 120;
        } else { // max == bf
            h = 60 * ((rf - gf) / (max - min)) + 240;
        }

        // Normalize hue to be within [0, 360)
        if (h < 0) {
            h += 360;
        }

        // Calculate the saturation
        float s = (max == 0) ? 0 : (1 - (min / max));

        // Calculate the value
        float v = max;

        // Return the result as an array
        return new int[]{(int)h, (int)(s*100), (int)(v*100)};
    }
}