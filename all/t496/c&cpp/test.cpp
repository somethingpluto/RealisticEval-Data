TEST_CASE("Test Pascal's Triangle Row") {
    SECTION("Test the 0th row of Pascal's Triangle") {
        REQUIRE(pascal_triangle_row(0) == std::vector<long long>({1}));
    }

    SECTION("Test the 1st row of Pascal's Triangle") {
        REQUIRE(pascal_triangle_row(1) == std::vector<long long>({1, 1}));
    }

    SECTION("Test the 2nd row of Pascal's Triangle") {
        REQUIRE(pascal_triangle_row(2) == std::vector<long long>({1, 2, 1}));
    }

    SECTION("Test the 3rd row of Pascal's Triangle") {
        REQUIRE(pascal_triangle_row(3) == std::vector<long long>({1, 3, 3, 1}));
    }

    SECTION("Test the 4th row of Pascal's Triangle") {
        REQUIRE(pascal_triangle_row(4) == std::vector<long long>({1, 4, 6, 4, 1}));
    }

    SECTION("Test the 5th row of Pascal's Triangle") {
        REQUIRE(pascal_triangle_row(5) == std::vector<long long>({1, 5, 10, 10, 5, 1}));
    }
}