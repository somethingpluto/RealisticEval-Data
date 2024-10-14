TEST_CASE("Test calculate_column_widths") {
    SECTION("Standard case") {
        std::vector<std::vector<std::string>> data = {
            {"Name", "Age", "City"},
            {"Alice", "22", "New York"},
            {"Bob", "30", "San Francisco"}
        };
        std::vector<int> expected = {5, 3, 13};
        REQUIRE(calculate_column_widths(data) == expected);
    }

    SECTION("Single element") {
        std::vector<std::vector<std::string>> data = {{"Name"}};
        std::vector<int> expected = {4};
        REQUIRE(calculate_column_widths(data) == expected);
    }

    SECTION("Varied length") {
        std::vector<std::vector<std::string>> data = {
            {"a", "bb", "ccc"},
            {"dddd", "ee", "f"}
        };
        std::vector<int> expected = {4, 2, 3};
        REQUIRE(calculate_column_widths(data) == expected);
    }

    SECTION("All empty strings") {
        std::vector<std::vector<std::string>> data = {
            {"", "", ""},
            {"", "", ""}
        };
        std::vector<int> expected = {0, 0, 0};
        REQUIRE(calculate_column_widths(data) == expected);
    }

    SECTION("Mixed content") {
        std::vector<std::vector<std::string>> data = {
            {"1234", "567", "890"},
            {"abc", "defg", "h"}
        };
        std::vector<int> expected = {4, 4, 3};
        REQUIRE(calculate_column_widths(data) == expected);
    }

    SECTION("Single column multiple rows") {
        std::vector<std::vector<std::string>> data = {
            {"one"},
            {"two"},
            {"three"}
        };
        std::vector<int> expected = {5};
        REQUIRE(calculate_column_widths(data) == expected);
    }
}