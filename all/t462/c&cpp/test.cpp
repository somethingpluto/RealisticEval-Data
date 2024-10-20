TEST_CASE("Test Spiral Order", "[spiralOrder]") {
    SECTION("Empty Matrix") {
        REQUIRE(spiralOrder({}) == std::vector<int>{});
    }

    SECTION("Single Row Matrix") {
        REQUIRE(spiralOrder({{1, 2, 3}}) == std::vector<int>({1, 2, 3}));
    }

    SECTION("Single Column Matrix") {
        REQUIRE(spiralOrder({{1}, {2}, {3}}) == std::vector<int>({1, 2, 3}));
    }

    SECTION("Square Matrix") {
        REQUIRE(spiralOrder({
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        }) == std::vector<int>({1, 2, 3, 6, 9, 8, 7, 4, 5}));
    }

    SECTION("Rectangle Matrix") {
        REQUIRE(spiralOrder({
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        }) == std::vector<int>({1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7}));
    }
}