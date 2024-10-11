TEST_CASE("Colors Test Cases", "[colors]") {
    SECTION("Red Color") {
        REQUIRE(Colors::red("Hello") == "\033[1;31mHello\033[0m");
    }

    SECTION("Green Color") {
        REQUIRE(Colors::green("World") == "\033[1;32mWorld\033[0m");
    }

    SECTION("Blue Color") {
        REQUIRE(Colors::blue("Catch2") == "\033[1;34mCatch2\033[0m");
    }

    SECTION("Yellow Color") {
        REQUIRE(Colors::yellow("Test") == "\033[1;33mTest\033[0m");
    }

    SECTION("Magenta Color") {
        REQUIRE(Colors::magenta("Case") == "\033[1;35mCase\033[0m");
    }

    SECTION("Cyan Color") {
        REQUIRE(Colors::cyan("Example") == "\033[1;36mExample\033[0m");
    }
}