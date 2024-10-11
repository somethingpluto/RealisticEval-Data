describe('floatToRgb', () => {
    test('pure red', () => {
        // Value at the lower boundary (0.0) should return pure red
        const result = floatToRgb(0.0);
        expect(result).toEqual([255, 0, 0]);
    });

    test('pure green', () => {
        // Value at the upper boundary (1.0) should return pure green
        const result = floatToRgb(1.0);
        expect(result).toEqual([0, 255, 0]);
    });

    test('midpoint', () => {
        // Value at 0.5 should return an equal mix of red and green, resulting in yellow
        const result = floatToRgb(0.5);
        expect(result).toEqual([127, 127, 0]);
    });

    test('quarter point', () => {
        // Value at 0.25 should return more red than green
        const result = floatToRgb(0.25);
        expect(result).toEqual([191, 63, 0]);
    });

    test('invalid value', () => {
        // Value outside the range [0, 1] should throw an Error
        expect(() => {
            floatToRgb(1.5);
        }).toThrow(Error);
    });
});