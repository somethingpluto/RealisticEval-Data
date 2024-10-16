#include <array>
#include <cmath>

/**
 * @brief Get the scaling factors for a 2D affine transformation.
 *
 * @param matrix The 3x3 affine transformation matrix.
 * @return std::pair<double, double> A pair containing the scale factors (scaleX, scaleY).
 */
std::pair<double, double> getScale(const std::array<std::array<double, 3>, 3>& matrix)
{
    // Extracting scale factors from the matrix
    double scaleX = std::sqrt(matrix[0][0] * matrix[0][0] + matrix[1][0] * matrix[1][0]);
    double scaleY = std::sqrt(matrix[0][1] * matrix[0][1] + matrix[1][1] * matrix[1][1]);

    return {scaleX, scaleY};
}
