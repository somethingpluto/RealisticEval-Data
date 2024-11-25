#include <Eigen/Dense>
#include <stdexcept>

// Function to extract the translation vector from a 3x3 affine transformation matrix
Eigen::Matrix<double, 2, 1> get_translation(const Eigen::Matrix3d& matrix) {
    // Ensure the matrix is a 3x3 Eigen matrix
    if (matrix.rows() != 3 || matrix.cols() != 3) {
        throw std::invalid_argument("Input must be a 3x3 affine transformation matrix.");
    }

    // Extract the translation components from the matrix
    Eigen::Matrix<double, 2, 1> translation;
    translation << matrix(0, 2), matrix(1, 2);

    return translation;
}