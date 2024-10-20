TEST_CASE("TestGenerateCombinations") {

    SECTION("Empty input") {
        std::vector<std::vector<std::string>> input_data = {};
        std::vector<std::vector<std::string>> expected = {};
        REQUIRE(generate_combinations(input_data) == expected);
    }

    SECTION("Single empty list") {
        std::vector<std::vector<std::string>> input_data = {{}};
        std::vector<std::vector<std::string>> expected = {};
        REQUIRE(generate_combinations(input_data) == expected);
    }

    SECTION("Single non-empty list") {
        std::vector<std::vector<std::string>> input_data = {{"a", "b", "c"}};
        std::vector<std::vector<std::string>> expected = {{"a"}, {"b"}, {"c"}};
        REQUIRE(generate_combinations(input_data) == expected);
    }

    SECTION("Multiple lists") {
        std::vector<std::vector<std::string>> input_data = {{"a", "b"}, {"1", "2"}};
        std::vector<std::vector<std::string>> expected = {{"a", "1"}, {"a", "2"}, {"b", "1"}, {"b", "2"}};
        REQUIRE(generate_combinations(input_data) == expected);
    }

    SECTION("Input containing empty list") {
        std::vector<std::vector<std::string>> input_data = {{"a", "b"}, {}, {"1", "2"}};
        std::vector<std::vector<std::string>> expected = {};
        REQUIRE(generate_combinations(input_data) == expected);
    }
}