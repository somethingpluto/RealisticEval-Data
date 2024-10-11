TEST_CASE("RGB to HSV Conversion", "[rgb_to_hsv]") {
    REQUIRE(rgb_to_hsv(0, 0, 255) == std::make_tuple(240, 100, 100));
    // Add more test cases here
}