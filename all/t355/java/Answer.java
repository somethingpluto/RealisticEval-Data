package org.real.temp;

/**
 * Calculates the spatial weight based on the difference in spatial coordinates and a space standard deviation.
 *
 * The spatial weight is calculated using the formula:
 * weight = exp(- (spatial_diff^2) / (2 * sigma_space^2))
 *
 * @param spatial_diff The difference in spatial coordinates, which is used to compute the weight.
 * @param sigma_space The standard deviation for spatial distance, affecting the spread of the weight.
 * @return The spatial weight as a float.
 * @throws IllegalArgumentException if sigma_space is less than or equal to zero.
 */
public class Answer {

    public static float spatialWeight(float spatial_diff, float sigma_space) {
        // Validate that sigma_space is greater than zero to avoid division by zero
        if (sigma_space <= 0.0f) {
            throw new IllegalArgumentException("sigma_space must be greater than zero.");
        }

        // Calculate the squared spatial difference
        float squared_diff = spatial_diff * spatial_diff;

        // Calculate the denominator using sigma_space squared
        float denominator = 2 * sigma_space * sigma_space;

        // Calculate and return the spatial weight
        return (float) Math.exp(-squared_diff / denominator);
    }
}