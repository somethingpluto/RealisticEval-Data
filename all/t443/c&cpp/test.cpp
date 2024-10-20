TEST_CASE("Test compress_whitespace function", "[compress_whitespace]") {
    SECTION("Test with a string containing single spaces") {
        std::string input = "This is a test string.";
        std::string expected = "This is a test string.";
        REQUIRE(compress_whitespace(input) == expected);
    }

    SECTION("Test with a string containing multiple spaces") {
        std::string input = "This    is  a   test   string.";
        std::string expected = "This is a test string.";
        REQUIRE(compress_whitespace(input) == expected);
    }

    SECTION("Test with leading and trailing spaces") {
        std::string input = "   Leading and trailing spaces   ";
        std::string expected = "Leading and trailing spaces";
        REQUIRE(compress_whitespace(input) == expected);
    }

    SECTION("Test with a string containing only spaces") {
        std::string input = "       ";
        std::string expected = "";
        REQUIRE(compress_whitespace(input) == expected);
    }

    SECTION("Test with an empty string") {
        std::string input = "";
        std::string expected = "";
        REQUIRE(compress_whitespace(input) == expected);
    }
}