TEST_CASE("Test Bresenham Line Algorithm", "[Bresenham]") {
    SECTION("Horizontal Line") {
        std::vector<std::pair<int, int>> expected = {{1, 5}, {2, 5}, {3, 5}, {4, 5}, {5, 5}};
        REQUIRE(bresenham_line(1, 5, 5, 5) == expected);
    }

    SECTION("Vertical Line") {
        std::vector<std::pair<int, int>> expected = {{3, 2}, {3, 3}, {3, 4}, {3, 5}, {3, 6}};
        REQUIRE(bresenham_line(3, 2, 3, 6) == expected);
    }

    SECTION("Diagonal Line") {
        std::vector<std::pair<int, int>> expected = {{2, 2}, {3, 3}, {4, 4}, {5, 5}, {6, 6}};
        REQUIRE(bresenham_line(2, 2, 6, 6) == expected);
    }

    SECTION("Steep Slope") {
        std::vector<std::pair<int, int>> expected = {{1, 1}, {2, 2}, {2, 3}, {3, 4}, {3, 5}, {4, 6}};
        REQUIRE(bresenham_line(1, 1, 4, 6) == expected);
    }

    SECTION("Negative Slope") {
        std::vector<std::pair<int, int>> expected = {{5, 1}, {4, 2}, {3, 3}, {2, 4}, {1, 5}};
        REQUIRE(bresenham_line(5, 1, 1, 5) == expected);
    }
}