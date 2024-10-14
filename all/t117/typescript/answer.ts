/**
 * Converts an RGB color value to HSL.
 *
 * @param {number} r - The red component (0-255).
 * @param {number} g - The green component (0-255).
 * @param {number} b - The blue component (0-255).
 * @returns {{ h: number; s: number; l: number }} An object containing the HSL values.
 */
function rgbToHsl(r: number, g: number, b: number): { h: number; s: number; l: number } {
    // Convert RGB to the [0, 1] range.
    r /= 255;
    g /= 255;
    b /= 255;

    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    let h: number, s: number, l: number = (max + min) / 2;

    if (max === min) {
        h = s = 0; // achromatic
    } else {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

        switch (max) {
            case r:
                h = (g - b) / d + (g < b ? 6 : 0);
                break;
            case g:
                h = (b - r) / d + 2;
                break;
            case b:
                h = (r - g) / d + 4;
                break;
            default:
                h = 0; // This case should never occur.
        }

        h /= 6;
    }

    // Convert hue to degrees
    h = Math.round(h * 360);
    // Convert saturation and lightness to percentage
    s = Math.round(s * 100);
    l = Math.round(l * 100);

    return { h, s, l };
}