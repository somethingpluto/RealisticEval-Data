#include <iostream>
#include <Eigen/Dense>

// Function to extract the translation part from a 3x3 affine transformation matrix
Eigen::Vector2d getTranslation(const Eigen::Matrix3d& matrix) {
    // Extract the translation vector from the last column of the matrix
    Eigen::Vector2d translation = matrix.block(0, 2, 3, 1).topRows<2>();
    return translation;
}