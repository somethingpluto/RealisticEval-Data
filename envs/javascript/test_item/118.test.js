/**
 * Converts HSL color values to RGB.
 *
 * @param {number} h - Hue (0-360 degrees).
 * @param {number} s - Saturation (0-100%).
 * @param {number} l - Lightness (0-100%).
 * @returns {Object} An object containing the RGB values.
 */
function hslToRgb(h, s, l) {
    // Normalize the input values
    h = h % 360;
    s = Math.max(0, Math.min(100, s)) / 100;
    l = Math.max(0, Math.min(100, l)) / 100;

    let r, g, b;

    if (s === 0) {
        // Achromatic (gray)
        r = g = b = l;
    } else {
        const hueToRgb = (p, q, t) => {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1 / 6) return p + (q - p) * 6 * t;
            if (t < 1 / 2) return q;
            if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
            return p;
        };

        const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        const p = 2 * l - q;

        r = hueToRgb(p, q, h / 360 + 1 / 3);
        g = hueToRgb(p, q, h / 360);
        b = hueToRgb(p, q, h / 360 - 1 / 3);
    }

    // Convert to 8-bit RGB values
    r = Math.round(r * 255);
    g = Math.round(g * 255);
    b = Math.round(b * 255);

    return { r, g, b };
}
describe('hslToRgb function', () => {
    test('converts pure red hue correctly', () => {
        expect(hslToRgb(0, 100, 50)).toEqual({ r: 255, g: 0, b: 0 });
    });

    test('returns gray for zero saturation', () => {
        expect(hslToRgb(240, 0, 50)).toEqual({ r: 128, g: 128, b: 128 });
    });

    test('returns white for full lightness', () => {
        expect(hslToRgb(120, 50, 100)).toEqual({ r: 255, g: 255, b: 255 });
    });

    test('converts full saturation and mid lightness blue correctly', () => {
        expect(hslToRgb(240, 100, 50)).toEqual({ r: 0, g: 0, b: 255 });
    });

    test('handles edge hue at 360 degrees correctly', () => {
        expect(hslToRgb(360, 100, 50)).toEqual({ r: 255, g: 0, b: 0 }); // Should be the same as hue 0
    });
});
