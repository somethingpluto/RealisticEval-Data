/**
 * Calculates the Gaussian weight based on the difference in intensity and a color standard deviation.
 *
 * The Gaussian weight is calculated using the formula:
 * weight = exp(- (intensityDiff^2) / (2 * sigmaColor^2))
 *
 * @param {number} intensityDiff The difference in intensity, which is used to compute the weight.
 * @param {number} sigmaColor The standard deviation for the color, affecting the spread of the weight.
 * @return {number} The Gaussian weight.
 */
function gaussianWeight(intensityDiff, sigmaColor) {
    return Math.exp(- (intensityDiff * intensityDiff) / (2 * sigmaColor * sigmaColor));
}
describe("Gaussian Weight Calculation Tests", () => {

    test("Zero Intensity Difference", () => {
        // When intensity difference is zero, weight should be 1
        const intensityDiff = 0.0;
        const sigmaColor = 1.0; // arbitrary sigma value
        expect(gaussianWeight(intensityDiff, sigmaColor)).toBeCloseTo(1.0, 3);
    });

    test("Positive Intensity Difference", () => {
        // A positive intensity difference with a reasonable sigma
        const intensityDiff = 2.0;
        const sigmaColor = 2.0;
        const expectedWeight = Math.exp(-(intensityDiff * intensityDiff) / (2 * sigmaColor * sigmaColor));
        expect(gaussianWeight(intensityDiff, sigmaColor)).toBeCloseTo(expectedWeight, 3);
    });

    test("Negative Intensity Difference", () => {
        // A negative intensity difference should yield the same weight as positive
        const intensityDiff = -2.0;
        const sigmaColor = 2.0;
        const expectedWeight = Math.exp(-(intensityDiff * intensityDiff) / (2 * sigmaColor * sigmaColor));
        expect(gaussianWeight(intensityDiff, sigmaColor)).toBeCloseTo(expectedWeight, 3);
    });

    test("Small Sigma Color", () => {
        // Test with a small sigma value
        const intensityDiff = 1.0;
        const sigmaColor = 0.1;
        const expectedWeight = Math.exp(-(intensityDiff * intensityDiff) / (2 * sigmaColor * sigmaColor));
        expect(gaussianWeight(intensityDiff, sigmaColor)).toBeCloseTo(expectedWeight, 3);
    });

    test("Large Sigma Color", () => {
        // Test with a large sigma value
        const intensityDiff = 1.0;
        const sigmaColor = 100.0;
        const expectedWeight = Math.exp(-(intensityDiff * intensityDiff) / (2 * sigmaColor * sigmaColor));
        expect(gaussianWeight(intensityDiff, sigmaColor)).toBeCloseTo(expectedWeight, 3);
    });

});
