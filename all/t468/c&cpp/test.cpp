TEST_CASE("Test GetTranslationFunction", "[get_translation]") {
    SECTION("Identity Matrix") {
        Eigen::Matrix3d matrix;
        matrix << 1, 0, 0,
                  0, 1, 0,
                  0, 0, 1;

        Eigen::Matrix<double, 2, 1> expected_translation = Eigen::Matrix<double, 2, 1>::Zero();
        REQUIRE(get_translation(matrix) == expected_translation);
    }

    SECTION("Translation Matrix") {
        Eigen::Matrix3d matrix;
        matrix << 1, 0, 5,
                  0, 1, 10,
                  0, 0, 1;

        Eigen::Matrix<double, 2, 1> expected_translation;
        expected_translation << 5.0, 10.0;
        REQUIRE(get_translation(matrix) == expected_translation);
    }

    SECTION("Negative Translation") {
        Eigen::Matrix3d matrix;
        matrix << 1, 0, -3,
                  0, 1, -6,
                  0, 0, 1;

        Eigen::Matrix<double, 2, 1> expected_translation;
        expected_translation << -3.0, -6.0;
        REQUIRE(get_translation(matrix) == expected_translation);
    }
}