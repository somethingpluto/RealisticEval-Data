#include <catch2/catch.hpp>
#include <Eigen/Dense>

// Assuming Eigen is used for matrix operations

Eigen::Vector2d get_translation(const Eigen::Matrix3d& matrix) {
    // Extract the translation part from the 3x3 matrix
    Eigen::Vector2d translation = matrix.block<2, 1>(0, 2);
    return translation;
}

TEST_CASE("Test get_translation function", "[get_translation]") {
    // Test case 1: Identity matrix should have no translation
    Eigen::Matrix3d identity_matrix = Eigen::Matrix3d::Identity();
    REQUIRE(get_translation(identity_matrix).isApprox(Eigen::Vector2d(0, 0)));

    // Test case 2: Translation matrix should return the correct translation vector
    Eigen::Matrix3d translation_matrix = Eigen::Matrix3d::Identity();
    translation_matrix(0, 2) = 5.0;
    translation_matrix(1, 2) = 10.0;
    REQUIRE(get_translation(translation_matrix).isApprox(Eigen::Vector2d(5.0, 10.0)));

    // Add more test cases as needed
}
