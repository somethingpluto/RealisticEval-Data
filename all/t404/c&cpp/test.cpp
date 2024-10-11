TEST_CASE("Power of matrix with zero exponent", "[matrix_power]") {
    std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}};
    std::vector<std::vector<int>> expected = {{1, 2}, {3, 4}};
    REQUIRE(power(matrix, 0) == expected);
}

TEST_CASE("Power of matrix with one exponent", "[matrix_power]") {
    std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}};
    std::vector<std::vector<int>> expected = {{1, 2}, {3, 4}};
    REQUIRE(power(matrix, 1) == expected);
}

TEST_CASE("Power of matrix with positive exponent", "[matrix_power]") {
    std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}};
    std::vector<std::vector<int>> expected = {{7, 10}, {15, 22}};
    REQUIRE(power(matrix, 2) == expected);
}

TEST_CASE("Negative exponent throws exception", "[matrix_power]") {
    std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}};
    REQUIRE_THROWS_AS(power(matrix, -1), std::invalid_argument);
}

TEST_CASE("Non-square matrix throws exception", "[matrix_power]") {
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}};
    REQUIRE_THROWS(power(matrix, 2));
}