#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

HSL rgbToHsl(int r, int g, int b); // Function prototype

TEST_CASE("rgbToHsl function") {
    SECTION("converts pure red to HSL") {
        REQUIRE(rgbToHsl(255, 0, 0) == HSL{0, 100, 50});
    }

    SECTION("converts black to HSL") {
        REQUIRE(rgbToHsl(0, 0, 0) == HSL{0, 0, 0});
    }

    SECTION("converts white to HSL") {
        REQUIRE(rgbToHsl(255, 255, 255) == HSL{0, 0, 100});
    }

    SECTION("converts a color on the edge of RGB range") {
        REQUIRE(rgbToHsl(0, 255, 255) == HSL{180, 100, 50});
    }
}