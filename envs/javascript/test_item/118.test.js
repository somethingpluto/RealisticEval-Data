/**
 * Converts HSL color values to RGB.
 *
 * @param {number} h - Hue (0-360 degrees).
 * @param {number} s - Saturation (0-100%).
 * @param {number} l - Lightness (0-100%).
 * @returns {Object} An object containing the RGB values.
 */
function hslToRgb(h, s, l) {
    s /= 100;
    l /= 100;

    let c = (1 - Math.abs(2 * l - 1)) * s;
    let x = c * (1 - Math.abs((h / 60) % 2 - 1));
    let m = l - c / 2;
    let r = 0;
    let g = 0;
    let b = 0;

    if (0 <= h && h < 60) {
        r = c;
        g = x;
        b = 0;
    } else if (60 <= h && h < 120) {
        r = x;
        g = c;
        b = 0;
    } else if (120 <= h && h < 180) {
        r = 0;
        g = c;
        b = x;
    } else if (180 <= h && h < 240) {
        r = 0;
        g = x;
        b = c;
    } else if (240 <= h && h < 300) {
        r = x;
        g = 0;
        b = c;
    } else if (300 <= h && h < 360) {
        r = c;
        g = 0;
        b = x;
    }

    r = Math.round((r + m) * 255);
    g = Math.round((g + m) * 255);
    b = Math.round((b + m) * 255);

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
