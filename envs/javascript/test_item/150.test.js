/**
 * Convert an RGB color object to a HEX color string.
 * @param rgb - An object containing the red, green, and blue components of the color.
 * @returns A string representing the HEX color code.
 */
export function rgbToHex(rgb) {
    const { r, g, b } = rgb;
    const toHex = (value) => {
        const hex = value.toString(16);
        return hex.length === 1 ? '0' + hex : hex;
    };
    return `#${toHex(r)}${toHex(g)}${toHex(b)}`.toUpperCase();
}

/**
 * Convert a HEX color string to an RGB color object.
 * @param hex - A string representing the HEX color code.
 * @returns An object containing the red, green, and blue components of the color, or null if the HEX code is invalid.
 */
export function hexToRgb(hex) {
    const isValidHex = (hex) => /^#?([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})$/.test(hex);
    if (!isValidHex(hex)) {
        return null;
    }

    let normalizedHex = hex.startsWith('#') ? hex.slice(1) : hex;
    if (normalizedHex.length === 3) {
        normalizedHex = normalizedHex.split('').map(char => char + char).join('');
    }

    const r = parseInt(normalizedHex.slice(0, 2), 16);
    const g = parseInt(normalizedHex.slice(2, 4), 16);
    const b = parseInt(normalizedHex.slice(4, 6), 16);

    return { r, g, b };
}
describe('rgbToHex and hexToRgb', () => {

    // Test the basic functionality of rgbToHex
    test('should correctly convert RGB to HEX', () => {
        const rgb = { r: 255, g: 99, b: 71 };
        const result = rgbToHex(rgb);
        expect(result).toBe('#ff6347'); // Expected HEX code for RGB(255, 99, 71)
    });

    // Test the basic functionality of hexToRgb
    test('should correctly convert HEX to RGB', () => {
        const hex = '#ff6347';
        const result = hexToRgb(hex);
        expect(result).toEqual({ r: 255, g: 99, b: 71 }); // Expected RGB object for HEX #ff6347
    });

    // Test rgbToHex for handling invalid values gracefully
    test('should handle invalid RGB components gracefully', () => {
        const rgb = { r: 300, g: -10, b: 128 };
        const result = rgbToHex(rgb);
        expect(result).toBe('#12c800'); // Invalid values (300, -10) should be clamped to "00", valid value should convert to "80"
    });

    // Test hexToRgb for handling invalid HEX strings
    test('should return null for invalid HEX strings', () => {
        const invalidHex = '#ggg123';
        const result = hexToRgb(invalidHex);
        expect(result).toBeNull(); // Invalid HEX code should return null
    });

    // Test rgbToHex for handling boundary values
    test('should handle boundary values in RGB correctly', () => {
        const rgb = { r: 0, g: 0, b: 0 };
        const result = rgbToHex(rgb);
        expect(result).toBe('#000000'); // Boundary RGB(0, 0, 0) should convert to #000000

        const rgbWhite = { r: 255, g: 255, b: 255 };
        const resultWhite = rgbToHex(rgbWhite);
        expect(resultWhite).toBe('#ffffff'); // Boundary RGB(255, 255, 255) should convert to #ffffff
    });
});
