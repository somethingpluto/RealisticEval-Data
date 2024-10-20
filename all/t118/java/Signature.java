/**
 * Converts HSL color values to RGB.
 *
 * @param h - Hue (0-360 degrees).
 * @param s - Saturation (0-100%).
 * @param l - Lightness (0-100%).
 * @returns An RGB object containing the RGB values.
 */
public static class RGB {
    public int r, g, b;

    public RGB(int r, int g, int b) {
        this.r = r;
        this.g = g;
        this.b = b;
    }
}
public static RGB hslToRgb(double h, double s, double l) {
}