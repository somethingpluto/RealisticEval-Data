/**
 * Analyze a list of pixels, each represented by RGB, and calculate the proportion of red in the list.
 *
 * @param {Array<Array<number>>} pixels - A list of pixels, where each pixel is represented as an array [R, G, B].
 * @returns {number} The proportion of red in the list of pixels, as a value between 0 and 1.
 */
function calculateRedProportion(pixels) {
    if (pixels.length === 0) return 0;

    let totalRed = 0;
    let totalIntensity = 0;

    for (let i = 0; i < pixels.length; i++) {
        const [R, G, B] = pixels[i];
        totalRed += R;
        totalIntensity += (R + G + B);
    }

    if (totalIntensity === 0) return 0;

    return totalRed / totalIntensity;
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
