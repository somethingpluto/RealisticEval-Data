TEST_CASE("Test RGB to HSV conversion") {
    SECTION("Test conversion of pure red color") {
        int r = 255, g = 0, b = 0;
        auto expected_result = std::make_tuple(0.0, 100.0, 100.0);
        auto result = rgb_to_hsv(r, g, b);
        REQUIRE(std::get<0>(result) == std::get<0>(expected_result));
        REQUIRE(std::get<1>(result) == std::get<1>(expected_result));
        REQUIRE(std::get<2>(result) == std::get<2>(expected_result));
    }

    SECTION("Test conversion of pure green color") {
        int r = 0, g = 255, b = 0;
        auto expected_result = std::make_tuple(120.0, 100.0, 100.0);
        auto result = rgb_to_hsv(r, g, b);
        REQUIRE(std::get<0>(result) == std::get<0>(expected_result));
        REQUIRE(std::get<1>(result) == std::get<1>(expected_result));
        REQUIRE(std::get<2>(result) == std::get<2>(expected_result));
    }

    SECTION("Test conversion of pure blue color") {
        int r = 0, g = 0, b = 255;
        auto expected_result = std::make_tuple(240.0, 100.0, 100.0);
        auto result = rgb_to_hsv(r, g, b);
        REQUIRE(std::get<0>(result) == std::get<0>(expected_result));
        REQUIRE(std::get<1>(result) == std::get<1>(expected_result));
        REQUIRE(std::get<2>(result) == std::get<2>(expected_result));
    }

    SECTION("Test conversion of white color") {
        int r = 255, g = 255, b = 255;
        auto expected_result = std::make_tuple(0.0, 0.0, 100.0);
        auto result = rgb_to_hsv(r, g, b);
        REQUIRE(std::get<0>(result) == std::get<0>(expected_result));
        REQUIRE(std::get<1>(result) == std::get<1>(expected_result));
        REQUIRE(std::get<2>(result) == std::get<2>(expected_result));
    }

    SECTION("Test conversion of black color") {
        int r = 0, g = 0, b = 0;
        auto expected_result = std::make_tuple(0.0, 0.0, 0.0);
        auto result = rgb_to_hsv(r, g, b);
        REQUIRE(std::get<0>(result) == std::get<0>(expected_result));
        REQUIRE(std::get<1>(result) == std::get<1>(expected_result));
        REQUIRE(std::get<2>(result) == std::get<2>(expected_result));
    }
}