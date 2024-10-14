TEST_CASE("Test conversion of various angles", "[RadiansToDegrees]") {
    SECTION("Test conversion of 0 radians") {
        REQUIRE(radians_to_degrees(0) == 0);
    }

    SECTION("Test conversion of π/2 radians") {
        REQUIRE_THAT(radians_to_degrees(M_PI / 2), Catch::Matchers::WithinAbs(90, 0.00001));
    }

    SECTION("Test conversion of π radians") {
        REQUIRE_THAT(radians_to_degrees(M_PI), Catch::Matchers::WithinAbs(180, 0.00001));
    }

    SECTION("Test conversion of 3π/2 radians") {
        REQUIRE_THAT(radians_to_degrees(3 * M_PI / 2), Catch::Matchers::WithinAbs(270, 0.00001));
    }

    SECTION("Test conversion of 2π radians") {
        REQUIRE_THAT(radians_to_degrees(2 * M_PI), Catch::Matchers::WithinAbs(360, 0.00001));
    }

    SECTION("Test conversion of -π/2 radians") {
        REQUIRE_THAT(radians_to_degrees(-M_PI / 2), Catch::Matchers::WithinAbs(-90, 0.00001));
    }

    SECTION("Test conversion of a large angle (4π radians)") {
        REQUIRE_THAT(radians_to_degrees(4 * M_PI), Catch::Matchers::WithinAbs(720, 0.00001));
    }
}