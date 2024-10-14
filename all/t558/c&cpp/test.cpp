TEST_CASE("Test conversion of angles", "[degrees_to_radians]") {
    SECTION("Test conversion of 0 degrees") {
        REQUIRE(std::abs(degrees_to_radians(0) - 0) < 1e-5);
    }

    SECTION("Test conversion of 90 degrees") {
        REQUIRE(std::abs(degrees_to_radians(90) - (M_PI / 2)) < 1e-5);
    }

    SECTION("Test conversion of 180 degrees") {
        REQUIRE(std::abs(degrees_to_radians(180) - M_PI) < 1e-5);
    }

    SECTION("Test conversion of 270 degrees") {
        REQUIRE(std::abs(degrees_to_radians(270) - (3 * M_PI / 2)) < 1e-5);
    }

    SECTION("Test conversion of 360 degrees") {
        REQUIRE(std::abs(degrees_to_radians(360) - (2 * M_PI)) < 1e-5);
    }

    SECTION("Test conversion of negative degrees") {
        REQUIRE(std::abs(degrees_to_radians(-90) - (-M_PI / 2)) < 1e-5);
    }

    SECTION("Test conversion of a large angle (720 degrees)") {
        REQUIRE(std::abs(degrees_to_radians(720) - (4 * M_PI)) < 1e-5);
    }
}