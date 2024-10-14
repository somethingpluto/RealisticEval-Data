#include <Eigen/Dense>
#include <iostream>

using Eigen::MatrixXd;
using Eigen::ArrayXd;

// Function to apply the im2col operation to an input image.
MatrixXd im2col(const Eigen::Array3i& image, int filter_height, int filter_width, int stride = 1, int padding = 0) {
    // Extract dimensions of the input image
    int C = image.dimension(0);
    int H = image.dimension(1);
    int W = image.dimension(2);

    // Calculate output dimensions
    int out_height = (H + 2 * padding - filter_height) / stride + 1;
    int out_width = (W + 2 * padding - filter_width) / stride + 1;

    // Create a padded image
    Eigen::Array3i padded_image(C, H + 2 * padding, W + 2 * padding);
    padded_image.setZero();
    padded_image.block(0, padding, padding, H, W) = image;

    // Initialize the column matrix
    MatrixXd col(C * filter_height * filter_width, out_height * out_width);
    col.setZero();

    // Fill the column matrix
    int col_idx = 0;
    for (int y = 0; y <= H + 2 * padding - filter_height; y += stride) {
        for (int x = 0; x <= W + 2 * padding - filter_width; x += stride) {
            Eigen::Array3i patch = padded_image.block(0, y, x, C, filter_height, filter_width);
            col.col(col_idx) = patch.reshape(C * filter_height * filter_width);
            col_idx++;
        }
    }

    return col;
}