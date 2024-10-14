TEST_CASE("removePunctuation", "[string]") {
    SECTION("removes punctuation from a simple sentence") {
        std::string input = "Hello, world!";
        std::string expected = "hello world";
        REQUIRE(removePunctuation(input) == expected);
    }

    SECTION("handles a string with no punctuation") {
        std::string input = "Hello world";
        std::string expected = "hello world";
        REQUIRE(removePunctuation(input) == expected);
    }

    SECTION("converts mixed case letters to lowercase") {
        std::string input = "HeLLo WoRLd!";
        std::string expected = "hello world";
        REQUIRE(removePunctuation(input) == expected);
    }

    SECTION("removes a variety of punctuation") {
        std::string input = "Life, in a nutshell: eat, sleep, code!";
        std::string expected = "life in a nutshell eat sleep code";
        REQUIRE(removePunctuation(input) == expected);
    }

    SECTION("trims whitespace from the ends of the string") {
        std::string input = "   What a wonderful world!   ";
        std::string expected = "what a wonderful world";
        REQUIRE(removePunctuation(input) == expected);
    }
}