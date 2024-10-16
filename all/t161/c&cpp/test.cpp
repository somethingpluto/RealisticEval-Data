TEST_CASE("generateCombinations") {
    SECTION("generates combinations for a single key with multiple values") {
        std::map<std::string, std::vector<int>> map = {{"a", {1, 2, 3}}};
        std::vector<std::vector<int>> expected = {{1}, {2}, {3}};
        REQUIRE(generateCombinations(map) == expected);
    }

    SECTION("generates combinations for multiple keys with single values") {
        std::map<std::string, std::vector<int>> map = {{"a", {1}}, {"b", {2}}};
        std::vector<std::vector<int>> expected = {{1, 2}};
        REQUIRE(generateCombinations(map) == expected);
    }

    SECTION("generates combinations for multiple keys with multiple values") {
        std::map<std::string, std::vector<int>> map = {{"a", {1, 2}}, {"b", {3, 4}}};
        std::vector<std::vector<int>> expected = {
            {1, 3}, {1, 4},
            {2, 3}, {2, 4}
        };
        REQUIRE(generateCombinations(map) == expected);
    }

    SECTION("handles an empty map") {
        std::map<std::string, std::vector<int>> map;
        std::vector<std::vector<int>> expected = {{}};
        REQUIRE(generateCombinations(map) == expected);
    }

    SECTION("handles keys with empty arrays as values") {
        std::map<std::string, std::vector<int>> map = {{"a", {}}, {"b", {1, 2}}};
        std::vector<std::vector<int>> expected = {};
        REQUIRE(generateCombinations(map) == expected);
    }
}