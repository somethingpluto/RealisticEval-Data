/**
 * @brief Calculates the Gaussian weight based on the difference in intensity and a color standard deviation.
 *
 * The Gaussian weight is calculated using the formula:
 * weight = exp(- (intensity_diff^2) / (2 * sigma_color^2))
 *
 * @param intensityDiff The difference in intensity, which is used to compute the weight.
 * @param sigmaColor The standard deviation for the color, affecting the spread of the weight.
 * @returns The Gaussian weight as a number.
 */
function gaussianWeight(intensityDiff: number, sigmaColor: number): number {
    // Calculate the squared intensity difference
    const squaredDiff = intensityDiff * intensityDiff;

    // Calculate the denominator using sigmaColor squared
    const denominator = 2 * sigmaColor * sigmaColor;

    // Calculate and return the Gaussian weight
    return Math.exp(-squaredDiff / denominator);
}