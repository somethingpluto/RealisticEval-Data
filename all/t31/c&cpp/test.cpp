TEST_CASE("Test calculate_red_proportion", "[calculate_red_proportion]") {
    SECTION("All red pixels") {
        // All pixels are fully red
        std::vector<std::tuple<int, int, int>> pixels = {{255, 0, 0}, {255, 0, 0}, {255, 0, 0}};
        float result = calculate_red_proportion(pixels);
        REQUIRE_THAT(result, Catch::Matchers::WithinAbs(1.0f, 0.001));
    }

    SECTION("No red pixels") {
        // No red component in any pixel
        std::vector<std::tuple<int, int, int>> pixels = {{0, 255, 0}, {0, 0, 255}, {0, 255, 255}};
        float result = calculate_red_proportion(pixels);
        REQUIRE_THAT(result, Catch::Matchers::WithinAbs(0.0f, 0.001));
    }

    SECTION("Empty pixel list") {
        // Empty list of pixels
        std::vector<std::tuple<int, int, int>> pixels = {};
        float result = calculate_red_proportion(pixels);
        REQUIRE_THAT(result, Catch::Matchers::WithinAbs(0.0f, 0.001));
    }

    SECTION("All black pixels") {
        // All pixels are black
        std::vector<std::tuple<int, int, int>> pixels = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        float result = calculate_red_proportion(pixels);
        REQUIRE_THAT(result, Catch::Matchers::WithinAbs(0.0f, 0.001));
    }
}