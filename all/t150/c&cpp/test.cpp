TEST_CASE("rgbToHex and hexToRgb") {
    
    // Test the basic logic of rgbToHex function
    SECTION("should correctly convert RGB to HEX") {
        RGB rgb = {255, 99, 71};
        std::string result = rgbToHex(rgb);
        REQUIRE(result == "#ff6347"); // Expected HEX code for RGB(255, 99, 71)
    }

    // Test the basic logic of hexToRgb function
    SECTION("should correctly convert HEX to RGB") {
        std::string hex = "#ff6347";
        auto result = hexToRgb(hex);
        REQUIRE(result.has_value());
        REQUIRE(result->r == 255);
        REQUIRE(result->g == 99);
        REQUIRE(result->b == 71); // Expected RGB object for HEX #ff6347
    }

    // Test the exception handling of rgbToHex function
    SECTION("should handle invalid RGB components gracefully") {
        RGB rgb = {300, -10, 128};
        std::string result = rgbToHex(rgb);
        REQUIRE(result == "#12c080"); // Invalid values (300, -10) should be clamped to "00", valid value should convert to "80"
    }

    // Test the exception handling of hexToRgb function
    SECTION("should return nullopt for invalid HEX strings") {
        std::string invalidHex = "#ggg123";
        auto result = hexToRgb(invalidHex);
        REQUIRE(!result.has_value()); // Invalid HEX code should return nullopt
    }

    // Test boundary values for rgbToHex function
    SECTION("should handle boundary values in RGB correctly") {
        RGB rgb = {0, 0, 0};
        std::string result = rgbToHex(rgb);
        REQUIRE(result == "#000000"); // Boundary RGB(0, 0, 0) should convert to #000000

        RGB rgbWhite = {255, 255, 255};
        std::string resultWhite = rgbToHex(rgbWhite);
        REQUIRE(resultWhite == "#ffffff"); // Boundary RGB(255, 255, 255) should convert to #ffffff
    }
}