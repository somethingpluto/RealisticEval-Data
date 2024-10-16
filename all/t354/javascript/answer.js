/**
 * @brief Calculates the Gaussian weight based on the difference in intensity and a color standard deviation.
 *
 * The Gaussian weight is calculated using the formula:
 * weight = exp(- (intensity_diff^2) / (2 * sigma_color^2))
 *
 * @param {number} intensityDiff The difference in intensity, which is used to compute the weight.
 * @param {number} sigmaColor The standard deviation for the color, affecting the spread of the weight.
 * @return {number} The Gaussian weight.
 */
function gaussianWeight(intensityDiff, sigmaColor) {
    // Calculate the squared intensity difference
    const squaredDiff = intensityDiff * intensityDiff;

    // Calculate the denominator using sigmaColor squared
    const denominator = 2 * sigmaColor * sigmaColor;

    // Calculate and return the Gaussian weight
    return Math.exp(-squaredDiff / denominator);
}