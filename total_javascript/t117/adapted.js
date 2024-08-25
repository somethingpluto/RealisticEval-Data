/**
 * Converts an RGB color value to HSL.
 *
 * @param {number} r - The red color value (0-255)
 * @param {number} g - The green color value (0-255)
 * @param {number} b - The blue color value (0-255)
 * @returns {Object} An object containing the HSL values
 */
function rgbToHsl(r, g, b) {
    // Convert RGB values to the range 0-1
    r /= 255;
    g /= 255;
    b /= 255;

    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
        h = s = 0; // achromatic
    } else {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }

    return {
        h: Math.round(h * 360),
        s: Math.round(s * 100),
        l: Math.round(l * 100)
    };
}