#include <catch2/catch_test_macros.hpp>
#include <vector>

TEST_CASE("Test transposing a square matrix", "[transpose_matrix]") {
    std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}};
    std::vector<std::vector<int>> expected = {{1, 3}, {2, 4}};
    auto result = transpose_matrix(matrix);
    REQUIRE(result == expected);
}

TEST_CASE("Test transposing a rectangular matrix", "[transpose_matrix]") {
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}};
    std::vector<std::vector<int>> expected = {{1, 4}, {2, 5}, {3, 6}};
    auto result = transpose_matrix(matrix);
    REQUIRE(result == expected);
}

TEST_CASE("Test transposing a matrix with an empty row", "[transpose_matrix]") {
    std::vector<std::vector<int>> matrix = {{}, {}};
    std::vector<std::vector<int>> expected = {};
    auto result = transpose_matrix(matrix);
    REQUIRE(result == expected);
}

TEST_CASE("Test transposing a matrix with a single element", "[transpose_matrix]") {
    std::vector<std::vector<int>> matrix = {{5}};
    std::vector<std::vector<int>> expected = {{5}};
    auto result = transpose_matrix(matrix);
    REQUIRE(result == expected);
}
