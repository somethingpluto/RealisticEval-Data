/**
 * Analyze a list of pixels, each represented by RGB, and calculate the proportion of red in the list.
 *
 * @param {Array<Array<number>>} pixels - A list of pixels, where each pixel is represented as an array [R, G, B].
 * @returns {number} The proportion of red in the list of pixels, as a value between 0 and 1.
 */
function calculateRedProportion(pixels) {
    if (!Array.isArray(pixels) || pixels.length === 0) {
        throw new Error('Invalid input: pixels must be a non-empty array');
    }

    let totalRed = 0;
    let totalPixels = pixels.length;

    for (let i = 0; i < totalPixels; i++) {
        const [r, g, b] = pixels[i];
        if (typeof r !== 'number' || typeof g !== 'number' || typeof b !== 'number') {
            throw new Error('Invalid pixel format: each pixel must be an array of three numbers [R, G, B]');
        }
        totalRed += r;
    }

    return totalRed / (totalPixels * 255);
}
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
