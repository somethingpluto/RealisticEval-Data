#include <cmath> // Include cmath for the exp function

/**
 * @brief Calculates the spatial weight based on the difference in spatial coordinates and a space standard deviation.
 *
 * The spatial weight is calculated using the formula:
 * weight = exp(- (spatial_diff^2) / (2 * sigma_space^2))
 *
 * @param spatial_diff The difference in spatial coordinates, which is used to compute the weight.
 * @param sigma_space The standard deviation for spatial distance, affecting the spread of the weight.
 * @return The spatial weight as a float.
 *
 */
inline float spatialWeight(float spatial_diff, float sigma_space) {}