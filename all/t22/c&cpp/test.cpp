#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <stdexcept>
#include <tuple>
#include <cmath>

using namespace std;

using Point = tuple<float, float>;

float calculate_euclidean_distance(const Point& point1, const Point& point2) {
    // Extract coordinates from the input tuples
    float x1, y1, x2, y2;
    tie(x1, y1) = point1;
    tie(x2, y2) = point2;

    // Compute differences and Euclidean distance using the Pythagorean theorem
    float dx = x2 - x1;
    float dy = y2 - y1;

    return sqrt(dx * dx + dy * dy);
}

TEST_CASE("Basic functionality") {
    Point point1 = {0.0f, 0.0f};
    Point point2 = {3.0f, 4.0f};
    float expected_distance = 5.0f;
    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance).epsilon(0.001));
}

TEST_CASE("Negative coordinates") {
    Point point1 = {-1.0f, -1.0f};
    Point point2 = {-4.0f, -5.0f};
    float expected_distance = 5.0f;
    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance).epsilon(0.001));
}

TEST_CASE("Zero distance") {
    Point point1 = {2.0f, 3.0f};
    Point point2 = {2.0f, 3.0f};
    float expected_distance = 0.0f;
    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance).epsilon(0.001));
}

TEST_CASE("Large coordinates") {
    Point point1 = {1e6f, 1e6f};
    Point point2 = {1e6f + 3.0f, 1e6f + 4.0f};
    float expected_distance = 5.0f;
    REQUIRE(calculate_euclidean_distance(point1, point2) == Approx(expected_distance).epsilon(0.001));
}

TEST_CASE("Invalid input") {
    REQUIRE_THROWS_AS(calculate_euclidean_distance({0.0f, 0.0f}, "invalid_input"), invalid_argument);
}