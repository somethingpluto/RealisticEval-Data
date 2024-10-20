TEST_CASE("Test format_comment function", "[format_comment]") {
    SECTION("Test with a short string that fits within max_length") {
        std::string input_string = "This is a test.";
        std::string expected_output = "# This is a test.";
        REQUIRE(format_comment(input_string) == expected_output);
    }

    SECTION("Test with a longer string that exceeds max_length") {
        std::string input_string = "This is a test of the format_comment function which should wrap long lines correctly.";
        std::string expected_output =
            "# This is a test of the format_comment function which should\n"
            "# wrap long lines correctly.";
        REQUIRE(format_comment(input_string, 60) == expected_output);
    }

    SECTION("Test with multiple lines of input") {
        std::string input_string = "First line.\nSecond line that is quite long and needs to be wrapped.";
        std::string expected_output =
            "# First line.\n"
            "# Second line that is quite long and needs to be wrapped.";
        REQUIRE(format_comment(input_string, 60) == expected_output);
    }

    SECTION("Test with a line that is exactly max_length characters long") {
        std::string input_string(60, 'A');  // 60 characters long
        std::string expected_output = "# " + std::string(60, 'A');
        REQUIRE(format_comment(input_string, 60) == expected_output);
    }

    SECTION("Test with an empty string") {
        std::string input_string = "";
        std::string expected_output = "# ";
        REQUIRE(format_comment(input_string) == expected_output);
    }
}