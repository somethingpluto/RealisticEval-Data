TEST_CASE("Test remove_triple_backticks functionality") {
    SECTION("Basic functionality") {
        // Test basic functionality
        std::vector<std::string> input_strings = {"Here is ```code``` example", "Another ```example``` here", "No backticks here"};
        std::vector<std::string> expected_output = {"Here is code example", "Another example here", "No backticks here"};
        REQUIRE(remove_triple_backticks(input_strings) == expected_output);
    }

    SECTION("Strings with multiple instances of triple backticks") {
        // Test strings containing multiple instances of triple backticks
        std::vector<std::string> input_strings = {"Multiple ```backticks``` in ```one``` string"};
        std::vector<std::string> expected_output = {"Multiple backticks in one string"};
        REQUIRE(remove_triple_backticks(input_strings) == expected_output);
    }

    SECTION("Empty strings") {
        // Test with empty strings
        std::vector<std::string> input_strings = {""};
        std::vector<std::string> expected_output = {""};
        REQUIRE(remove_triple_backticks(input_strings) == expected_output);
    }

    SECTION("Strings that do not contain triple backticks") {
        // Test strings that do not contain triple backticks
        std::vector<std::string> input_strings = {"Just a normal string", "Another normal string"};
        std::vector<std::string> expected_output = {"Just a normal string", "Another normal string"};
        REQUIRE(remove_triple_backticks(input_strings) == expected_output);
    }

    SECTION("Edge cases") {
        // Test edge cases like strings made entirely of triple backticks
        std::vector<std::string> input_strings = {"```", "```more```", "text``````"};
        std::vector<std::string> expected_output = {"", "more", "text"};
        REQUIRE(remove_triple_backticks(input_strings) == expected_output);
    }
}