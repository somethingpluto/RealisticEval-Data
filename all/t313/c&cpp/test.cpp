TEST_CASE("isBackgroundTooDarkOrBright", "[brightness]") {
    
    SECTION("should return 'dark' for a dark background color") {
        setBackgroundColor("rgb(30, 30, 30)");
        REQUIRE(isBackgroundTooDarkOrBright() == "dark");
    }

    SECTION("should return 'bright' for a bright background color") {
        setBackgroundColor("rgb(250, 250, 250)");
        REQUIRE(isBackgroundTooDarkOrBright() == "bright");
    }

    SECTION("should return 'normal' for a background color with normal brightness") {
        setBackgroundColor("rgb(150, 150, 150)");
        REQUIRE(isBackgroundTooDarkOrBright() == "normal");
    }

    SECTION("should correctly handle a bright color with high red component") {
        setBackgroundColor("rgb(255, 100, 100)");
        REQUIRE(isBackgroundTooDarkOrBright() == "normal");
    }

    SECTION("should correctly handle a dark color with low green and blue components") {
        setBackgroundColor("rgb(10, 10, 100)");
        REQUIRE(isBackgroundTooDarkOrBright() == "dark");
    }
}