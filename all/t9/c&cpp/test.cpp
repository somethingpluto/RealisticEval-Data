#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>

bool is_point_on_line(const std::vector<int>& A, const std::vector<int>& B, const std::vector<int>& C) {
    int x_a = A[0], y_a = A[1];
    int x_b = B[0], y_b = B[1];
    int x_c = C[0], y_c = C[1];

    // Handle the vertical line case
    if (x_a == x_b) {
        return x_c == x_a;  // C must also have the same x-coordinate
    }

    // Check if slopes of AC and BC are equal
    return (y_c - y_a) * (x_b - x_a) == (y_b - y_a) * (x_c - x_a);
}

TEST_CASE("Test is_point_on_line functionality") {
    SECTION("Point on the line") {
        std::vector<int> A = {0, 0};
        std::vector<int> B = {10, 10};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point not on the line") {
        std::vector<int> A = {0, 0};
        std::vector<int> B = {10, 10};
        std::vector<int> C = {5, 6};
        REQUIRE_FALSE(is_point_on_line(A, B, C));
    }

    SECTION("Point on a vertical line") {
        std::vector<int> A = {5, 0};
        std::vector<int> B = {5, 10};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point on a horizontal line") {
        std::vector<int> A = {0, 5};
        std::vector<int> B = {10, 5};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point not on a vertical line") {
        std::vector<int> A = {5, 0};
        std::vector<int> B = {5, 10};
        std::vector<int> C = {6, 5};
        REQUIRE_FALSE(is_point_on_line(A, B, C));
    }
}