#include <catch2/catch.hpp>
#include <Eigen/Dense>

double get_rotation(const Eigen::Matrix2d& matrix) {
    /**
     * Given an affine transformation matrix, return the corresponding rotation angle in radians.
     *
     * Args:
     *     matrix (Eigen::Matrix2d): A 2D affine transformation matrix.
     *
     * Returns:
     *     double: The rotation angle in radians, extracted from the affine matrix.
     */
    double cos_theta = (matrix(0, 0) + matrix(1, 1)) / 2.0;
    return std::acos(cos_theta);
}

TEST_CASE("get_rotation", "[rotation]") {
    // Test case 1: Identity matrix
    Eigen::Matrix2d identity_matrix = Eigen::Matrix2d::Identity();
    REQUIRE(get_rotation(identity_matrix) == Approx(0.0));

    // Test case 2: Rotation matrix by 90 degrees (pi/2 radians)
    Eigen::Matrix2d rotation_matrix_90;
    rotation_matrix_90 << 0, -1,
                          1,  0;
    REQUIRE(get_rotation(rotation_matrix_90) == Approx(M_PI / 2.0));

    // Test case 3: Rotation matrix by 180 degrees (pi radians)
    Eigen::Matrix2d rotation_matrix_180;
    rotation_matrix_180 << -1, 0,
                           0, -1;
    REQUIRE(get_rotation(rotation_matrix_180) == Approx(M_PI).margin(1e-6)); // Allowing some margin for floating-point precision

    // Test case 4: Rotation matrix by 270 degrees (3*pi/2 radians)
    Eigen::Matrix2d rotation_matrix_270;
    rotation_matrix_270 << 0, 1,
                          -1, 0;
    REQUIRE(get_rotation(rotation_matrix_270) == Approx(3 * M_PI / 2.0));
}
