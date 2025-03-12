// Start of the TypeScript module

export function rgbToHsl({ r, g, b }: { r: number; g: number; b: number }): { h: number; s: number; l: number } {
  // ... (rest of the function remains unchanged)
}

// End of the TypeScript module
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

    // Additional tests
    test('should handle vibrant green', () => {
        const rgb = { r: 0, g: 255, b: 0 };
        const result = rgbToHsl(rgb);
        expect(result).toEqual({ h: 120, s: 100, l: 50 });
    });

    test('should handle deep blue', () => {
        const rgb = { r: 0, g: 0, b: 255 };
        const result = rgbToHsl(rgb);
        expect(result).toEqual({ h: 240, s: 100, l: 50 });
    });
});
