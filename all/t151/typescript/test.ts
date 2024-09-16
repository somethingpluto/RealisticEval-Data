describe('rgbToHsl', () => {

    test('should convert basic RGB values correctly (red)', () => {
        const rgb = { r: 255, g: 0, b: 0 };
        const result = rgbToHsl(rgb);
        expect(result).toEqual({ h: 0, s: 100, l: 50 });
    });

    test('should handle grayscale values (middle gray)', () => {
        const rgb = { r: 128, g: 128, b: 128 };
        const result = rgbToHsl(rgb);
        expect(result).toEqual({ h: 0, s: 0, l: 50 });
    });

    test('should handle edge cases (white color)', () => {
        const rgb = { r: 255, g: 255, b: 255 };
        const result = rgbToHsl(rgb);
        expect(result).toEqual({ h: 0, s: 0, l: 100 });
    });

    test('should handle edge cases (black color)', () => {
        const rgb = { r: 0, g: 0, b: 0 };
        const result = rgbToHsl(rgb);
        expect(result).toEqual({ h: 0, s: 0, l: 0 });
    });

    test('should throw an error for invalid RGB values (negative values)', () => {
        const rgb = { r: -50, g: 50, b: 50 };
        expect(() => rgbToHsl(rgb)).toThrow('Invalid RGB value. Each value must be between 0 and 255.');
    });

});
