TEST_CASE("TestGetRotationFunction", "[rotation]") {
    SECTION("test_rotation_0_degrees") {
        // Test for a rotation of 0 degrees (identity matrix)
        Eigen::Matrix3d matrix;
        matrix << 1, 0, 0,
                  0, 1, 0,
                  0, 0, 1;
        double expected_rotation = 0.0;
        REQUIRE(std::abs(get_rotation(matrix) - expected_rotation) < 1e-6);
    }

    SECTION("test_rotation_90_degrees") {
        // Test for a rotation of 90 degrees
        Eigen::Matrix3d matrix;
        matrix << 0, -1, 0,
                  1, 0, 0,
                  0, 0, 1;
        double expected_rotation = M_PI / 2;  // 90 degrees in radians
        REQUIRE(std::abs(get_rotation(matrix) - expected_rotation) < 1e-6);
    }

    SECTION("test_rotation_180_degrees") {
        // Test for a rotation of 180 degrees
        Eigen::Matrix3d matrix;
        matrix << -1, 0, 0,
                  0, -1, 0,
                  0, 0, 1;
        double expected_rotation = M_PI;  // 180 degrees in radians
        REQUIRE(std::abs(get_rotation(matrix) - expected_rotation) < 1e-6);
    }

    SECTION("test_rotation_negative_90_degrees") {
        // Test for a rotation of -90 degrees
        Eigen::Matrix3d matrix;
        matrix << 0, 1, 0,
                  -1, 0, 0,
                  0, 0, 1;
        double expected_rotation = -M_PI / 2;  // -90 degrees in radians
        REQUIRE(std::abs(get_rotation(matrix) - expected_rotation) < 1e-6);
    }
}