#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>

struct Coordinates {
    double x;
    double y;
};

// Function prototype
Coordinates getBezierPoint(double t, const std::vector<Coordinates>& points);

TEST_CASE("getBezierPoint", "[Bezier]") {
    // Test case 1: Test with a simple linear curve
    SECTION("should return the midpoint of two points") {
        std::vector<Coordinates> points = {{0, 0}, {2, 2}};
        Coordinates result = getBezierPoint(0.5, points);
        REQUIRE(result.x == Approx(1));
        REQUIRE(result.y == Approx(1));
    }

    // Test case 2: Test with three points (quadratic curve)
    SECTION("should return the correct point on a quadratic Bézier curve") {
        std::vector<Coordinates> points = {{0, 0}, {1, 2}, {2, 0}};
        Coordinates result = getBezierPoint(0.5, points);
        REQUIRE(result.x == Approx(1));
        REQUIRE(result.y == Approx(1));
    }

    // Test case 3: Test with four points (cubic curve)
    SECTION("should return the correct point on a cubic Bézier curve") {
        std::vector<Coordinates> points = {{0, 0}, {1, 3}, {3, 1}, {4, 0}};
        Coordinates result = getBezierPoint(0.5, points);
        REQUIRE(result.x == Approx(2));
        REQUIRE(result.y == Approx(1.5));
    }

    // Test case 4: Test with single point (edge case)
    SECTION("should return the only point when there is a single control point") {
        std::vector<Coordinates> points = {{5, 5}};
        Coordinates result = getBezierPoint(0.5, points);
        REQUIRE(result.x == Approx(5));
        REQUIRE(result.y == Approx(5));
    }

    // Test case 5: Test with extreme t value (0)
    SECTION("should return the first control point when t is 0") {
        std::vector<Coordinates> points = {{0, 0}, {5, 5}};
        Coordinates result = getBezierPoint(0, points);
        REQUIRE(result.x == Approx(0));
        REQUIRE(result.y == Approx(0));
    }

    // Test case 6: Test with extreme t value (1)
    SECTION("should return the last control point when t is 1") {
        std::vector<Coordinates> points = {{0, 0}, {5, 5}};
        Coordinates result = getBezierPoint(1, points);
        REQUIRE(result.x == Approx(5));
        REQUIRE(result.y == Approx(5));
    }
}