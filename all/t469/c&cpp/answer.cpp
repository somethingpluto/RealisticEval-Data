#include <iostream>
#include <Eigen/Dense>  // For matrix operations
#include <utility>      // For std::pair
#include <stdexcept>    // For std::invalid_argument

// Function to calculate the scaling factors from a 3x3 affine transformation matrix
std::pair<double, double> get_scale(const Eigen::MatrixXd& matrix) {
    // Ensure the matrix is a 3x3 matrix
    if (matrix.rows() != 3 || matrix.cols() != 3) {
        throw std::invalid_argument("Input must be a 3x3 affine transformation matrix.");
    }

    // Calculate the scale factors using the norm of the columns
    double scale_x = matrix.block(0, 0, 2, 1).norm();  // Using the first two rows for x-scale
    double scale_y = matrix.block(0, 1, 2, 1).norm();  // Using the first two rows for y-scale

    return std::make_pair(scale_x, scale_y);
}