/**
 * Calculates the Gaussian weight based on the difference in intensity and a color standard deviation.
 *
 * The Gaussian weight is calculated using the formula:
 * weight = exp(- (intensityDiff^2) / (2 * sigmaColor^2))
 *
 * @param intensityDiff The difference in intensity, which is used to compute the weight.
 * @param sigmaColor The standard deviation for the color, affecting the spread of the weight.
 * @returns The Gaussian weight as a number.
 */
function gaussianWeight(intensityDiff: number, sigmaColor: number): number {}