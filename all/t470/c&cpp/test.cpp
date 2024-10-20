TEST_CASE("TestShearTransformation", "[shear]") {
    SECTION("test_identity_shear") {
        // Test with zero shear factor which should return the original matrix unchanged.
        Eigen::MatrixXd matrix = Eigen::MatrixXd::Zero(2, 2);
        matrix << 1, 2,
                  3, 4;
        double shear_factor = 0;
        Eigen::MatrixXd expected_output = Eigen::MatrixXd::Zero(2, 2);
        expected_output << 1, 2,
                           3, 4;
        Eigen::MatrixXd result = apply_shear_x(matrix, shear_factor);
        REQUIRE(result.isApprox(expected_output));
    }

    SECTION("test_positive_shear") {
        // Test with a positive shear factor.
        Eigen::MatrixXd matrix = Eigen::MatrixXd::Zero(2, 2);
        matrix << 1, 2,
                  3, 4;
        double shear_factor = 1;
        Eigen::MatrixXd expected_output = Eigen::MatrixXd::Zero(2, 2);
        expected_output << 1, 3,
                           3, 7;
        Eigen::MatrixXd result = apply_shear_x(matrix, shear_factor);
        REQUIRE(result.isApprox(expected_output));
    }

    SECTION("test_negative_shear") {
        // Test with a negative shear factor.
        Eigen::MatrixXd matrix = Eigen::MatrixXd::Zero(2, 2);
        matrix << 1, 2,
                  3, 4;
        double shear_factor = -1;
        Eigen::MatrixXd expected_output = Eigen::MatrixXd::Zero(2, 2);
        expected_output << 1, 1,
                           3, 1;
        Eigen::MatrixXd result = apply_shear_x(matrix, shear_factor);
        REQUIRE(result.isApprox(expected_output));
    }

    SECTION("test_high_shear_factor") {
        // Test with a high shear factor to see how the matrix adapts to extreme transformations.
        Eigen::MatrixXd matrix = Eigen::MatrixXd::Zero(2, 2);
        matrix << 1, 1,
                  1, 1;
        double shear_factor = 10;
        Eigen::MatrixXd expected_output = Eigen::MatrixXd::Zero(2, 2);
        expected_output << 1, 11,
                           1, 11;
        Eigen::MatrixXd result = apply_shear_x(matrix, shear_factor);
        REQUIRE(result.isApprox(expected_output));
    }
}