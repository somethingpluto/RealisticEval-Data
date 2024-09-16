// Created by chatgpt.
inline float gaussianWeight(float intensity_diff, float sigma_color) {
	return exp(-(intensity_diff * intensity_diff) / (2 * sigma_color * sigma_color));
}