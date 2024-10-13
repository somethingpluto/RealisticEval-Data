TEST_CASE("Test Float to RGB Conversion") {
    SECTION("Pure Red") {
        // Value at the lower boundary (0.0) should return pure red
        auto result = float_to_rgb(0.0f);
        REQUIRE(std::get<0>(result) == 255);
        REQUIRE(std::get<1>(result) == 0);
        REQUIRE(std::get<2>(result) == 0);
    }

    SECTION("Pure Green") {
        // Value at the upper boundary (1.0) should return pure green
        auto result = float_to_rgb(1.0f);
        REQUIRE(std::get<0>(result) == 0);
        REQUIRE(std::get<1>(result) == 255);
        REQUIRE(std::get<2>(result) == 0);
    }

    SECTION("Midpoint") {
        // Value at 0.5 should return an equal mix of red and green, resulting in yellow
        auto result = float_to_rgb(0.5f);
        REQUIRE(std::get<0>(result) == 127);
        REQUIRE(std::get<1>(result) == 127);
        REQUIRE(std::get<2>(result) == 0);
    }

    SECTION("Quarter Point") {
        // Value at 0.25 should return more red than green
        auto result = float_to_rgb(0.25f);
        REQUIRE(std::get<0>(result) == 191);
        REQUIRE(std::get<1>(result) == 63);
        REQUIRE(std::get<2>(result) == 0);
    }

    SECTION("Invalid Value") {
        // Value outside the range [0, 1] should throw an exception
        REQUIRE_THROWS_AS(float_to_rgb(1.5f), std::invalid_argument);
    }
}