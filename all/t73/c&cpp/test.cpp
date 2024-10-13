TEST_CASE("TestDictOfListsToListOfDicts") {
    SECTION("test_standard_conversion") {
        // Test standard conversion with equal length lists
        std::map<std::string, std::vector<std::string>> dict_of_lists = {
            {"name", {"Alice", "Bob", "Charlie"}},
            {"age", {"25", "30", "35"}},
            {"city", {"New York", "Los Angeles", "Chicago"}}
        };
        std::vector<std::map<std::string, std::string>> expected_result = {
            {{"name", "Alice"}, {"age", "25"}, {"city", "New York"}},
            {{"name", "Bob"}, {"age", "30"}, {"city", "Los Angeles"}},
            {{"name", "Charlie"}, {"age", "35"}, {"city", "Chicago"}}
        };

        auto result = dict_of_lists_to_list_of_dicts(dict_of_lists);
        REQUIRE(result == expected_result);
    }

    SECTION("test_empty_lists") {
        // Test the function with empty lists
        std::map<std::string, std::vector<std::string>> dict_of_lists = {
            {"name", {}},
            {"age", {}},
            {"city", {}}
        };
        std::vector<std::map<std::string, std::string>> expected_result = {};

        auto result = dict_of_lists_to_list_of_dicts(dict_of_lists);
        REQUIRE(result == expected_result);
    }

    SECTION("test_single_element_lists") {
        // Test the function with single-element lists
        std::map<std::string, std::vector<std::string>> dict_of_lists = {
            {"name", {"Alice"}},
            {"age", {"25"}},
            {"city", {"New York"}}
        };
        std::vector<std::map<std::string, std::string>> expected_result = {
            {{"name", "Alice"}, {"age", "25"}, {"city", "New York"}}
        };

        auto result = dict_of_lists_to_list_of_dicts(dict_of_lists);
        REQUIRE(result == expected_result);
    }
}