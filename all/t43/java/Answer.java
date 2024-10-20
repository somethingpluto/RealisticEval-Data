package org.real.temp;

public class Answer {

    public static double[] rgbToHsv(int r, int g, int b) {
        // Normalize the RGB values by dividing by 255
        double rNorm = r / 255.0;
        double gNorm = g / 255.0;
        double bNorm = b / 255.0;

        // Find the minimum and maximum values among R, G, and B
        double maxRgb = Math.max(rNorm, Math.max(gNorm, bNorm));
        double minRgb = Math.min(rNorm, Math.min(gNorm, bNorm));
        double delta = maxRgb - minRgb;

        // Initialize H, S, V
        double h = 0;
        double s = 0;
        double v = maxRgb;

        // Calculate H (Hue)
        if (delta != 0) {
            if (maxRgb == rNorm) {
                h = ((gNorm - bNorm) / delta) % 6;
            } else if (maxRgb == gNorm) {
                h = ((bNorm - rNorm) / delta) + 2;
            } else {
                h = ((rNorm - gNorm) / delta) + 4;
            }

            h *= 60; // Convert to degrees on the color circle
            if (h < 0) {
                h += 360; // Make sure H is positive
            }
        }

        // Calculate S (Saturation)
        if (maxRgb != 0) {
            s = delta / maxRgb;
        }

        // Scale S and V to be percentages
        s *= 100;
        v *= 100;

        return new double[]{h, s, v};
    }

    public static void main(String[] args) {
        // Example usage
        int r = 255;
        int g = 0;
        int b = 0;

        double[] hsv = rgbToHsv(r, g, b);
        System.out.printf("H: %.2f, S: %.2f%%, V: %.2f%%\n", hsv[0], hsv[1], hsv[2]);
    }
}
