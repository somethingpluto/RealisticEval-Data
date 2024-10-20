/**
 * Converts RGB color values to HSL (Hue, Saturation, Lightness) color values.
 * The input RGB values should be in the range of 0 to 255, and the output HSL values will have:
 * - `h` (Hue) in the range of 0 to 360,
 * - `s` (Saturation) in the range of 0 to 100 (percentage),
 * - `l` (Lightness) in the range of 0 to 100 (percentage).
 *
 * @param r The red color value (0-255).
 * @param g The green color value (0-255).
 * @param b The blue color value (0-255).
 * @return An HSL object representing the HSL color values.
 * @return.h The hue value (0-360).
 * @return.s The saturation value (0-100).
 * @return.l The lightness value (0-100).
 */
public static class HSL {
    public int h;
    public int s;
    public int l;

    public HSL(int h, int s, int l) {
        this.h = h;
        this.s = s;
        this.l = l;
    }
}
public static HSL rgbToHsl(int r, int g, int b) {}