TEST_CASE("Test divide_list function", "[divide_list]") {
    SECTION("Even division") {
        std::vector<int> lst = {1, 2, 3, 4, 5, 6};
        int n = 3;
        std::vector<std::vector<int>> expected = {{1, 2}, {3, 4}, {5, 6}};
        REQUIRE(divide_list(lst, n) == expected);
    }

    SECTION("Uneven division") {
        std::vector<int> lst = {1, 2, 3, 4, 5, 6, 7};
        int n = 3;
        std::vector<std::vector<int>> expected = {{1, 2, 3}, {4, 5}, {6, 7}};
        REQUIRE(divide_list(lst, n) == expected);
    }

    SECTION("More parts than items") {
        std::vector<int> lst = {1, 2, 3};
        int n = 5;
        std::vector<std::vector<int>> expected = {{1}, {2}, {3}, {}, {}};
        REQUIRE(divide_list(lst, n) == expected);
    }

    SECTION("Single element") {
        std::vector<int> lst = {1};
        int n = 1;
        std::vector<std::vector<int>> expected = {{1}};
        REQUIRE(divide_list(lst, n) == expected);
    }

    SECTION("Empty list") {
        std::vector<int> lst = {};
        int n = 3;
        std::vector<std::vector<int>> expected = {{}, {}, {}};
        REQUIRE(divide_list(lst, n) == expected);
    }
}