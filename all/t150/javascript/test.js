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