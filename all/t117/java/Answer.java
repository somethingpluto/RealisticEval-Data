package org.real.temp;

public class Answer {

    /**
     * Converts an RGB color value to HSL.
     *
     * @param r The red component (0-255).
     * @param g The green component (0-255).
     * @param b The blue component (0-255).
     * @return An array containing the HSL values.
     */
    public static int[] rgbToHsl(int r, int g, int b) {
        // Convert RGB to the [0, 1] range.
        double rNorm = r / 255.0;
        double gNorm = g / 255.0;
        double bNorm = b / 255.0;

        double max = Math.max(rNorm, Math.max(gNorm, bNorm));
        double min = Math.min(rNorm, Math.min(gNorm, bNorm));
        double h, s, l = (max + min) / 2;

        if (max == min) {
            h = s = 0; // achromatic
        } else {
            double d = max - min;
            s = (l > 0.5) ? d / (2 - max - min) : d / (max + min);

            switch ((int) (max * 255)) {
                case 255: // r is max
                    h = (gNorm - bNorm) / d + (gNorm < bNorm ? 6 : 0);
                    break;
                case 255 * 2: // g is max
                    h = (bNorm - rNorm) / d + 2;
                    break;
                case 255 * 3: // b is max
                    h = (rNorm - gNorm) / d + 4;
                    break;
                default:
                    h = 0;
            }

            h /= 6;
        }

        // Convert hue to degrees
        h = Math.round(h * 360);
        // Convert saturation and lightness to percentage
        s = Math.round(s * 100);
        l = Math.round(l * 100);

        return new int[] { (int) h, (int) s, (int) l };
    }

    public static void main(String[] args) {
        int r = 255; // Example red value
        int g = 0;   // Example green value
        int b = 0;   // Example blue value

        int[] hsl = rgbToHsl(r, g, b);
        System.out.printf("HSL: (%d, %d%%, %d%%)%n", hsl[0], hsl[1], hsl[2]);
    }
}