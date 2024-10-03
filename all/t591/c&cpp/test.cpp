TEST_CASE("Color RGB Values Test") {
    // Define an array of colors and their expected RGB values
    struct ColorTest {
        Color color;
        RGB expectedRGB;
    };

    ColorTest colorTests[] = {
        {Color::RED, {255, 0, 0}},
        {Color::GREEN, {0, 255, 0}},
        {Color::BLUE, {0, 0, 255}},
        {Color::YELLOW, {255, 255, 0}},
        {Color::MAGENTA, {255, 0, 255}},
        {Color::CYAN, {0, 255, 255}},
        {Color::WHITE, {255, 255, 255}},
        {Color::BLACK, {0, 0, 0}},
        {Color::ORANGE, {255, 165, 0}},
        {Color::PURPLE, {128, 0, 128}},
        {Color::PINK, {255, 192, 203}},
        {Color::BROWN, {165, 42, 42}}
    };

    for (const auto& test : colorTests) {
        RGB rgb = getColorRGB(test.color);
        REQUIRE(rgb.r == test.expectedRGB.r);
        REQUIRE(rgb.g == test.expectedRGB.g);
        REQUIRE(rgb.b == test.expectedRGB.b);
    }
}