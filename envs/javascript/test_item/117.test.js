/**
 * Converts an RGB color value to HSL.
 *
 * @param {number} r - The red component (0-255).
 * @param {number} g - The green component (0-255).
 * @param {number} b - The blue component (0-255).
 * @returns {Object} An object containing the HSL values.
 */
function rgbToHsl(r, g, b) {
    // Normalize RGB values to the range [0, 1]
    r /= 255;
    g /= 255;
    b /= 255;

    // Find the maximum and minimum values among r, g, b
    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);

    // Calculate lightness
    let l = (max + min) / 2;

    // Calculate saturation and hue
    let h, s;
    if (max === min) {
        // Achromatic case (gray)
        h = 0;
        s = 0;
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
        }

        h /= 6;
    }

    // Convert h, s, l to the range [0, 1]
    h = Math.round(h * 360);
    s = Math.round(s * 100);
    l = Math.round(l * 100);

    return { h, s, l };
}
describe('rgbToHsl function', () => {
    test('converts pure red to HSL', () => {
        expect(rgbToHsl(255, 0, 0)).toEqual({h: 0, s: 100, l: 50});
    });

    test('converts black to HSL', () => {
        expect(rgbToHsl(0, 0, 0)).toEqual({h: 0, s: 0, l: 0});
    });

    test('converts white to HSL', () => {
        expect(rgbToHsl(255, 255, 255)).toEqual({h: 0, s: 0, l: 100});
    });

    test('converts a color on the edge of RGB range', () => {
        expect(rgbToHsl(0, 255, 255)).toEqual({h: 180, s: 100, l: 50});
    });
});
