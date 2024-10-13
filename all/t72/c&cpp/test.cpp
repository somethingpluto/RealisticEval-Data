TEST_CASE("TestGet3DCoordinates", "[get_3d_coordinates]") {
    // Define a common intrinsic matrix for testing
    MatrixXd K(3, 3);
    K << 1000, 0, 320,
         0, 1000, 240,
         0, 0, 1;

    SECTION("test_center_coordinates") {
        // Test with center pixel coordinates where x and y should map to zero in NDC.
        VectorXd result = get_3d_coordinates(K, 100, 320, 240);
        REQUIRE_THAT(result, Catch::Approx(VectorXd::Zero(3)).epsilon(1e-6));
    }

    SECTION("test_boundary_coordinates") {
        // Test with boundary values in the image frame.
        VectorXd result = get_3d_coordinates(K, 50, 640, 480);
        double expected_x = (640 - 320) / 1000 * 50;
        double expected_y = (480 - 240) / 1000 * 50;
        REQUIRE_THAT(result, Catch::Approx(VectorXd::Zero(3) + VectorXd({expected_x, expected_y, 50})).epsilon(1e-6));
    }

    SECTION("test_negative_depth") {
        // Test with a negative depth to see if it handles incorrect input properly.
        VectorXd result = get_3d_coordinates(K, -100, 320, 240);
        REQUIRE_THAT(result, Catch::Approx(VectorXd::Zero(3) + VectorXd({0.0, 0.0, -100})).epsilon(1e-6));
    }

    SECTION("test_zero_depth") {
        // Test with zero depth which should lead to a zero-length vector.
        VectorXd result = get_3d_coordinates(K, 0, 320, 240);
        REQUIRE_THAT(result, Catch::Approx(VectorXd::Zero(3)).epsilon(1e-6));
    }

    SECTION("test_non_integer_values") {
        // Test with non-integer pixel coordinates.
        VectorXd result = get_3d_coordinates(K, 100, 320.5, 240.5);
        double expected_x = (320.5 - 320) / 1000 * 100;
        double expected_y = (240.5 - 240) / 1000 * 100;
        REQUIRE_THAT(result, Catch::Approx(VectorXd::Zero(3) + VectorXd({expected_x, expected_y, 100})).epsilon(1e-6));
    }
}