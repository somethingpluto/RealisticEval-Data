#define CATCH_CONFIG_MAIN  // This tells Catch2 to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>
#include <string>
#include "your_rainbow_generator_header.h"  // Include your header where `rainbowHexGenerator` is declared

TEST_CASE("RainbowHexGenerator", "[rainbow]") {
    // Define rainbow colors
    std::vector<std::string> rainbow_colors = {
        "#FF0000",  // Red
        "#FF7F00",  // Orange
        "#FFFF00",  // Yellow
        "#00FF00",  // Green
        "#0000FF",  // Blue
        "#4B0082",  // Indigo
        "#8A2BE2"   // Violet
    };

    SECTION("No intermediates") {
        // Test with zero intermediates
        std::vector<std::string> result = rainbowHexGenerator(0);
        REQUIRE(result == rainbow_colors);
    }

    SECTION("One intermediate") {
        // Test with one intermediate color between each main color
        std::vector<std::string> result = rainbowHexGenerator(1);
        // Check if the length is correct (7 main + 6 intermediates)
        REQUIRE(result.size() == 13);
    }

    SECTION("Include endpoints") {
        // Test including the endpoint (wrap-around) interpolation
        std::vector<std::string> result = rainbowHexGenerator(1, true);
        // Check if the length is correct (7 main + 7 intermediates including wrap-around)
        REQUIRE(result.size() == 14);
    }

    SECTION("High number of intermediates") {
        // Test with a high number of intermediates to check gradient smoothness
        std::vector<std::string> result = rainbowHexGenerator(10);
        // Check if the length is correct (7 main + 60 intermediates)
        REQUIRE(result.size() == 67);
    }
}