#include <vector>
#include <iostream>

// Function to get elements of the matrix in spiral order
std::vector<int> spiralOrder(const std::vector<std::vector<int>>& matrix) {
    std::vector<int> result;
    if (matrix.empty()) return result;

    int rows = matrix.size();
    int cols = matrix[0].size();
    int top = 0, bottom = rows - 1, left = 0, right = cols - 1;

    while (top <= bottom && left <= right) {
        // Traverse from left to right along the top row
        for (int i = left; i <= right; ++i) {
            result.push_back(matrix[top][i]);
        }
        ++top;

        // Traverse downwards along the right column
        for (int i = top; i <= bottom; ++i) {
            result.push_back(matrix[i][right]);
        }
        --right;

        // Traverse from right to left along the bottom row
        if (top <= bottom) {
            for (int i = right; i >= left; --i) {
                result.push_back(matrix[bottom][i]);
            }
            --bottom;
        }

        // Traverse upwards along the left column
        if (left <= right) {
            for (int i = bottom; i >= top; --i) {
                result.push_back(matrix[i][left]);
            }
            ++left;
        }
    }

    return result;
}

// Test cases using Catch2
#define CATCH_CONFIG_MAIN
#include "catch.hpp"

TEST_CASE("Spiral Order", "[spiral_order]") {
    SECTION("Empty Matrix") {
        std::vector<std::vector<int>> matrix = {};
        REQUIRE(spiralOrder(matrix).empty());
    }

    SECTION("Single Row") {
        std::vector<std::vector<int>> matrix = {{1, 2, 3}};
        std::vector<int> expected = {1, 2, 3};
        REQUIRE(spiralOrder(matrix) == expected);
    }

    SECTION("Single Column") {
        std::vector<std::vector<int>> matrix = {{1}, {2}, {3}};
        std::vector<int> expected = {1, 2, 3};
        REQUIRE(spiralOrder(matrix) == expected);
    }

    SECTION("2x2 Matrix") {
        std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}};
        std::vector<int> expected = {1, 2, 4, 3};
        REQUIRE(spiralOrder(matrix) == expected);
    }

    SECTION("3x3 Matrix") {
        std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        std::vector<int> expected = {1, 2, 3, 6, 9, 8, 7, 4, 5};
        REQUIRE(spiralOrder(matrix) == expected);
    }

    SECTION("4x3 Matrix") {
        std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
        std::vector<int> expected = {1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8};
        REQUIRE(spiralOrder(matrix) == expected);
    }
}