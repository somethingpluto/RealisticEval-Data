#include <Eigen/Dense>

/**
 * Applies a shear transformation to a 2D matrix along the x-axis.
 *
 * @param matrix A 2D Eigen::MatrixXd object representing the original matrix.
 * @param shear_factor The factor by which the matrix is sheared along the x-axis.
 * @return Eigen::MatrixXd The sheared matrix.
 */
Eigen::MatrixXd applyShearX(const Eigen::MatrixXd& matrix, double shearFactor) {
    // Create an identity matrix of size equal to the input matrix
    Eigen::MatrixXd shearMatrix = Eigen::MatrixXd::Identity(matrix.rows(), matrix.cols());

    // Set the appropriate element for the shear transformation along the x-axis
    shearMatrix(1, 0) = shearFactor;

    // Perform the multiplication between the shear matrix and the original matrix
    return shearMatrix * matrix;
}
