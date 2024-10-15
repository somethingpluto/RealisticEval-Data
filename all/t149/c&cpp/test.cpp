TEST_CASE("hslToRgb", "[color]") {
    SECTION("Converts black (0% lightness)") {
        RGB color = hslToRgb(0, 0, 0);
        REQUIRE(color.r == 0);
        REQUIRE(color.g == 0);
        REQUIRE(color.b == 0);
    }

    SECTION("Converts white (100% lightness)") {
        RGB color = hslToRgb(0, 0, 1);
        REQUIRE(color.r == 255);
        REQUIRE(color.g == 255);
        REQUIRE(color.b == 255);
    }

    SECTION("Converts red (hue at 0)") {
        RGB color = hslToRgb(0, 1, 0.5);
        REQUIRE(color.r == 255);
        REQUIRE(color.g == 0);
        REQUIRE(color.b == 0);
    }

    SECTION("Converts green (hue at 120)") {
        RGB color = hslToRgb(120, 1, 0.5);
        REQUIRE(color.r == 0);
        REQUIRE(color.g == 255);
        REQUIRE(color.b == 0);
    }

    SECTION("Converts blue (hue at 240)") {
        RGB color = hslToRgb(240, 1, 0.5);
        REQUIRE(color.r == 0);
        REQUIRE(color.g == 0);
        REQUIRE(color.b == 255);
    }

    SECTION("Handles edge case with maximum hue (360 equivalent to 0)") {
        RGB color = hslToRgb(360, 1, 0.5);
        REQUIRE(color.r == 255);
        REQUIRE(color.g == 0);
        REQUIRE(color.b == 0);
    }
}