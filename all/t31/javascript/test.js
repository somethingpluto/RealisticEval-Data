describe('TestCalculateRedProportion', () => {
    it('should return 1.0 when all pixels are fully red', () => {
        const pixels = [[255, 0, 0], [255, 0, 0], [255, 0, 0]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(1.0);
    });

    it('should return 0.0 when no red component in any pixel', () => {
        const pixels = [[0, 255, 0], [0, 0, 255], [0, 255, 255]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

    it('should return 0.0 when the pixel list is empty', () => {
        const pixels = [];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });

    it('should return 0.0 when all pixels are black', () => {
        const pixels = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
        const result = calculateRedProportion(pixels);
        expect(result).toBeCloseTo(0.0);
    });
});