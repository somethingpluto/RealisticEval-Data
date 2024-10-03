TEST_CASE("Hue to RGB Conversion Tests") {
    SECTION("Hue 0 (Red)") {
        auto [r, g, b] = hueToRGB(0);
        REQUIRE(r == 255);
        REQUIRE(g == 0);
        REQUIRE(b == 0);
    }

    SECTION("Hue 120 (Green)") {
        auto [r, g, b] = hueToRGB(120);
        REQUIRE(r == 0);
        REQUIRE(g == 255);
        REQUIRE(b == 0);
    }

    SECTION("Hue 240 (Blue)") {
        auto [r, g, b] = hueToRGB(240);
        REQUIRE(r == 0);
        REQUIRE(g == 0);
        REQUIRE(b == 255);
    }

    SECTION("Hue 60 (Yellow)") {
        auto [r, g, b] = hueToRGB(60);
        REQUIRE(r == 255);
        REQUIRE(g == 255);
        REQUIRE(b == 0);
    }

    SECTION("Hue 180 (Cyan)") {
        auto [r, g, b] = hueToRGB(180);
        REQUIRE(r == 0);
        REQUIRE(g == 255);
        REQUIRE(b == 255);
    }

    SECTION("Hue 300 (Magenta)") {
        auto [r, g, b] = hueToRGB(300);
        REQUIRE(r == 255);
        REQUIRE(g == 0);
        REQUIRE(b == 255);
    }

}