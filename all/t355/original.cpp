// Created by chatgpt.
// Calculate the Gaussian weight for spatial distance
inline float spatialWeight(float spatial_diff, float sigma_space) {
	return exp(-(spatial_diff * spatial_diff) / (2 * sigma_space * sigma_space));
}
