TEST_CASE("Test remove_triple_backticks function", "[remove_triple_backticks]") {
    SECTION("Empty list") {
        std::vector<std::string> input = {};
        std::vector<std::string> expected_output = {};
        REQUIRE(remove_triple_backticks(input) == expected_output);
    }

    SECTION("No triple backticks") {
        std::vector<std::string> input = {"Hello, world!", "`single`backtick"};
        std::vector<std::string> expected_output = {"Hello, world!", "`single`backtick"};
        REQUIRE(remove_triple_backticks(input) == expected_output);
    }

    SECTION("Single triple backticks") {
        std::vector<std::string> input = {"Hello, ```world!```"};
        std::vector<std::string> expected_output = {"Hello, world!"};
        REQUIRE(remove_triple_backticks(input) == expected_output);
    }

    SECTION("Multiple triple backticks") {
        std::vector<std::string> input = {"Hello, ```world!```", "Another ```example``` here."};
        std::vector<std::string> expected_output = {"Hello, world!", "Another example here."};
        REQUIRE(remove_triple_backticks(input) == expected_output);
    }

    SECTION("Triple backticks at the end") {
        std::vector<std::string> input = {"Hello, world!!!```"};
        std::vector<std::string> expected_output = {"Hello, world!!!"};
        REQUIRE(remove_triple_backticks(input) == expected_output);
    }
}