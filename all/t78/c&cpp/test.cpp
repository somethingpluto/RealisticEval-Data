TEST_CASE("Test Euler to Rotation Matrix") {
    SECTION("Zero Rotation") {
        // Test with zero rotation for all axes
        Matrix3f R = euler_to_rotation_matrix(0, 0, 0);
        Matrix3f expected = Matrix3f::Identity();
        REQUIRE_THAT(R, Catch::Approx(expected).epsilon(1e-6));
    }

    SECTION("Rotation About X") {
        // Test rotation about the x-axis
        Matrix3f R = euler_to_rotation_matrix(90, 0, 0);
        Matrix3f expected = Matrix3f::Zero();
        expected << 1, 0, 0,
                    0, 0, -1,
                    0, 1, 0;
        REQUIRE_THAT(R, Catch::Approx(expected).epsilon(1e-6));
    }

    SECTION("Rotation About Y") {
        // Test rotation about the y-axis
        Matrix3f R = euler_to_rotation_matrix(0, 90, 0);
        Matrix3f expected = Matrix3f::Zero();
        expected << 0, 0, 1,
                    0, 1, 0,
                    -1, 0, 0;
        REQUIRE_THAT(R, Catch::Approx(expected).epsilon(1e-6));
    }

    SECTION("Rotation About Z") {
        // Test rotation about the z-axis
        Matrix3f R = euler_to_rotation_matrix(0, 0, 90);
        Matrix3f expected = Matrix3f::Zero();
        expected << 0, -1, 0,
                    1, 0, 0,
                    0, 0, 1;
        REQUIRE_THAT(R, Catch::Approx(expected).epsilon(1e-6));
    }

    SECTION("Combined Rotation") {
        // Test combined rotation
        Matrix3f R = euler_to_rotation_matrix(30, 45, 60);
        Matrix3f expected = Matrix3f::Zero();
        expected << 0.35355339, -0.5732233, 0.73919892,
                    0.61237244, 0.73919892, 0.28033009,
                    -0.70710678, 0.35355339, 0.61237244;
        REQUIRE_THAT(R, Catch::Approx(expected).epsilon(1e-5));
    }
}
