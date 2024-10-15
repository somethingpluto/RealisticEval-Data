TEST_CASE("convertCamelCaseToSentence") {
    SECTION("should convert a simple camelCase string to a sentence") {
        std::string input = "thisIsTest";
        std::string expectedOutput = "This is test";
        REQUIRE(camelCaseToCapitalizedWithSpaces(input) == expectedOutput);
    }

    SECTION("should handle single word starting with lowercase") {
        std::string input = "example";
        std::string expectedOutput = "Example";
        REQUIRE(camelCaseToCapitalizedWithSpaces(input) == expectedOutput);
    }

    SECTION("should handle a camelCase string with multiple uppercase letters") {
        std::string input = "thisIsAnExampleString";
        std::string expectedOutput = "This is an example string";
        REQUIRE(camelCaseToCapitalizedWithSpaces(input) == expectedOutput);
    }

    SECTION("should handle a single uppercase letter") {
        std::string input = "aSingleUppercaseLetterX";
        std::string expectedOutput = "A single uppercase letter x";
        REQUIRE(camelCaseToCapitalizedWithSpaces(input) == expectedOutput);
    }

    SECTION("should handle an already capitalized string") {
        std::string input = "AlreadyCapitalized";
        std::string expectedOutput = "Already capitalized";
        REQUIRE(camelCaseToCapitalizedWithSpaces(input) == expectedOutput);
    }
}