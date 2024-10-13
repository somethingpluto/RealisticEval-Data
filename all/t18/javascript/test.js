describe('TestFloatToRGB', () => {
    it('should return pure red for value 0.0', () => {
        const result = floatToRGB(0.0);
        expect(result).toEqual([255, 0, 0]);
    });

    it('should return pure green for value 1.0', () => {
        const result = floatToRGB(1.0);
        expect(result).toEqual([0, 255, 0]);
    });

    it('should return yellow (equal mix of red and green) for value 0.5', () => {
        const result = floatToRGB(0.5);
        expect(result).toEqual([127, 127, 0]);
    });

    it('should return more red than green for value 0.25', () => {
        const result = floatToRGB(0.25);
        expect(result).toEqual([191, 63, 0]);
    });

    it('should throw an error for value outside the range [0, 1]', () => {
        expect(() => floatToRGB(1.5)).toThrow('Value must be between 0 and 1 inclusive.');
    });
});