TEST_CASE("Test Get Scale Function", "[get_scale]") {
    SECTION("Identity Matrix") {
        // Test for the identity matrix (no scaling)
        Eigen::MatrixXd matrix(3, 3);
        matrix << 1, 0, 0,
                  0, 1, 0,
                  0, 0, 1;
        auto expected_scale = std::make_pair(1.0, 1.0);
        REQUIRE(get_scale(matrix) == expected_scale);
    }

    SECTION("Scaling Matrix") {
        // Test for a scaling matrix (2x in x and 3x in y)
        Eigen::MatrixXd matrix(3, 3);
        matrix << 2, 0, 0,
                  0, 3, 0,
                  0, 0, 1;
        auto expected_scale = std::make_pair(2.0, 3.0);
        REQUIRE(get_scale(matrix) == expected_scale);
    }

    SECTION("Uniform Scaling") {
        // Test case with uniform scaling
        Eigen::MatrixXd matrix(3, 3);
        matrix << 2, 0, 0,
                  0, 2, 0,
                  0, 0, 1;
        auto expected_scale = std::make_pair(2.0, 2.0);
        REQUIRE(get_scale(matrix) == expected_scale);
    }

    SECTION("Non-Uniform Scaling") {
        // Test case with non-uniform scaling
        Eigen::MatrixXd matrix(3, 3);
        matrix << 3, 0, 0,
                  0, 5, 0,
                  0, 0, 1;
        auto expected_scale = std::make_pair(3.0, 5.0);
        REQUIRE(get_scale(matrix) == expected_scale);
    }

    SECTION("Reflection Matrix") {
        // Test case with reflection matrix
        Eigen::MatrixXd matrix(3, 3);
        matrix << -1, 0, 0,
                  0, 1, 0,
                  0, 0, 1;
        auto expected_scale = std::make_pair(1.0, 1.0);
        REQUIRE(get_scale(matrix) == expected_scale);
    }
}