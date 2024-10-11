TEST_CASE("dictOfListsToListOfDicts", "[conversion]") {
    SECTION("Single key-value pair") {
        std::map<std::string, std::vector<int>> dict = {{"a", {1, 2, 3}}};
        std::vector<std::map<std::string, int>> expected = {{{"a", 1}}, {{"a", 2}}, {{"a", 3}}};
        REQUIRE(dictOfListsToListOfDicts(dict) == expected);
    }

    SECTION("Multiple key-value pairs") {
        std::map<std::string, std::vector<int>> dict = {{"a", {1, 2}}, {"b", {3, 4}}, {"c", {5, 6}}};
        std::vector<std::map<std::string, int>> expected = {{{"a", 1}, {"b", 3}, {"c", 5}}, {{"a", 2}, {"b", 4}, {"c", 6}}};
        REQUIRE(dictOfListsToListOfDicts(dict) == expected);
    }

    SECTION("Empty input") {
        std::map<std::string, std::vector<int>> dict = {};
        std::vector<std::map<std::string, int>> expected = {};
        REQUIRE(dictOfListsToListOfDicts(dict) == expected);
    }

    SECTION("Different lengths of lists") {
        std::map<std::string, std::vector<int>> dict = {{"a", {1, 2}}, {"b", {3}}};
        std::vector<std::map<std::string, int>> expected = {{{"a", 1}, {"b", 3}}, {{"a", 2}}};
        REQUIRE(dictOfListsToListOfDicts(dict) == expected);
    }
}