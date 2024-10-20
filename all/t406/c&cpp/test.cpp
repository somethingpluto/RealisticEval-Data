TEST_CASE("Test Colors", "[Colors]") {
    SECTION("Test the red color method") {
        const std::string input_text = "Hello";
        const std::string expected_output = "\033[91mHello\033[0m";
        REQUIRE(Colors::red(input_text) == expected_output);
    }

    SECTION("Test the green color method") {
        const std::string input_text = "Hello";
        const std::string expected_output = "\033[92mHello\033[0m";
        REQUIRE(Colors::green(input_text) == expected_output);
    }

    SECTION("Test the blue color method") {
        const std::string input_text = "Hello";
        const std::string expected_output = "\033[94mHello\033[0m";
        REQUIRE(Colors::blue(input_text) == expected_output);
    }

    SECTION("Test the yellow color method") {
        const std::string input_text = "Hello";
        const std::string expected_output = "\033[93mHello\033[0m";
        REQUIRE(Colors::yellow(input_text) == expected_output);
    }

    SECTION("Test the magenta color method") {
        const std::string input_text = "Hello";
        const std::string expected_output = "\033[95mHello\033[0m";
        REQUIRE(Colors::magenta(input_text) == expected_output);
    }

    SECTION("Test the cyan color method") {
        const std::string input_text = "Hello";
        const std::string expected_output = "\033[96mHello\033[0m";
        REQUIRE(Colors::cyan(input_text) == expected_output);
    }

    SECTION("Test combining different color methods") {
        const std::string input_text_red = Colors::red("Red");
        const std::string input_text_blue = Colors::blue("Blue");
        const std::string input_text_combined = input_text_red + " and " + input_text_blue;
        const std::string expected_output = "\033[91mRed\033[0m and \033[94mBlue\033[0m";
        REQUIRE(input_text_combined == expected_output);
    }
}