/**
 * @brief Apply the im2col operation to an input image.
 *
 * This function transforms the input image into a 2D array where each column 
 * represents a flattened filter region, allowing for efficient convolution operations.
 *
 * @param image The input image of shape (C, H, W) where:
 *        - C: Number of channels
 *        - H: Height of the image
 *        - W: Width of the image
 * @param filter_height The height of the filter.
 * @param filter_width The width of the filter.
 * @param stride The stride of the filter.
 * @param padding The number of pixels to pad the input image.
 * @return A 2D array (Eigen::MatrixXd) where each column is a flattened filter region.
 */
MatrixXd im2col(const Array3i& image, int filter_height, int filter_width, int stride = 1, int padding = 0) {
}