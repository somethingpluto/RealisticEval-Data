#include <cmath> // Include the cmath library for the exp function

/**
 * @brief Calculates the Gaussian weight based on the difference in intensity and a color standard deviation.
 *
 * The Gaussian weight is calculated using the formula:
 * weight = exp(- (intensity_diff^2) / (2 * sigma_color^2))
 *
 * @param intensity_diff The difference in intensity, which is used to compute the weight.
 * @param sigma_color The standard deviation for the color, affecting the spread of the weight.
 * @return The Gaussian weight as a float.
 */
inline float gaussianWeight(float intensity_diff, float sigma_color) {}