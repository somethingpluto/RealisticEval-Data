#include <iostream>
#include <Eigen/Dense> // For matrix operations
#include <cmath>       // For trigonometric functions

// Function to calculate the rotation angle from a 3x3 affine transformation matrix
double get_rotation(const Eigen::Matrix3d& matrix) {
    // Ensure the matrix is a 3x3 affine transformation matrix
    if (matrix.rows() != 3 || matrix.cols() != 3) {
        throw std::invalid_argument("Input must be a 3x3 affine transformation matrix.");
    }

    // Calculate the rotation angle using atan2
    double rotation_angle = std::atan2(matrix(1, 0), matrix(0, 0));

    return rotation_angle;
}