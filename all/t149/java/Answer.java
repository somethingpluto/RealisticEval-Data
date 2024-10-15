public class ColorConverter {

    /**
     * Converts an HSL color value to RGB.
     * Assumes hue is in the range [0, 360] and
     * saturation and lightness are in the range [0, 1].
     *
     * @param hue The hue of the color (0-360)
     * @param saturation The saturation of the color (0-1)
     * @param lightness The lightness of the color (0-1)
     * @return An array containing the red, green, and blue channels.
     */
    public static int[] hslToRgb(double hue, double saturation, double lightness) {
        double r, g, b;

        if (saturation == 0) {
            // Achromatic case
            r = g = b = lightness; // all equal to lightness
        } else {
            double q = lightness < 0.5 ? lightness * (1 + saturation) : lightness + saturation - lightness * saturation;
            double p = 2 * lightness - q;

            r = hueToRgb(p, q, hue / 360 + 1.0 / 3.0);
            g = hueToRgb(p, q, hue / 360);
            b = hueToRgb(p, q, hue / 360 - 1.0 / 3.0);
        }

        return new int[]{(int) Math.round(r * 255), (int) Math.round(g * 255), (int) Math.round(b * 255)};
    }

    private static double hueToRgb(double p, double q, double t) {
        if (t < 0) t += 1;
        if (t > 1) t -= 1;
        if (t < 1.0 / 6.0) return p + (q - p) * 6 * t;
        if (t < 0.5) return q;
        if (t < 2.0 / 3.0) return p + (q - p) * (2.0 / 3.0 - t) * 6;
        return p;
    }
}