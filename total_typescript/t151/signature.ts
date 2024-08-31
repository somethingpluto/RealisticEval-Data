/**
 * Converts RGB color values to HSL (Hue, Saturation, Lightness) color values.
 * The input RGB values should be in the range of 0 to 255, and the output HSL values will have:
 * - `h` (Hue) in the range of 0 to 360,
 * - `s` (Saturation) in the range of 0 to 100 (percentage),
 * - `l` (Lightness) in the range of 0 to 100 (percentage).
 *
 * @param {Object} rgb - The RGB color values.
 * @param {number} rgb.r - The red color value (0-255).
 * @param {number} rgb.g - The green color value (0-255).
 * @param {number} rgb.b - The blue color value (0-255).
 * @returns {Object} An object representing the HSL color values.
 * @returns {number} h - The hue value (0-360).
 * @returns {number} s - The saturation value (0-100).
 * @returns {number} l - The lightness value (0-100).
 */
export function rgbToHsl({ r, g, b }: { r: number; g: number; b: number }): { h: number; s: number; l: number } {

}