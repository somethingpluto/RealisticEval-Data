MatrixXd im2col(const Array3i& image, int filter_height, int filter_width, int stride = 1, int padding = 0) {
    /**
     * Apply the im2col operation to an input image.
     *
     * Parameters:
     * - image (Eigen::Array3i): The input image of shape (C, H, W) where:
     *     C: Number of channels
     *     H: Height of the image
     *     W: Width of the image
     * - filter_height (int): Height of the filter
     * - filter_width (int): Width of the filter
     * - stride (int): Stride of the filter
     * - padding (int): Number of pixels to pad the input image
     *
     * Returns:
     * - col (Eigen::MatrixXd): A 2D array where each column is a flattened filter region
     */
}