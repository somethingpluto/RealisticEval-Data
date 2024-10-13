package org.real.temp;

public class Answer {

    /**
     * Converts RGB color values to HSV (Hue, Saturation, Value).
     * 
     * @param r The red component of the color (0-255).
     * @param g The green component of the color (0-255).
     * @param b The blue component of the color (0-255).
     * @return A tuple containing the HSV values (Hue, Saturation, Value).
     */
    public static Tuple rgbToHsv(int r, int g, int b) {
        // Normalize the RGB values by dividing by 255
        double rNorm = r / 255.0;
        double gNorm = g / 255.0;
        double bNorm = b / 255.0;

        // Find the minimum and maximum values among R, G, and B
        double maxRgb = Math.max(rNorm, Math.max(gNorm, bNorm));
        double minRgb = Math.min(rNorm, Math.min(gNorm, bNorm));
        double delta = maxRgb - minRgb;

        // Calculate H (Hue)
        double h = 0;
        if (delta == 0) {
            h = 0;
        } else if (maxRgb == rNorm) {
            h = ((gNorm - bNorm) / delta) % 6;
        } else if (maxRgb == gNorm) {
            h = ((bNorm - rNorm) / delta) + 2;
        } else {
            h = ((rNorm - gNorm) / delta) + 4;
        }

        h *= 60;  // Convert to degrees on the color circle

        // Calculate S (Saturation)
        double s = 0;
        if (maxRgb == 0) {
            s = 0;
        } else {
            s = delta / maxRgb;
        }

        // V (Value) is equal to max_rgb
        double v = maxRgb;

        return new Tuple(h, s * 100, v * 100);
    }

    // A simple Tuple class to hold the HSV values
    public static class Tuple {
        private final double hue;
        private final double saturation;
        private final double value;

        public Tuple(double hue, double saturation, double value) {
            this.hue = hue;
            this.saturation = saturation;
            this.value = value;
        }

        @Override
        public String toString() {
            return "(" + hue + ", " + saturation + ", " + value + ")";
        }
    }

    public static void main(String[] args) {
        // Example usage
        Tuple hsv = rgbToHsv(255, 0, 0); // Red color
        System.out.println(hsv);
    }
}