#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <tuple>

// Assuming hslToRgb function is defined somewhere above or in an included header

TEST_CASE("hslToRgb function", "[color]") {
    SECTION("converts pure red hue correctly") {
        auto [r, g, b] = hslToRgb(0, 100, 50);
        REQUIRE(r == 255);
        REQUIRE(g == 0);
        REQUIRE(b == 0);
    }

    SECTION("returns gray for zero saturation") {
        auto [r, g, b] = hslToRgb(240, 0, 50);
        REQUIRE(r == 128);
        REQUIRE(g == 128);
        REQUIRE(b == 128);
    }

    SECTION("returns white for full lightness") {
        auto [r, g, b] = hslToRgb(120, 50, 100);
        REQUIRE(r == 255);
        REQUIRE(g == 255);
        REQUIRE(b == 255);
    }

    SECTION("converts full saturation and mid lightness blue correctly") {
        auto [r, g, b] = hslToRgb(240, 100, 50);
        REQUIRE(r == 0);
        REQUIRE(g == 0);
        REQUIRE(b == 255);
    }

    SECTION("handles edge hue at 360 degrees correctly") {
        auto [r, g, b] = hslToRgb(360, 100, 50);
        REQUIRE(r == 255);
        REQUIRE(g == 0);
        REQUIRE(b == 0); // Should be the same as hue 0
    }
}