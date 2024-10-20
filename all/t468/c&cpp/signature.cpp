#include <Eigen/Dense>
#include <vector>

/**
 * @brief Given a 3x3 matrix, return the corresponding translation vector.
 *
 * @param matrix A 3x3 affine transformation matrix.
 * @return std::vector<double> A 2-element vector containing the translation components (translation_x, translation_y).
 */
std::vector<double> get_translation(const Eigen::Matrix3d& matrix);
