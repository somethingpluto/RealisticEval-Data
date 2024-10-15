/**
 * Converts RGB color values to HSL (Hue, Saturation, Lightness) color values.
 * The input RGB values should be in the range of 0 to 255, and the output HSL values will have:
 * - `h` (Hue) in the range of 0 to 360,
 * - `s` (Saturation) in the range of 0 to 100 (percentage),
 * - `l` (Lightness) in the range of 0 to 100 (percentage).
 *
 * @param rgb - The RGB color values.
 * @param rgb.r - The red color value (0-255).
 * @param rgb.g - The green color value (0-255).
 * @param rgb.b - The blue color value (0-255).
 * @returns An object representing the HSL color values.
 * @returns h - The hue value (0-360).
 * @returns s - The saturation value (0-100).
 * @returns l - The lightness value (0-100).
 */
HSL rgbToHsl(const RGB& rgb);