/**
 * Converts an RGB color value to HSL.
 *
 * @param {number} r - The red component (0-255).
 * @param {number} g - The green component (0-255).
 * @param {number} b - The blue component (0-255).
 * @returns {Object} An object containing the HSL values.
 */
function rgbToHsl(r, g, b) {
    // Make r, g, and b fractions of 1
    r /= 255;
    g /= 255;
    b /= 255;

    // Find the minimum and maximum values of r, g, and b
    const min = Math.min(r, g, b);
    const max = Math.max(r, g, b);
    const delta = max - min;

    // Calculate hue
    let h;
    if (delta === 0) {
        h = 0;
    } else if (max === r) {
        h = ((g - b) / delta) % 6;
    } else if (max === g) {
        h = (b - r) / delta + 2;
    } else {
        h = (r - g) / delta + 4;
    }
    h *= 60;

    // Calculate lightness
    const l = (max + min) / 2;

    // Calculate saturation
    let s;
    if (delta === 0) {
        s = 0;
    } else {
        s = delta / (1 - Math.abs(2 * l - 1));
    }

    // Return the HSL values
    return {
        h: Math.round(h),
        s: Math.round(s * 100),
        l: Math.round(l * 100)
    };
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
