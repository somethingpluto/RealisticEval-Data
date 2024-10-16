function spatialWeight(spatial_diff: number, sigma_space: number): number {
    // Validate that sigma_space is greater than zero to avoid division by zero
    if (sigma_space <= 0) {
        throw new Error("sigma_space must be greater than zero.");
    }

    // Calculate the squared spatial difference
    const squared_diff = spatial_diff * spatial_diff;

    // Calculate the denominator using sigma_space squared
    const denominator = 2 * sigma_space * sigma_space;

    // Calculate and return the spatial weight
    return Math.exp(-squared_diff / denominator);
}