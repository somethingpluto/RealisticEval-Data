/**
 * Converts a hue value to its corresponding RGB color values.
 *
 * @param {number} hue - A float representing the hue angle in degrees,
 *                       expected to be in the range [0, 360).
 *
 * @return {Array<number>} An array containing three integers representing the
 *                         RGB color components in the range [0, 255]. The
 *                         first element is the red component, the second
 *                         element is the green component, and the third element
 *                         is the blue component.
 */
function hueToRGB(hue: number): [number, number, number] {
    // Ensure hue is in the range [0, 360)
    hue = hue % 360;

    const c = 255; // Chroma (max RGB value)
    const x = c * (1 - Math.abs((hue / 60) % 2 - 1));
    const m = 0;

    let r: number, g: number, b: number;

    if (hue >= 0 && hue < 60) {
        r = c; g = x; b = m;
    } else if (hue >= 60 && hue < 120) {
        r = x; g = c; b = m;
    } else if (hue >= 120 && hue < 180) {
        r = m; g = c; b = x;
    } else if (hue >= 180 && hue < 240) {
        r = m; g = x; b = c;
    } else if (hue >= 240 && hue < 300) {
        r = x; g = m; b = c;
    } else {
        r = c; g = m; b = x;
    }

    // Convert to the range [0, 255]
    return [Math.round(r + m), Math.round(g + m), Math.round(b + m)];
}