TEST_CASE("TestFloatToRGB", "[floatToRGB]") {

    SECTION("Test pure red") {
        // Value at the lower boundary (0.0) should return pure red
        auto result = floatToRGB(0.0f);
        CHECK(result == std::make_tuple(255, 0, 0));
    }

    SECTION("Test pure green") {
        // Value at the upper boundary (1.0) should return pure green
        auto result = floatToRGB(1.0f);
        CHECK(result == std::make_tuple(0, 255, 0));
    }

    SECTION("Test midpoint") {
        // Value at 0.5 should return an equal mix of red and green
        auto result = floatToRGB(0.5f);
        CHECK(result == std::make_tuple(127, 127, 0));
    }

    SECTION("Test quarter point") {
        // Value at 0.25 should return more red than green
        auto result = floatToRGB(0.25f);
        CHECK(result == std::make_tuple(191, 63, 0));
    }

    SECTION("Test invalid value") {
        // Value outside the range [0, 1] should throw an exception
        CHECK_THROWS_AS(floatToRGB(1.5f), std::out_of_range);
    }
}