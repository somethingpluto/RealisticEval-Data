#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <tuple>

// Assume rgbToHsv function is defined as previously discussed

TEST_CASE("RGB to HSV conversion", "[rgbToHsv]") {
    SECTION("Pure red color") {
        int r = 255, g = 0, b = 0;
        auto [h, s, v] = rgbToHsv(r, g, b);
        REQUIRE(h == Approx(0).margin(1e-2));
        REQUIRE(s == Approx(1).margin(1e-2));
        REQUIRE(v == Approx(1).margin(1e-2));
    }

    SECTION("Pure green color") {
        int r = 0, g = 255, b = 0;
        auto [h, s, v] = rgbToHsv(r, g, b);
        REQUIRE(h == Approx(120).margin(1e-2));
        REQUIRE(s == Approx(1).margin(1e-2));
        REQUIRE(v == Approx(1).margin(1e-2));
    }

    SECTION("Pure blue color") {
        int r = 0, g = 0, b = 255;
        auto [h, s, v] = rgbToHsv(r, g, b);
        REQUIRE(h == Approx(240).margin(1e-2));
        REQUIRE(s == Approx(1).margin(1e-2));
        REQUIRE(v == Approx(1).margin(1e-2));
    }

    SECTION("White color") {
        int r = 255, g = 255, b = 255;
        auto [h, s, v] = rgbToHsv(r, g, b);
        REQUIRE(h == Approx(0).margin(1e-2)); // Hue for white can be considered undefined but 0 is traditionally used
        REQUIRE(s == Approx(0).margin(1e-2));
        REQUIRE(v == Approx(1).margin(1e-2));
    }

    SECTION("Black color") {
        int r = 0, g = 0, b = 0;
        auto [h, s, v] = rgbToHsv(r, g, b);
        REQUIRE(h == Approx(0).margin(1e-2)); // Hue for black can be considered undefined but 0 is traditionally used
        REQUIRE(s == Approx(0).margin(1e-2));
        REQUIRE(v == Approx(0).margin(1e-2));
    }
}