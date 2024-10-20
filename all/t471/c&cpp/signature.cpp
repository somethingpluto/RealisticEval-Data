#include <Eigen/Dense>

/**
 * @brief Extracts the rotation angle from a 2D affine transformation matrix.
 *
 * @param matrix A 2x3 Eigen::Matrix representing a 2D affine transformation matrix.
 * @return double The rotation angle in radians, extracted from the affine matrix.
 */
double get_rotation(const Eigen::Matrix2d& matrix);
