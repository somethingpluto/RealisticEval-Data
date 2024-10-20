TEST_CASE("Test remove_parts_of_string function") {
    SECTION("Test with a string that has no uppercase letters") {
        std::vector<std::string> input = {"abcdefg"};
        std::vector<std::string> expected = {"abcdefg"};
        REQUIRE(remove_parts_of_string(input) == expected);
    }

    SECTION("Test with a string that has no lowercase letters") {
        std::vector<std::string> input = {"ABCDEFG"};
        std::vector<std::string> expected = {"ABCDEFG"};
        REQUIRE(remove_parts_of_string(input) == expected);
    }

    SECTION("Test with a string that has mixed cases") {
        std::vector<std::string> input = {"1234AbCde5678"};
        std::vector<std::string> expected = {"AbCde5678"};
        REQUIRE(remove_parts_of_string(input) == expected);
    }

    SECTION("Test with an empty string") {
        std::vector<std::string> input = {""};
        std::vector<std::string> expected = {""};
        REQUIRE(remove_parts_of_string(input) == expected);
    }

    SECTION("Test with a string that has only one uppercase letter") {
        std::vector<std::string> input = {"X"};
        std::vector<std::string> expected = {"X"};
        REQUIRE(remove_parts_of_string(input) == expected);
    }

    SECTION("Test with a string that has only one lowercase letter") {
        std::vector<std::string> input = {"y"};
        std::vector<std::string> expected = {"y"};
        REQUIRE(remove_parts_of_string(input) == expected);
    }
}