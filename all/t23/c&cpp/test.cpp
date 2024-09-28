#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <cmath>
#include <optional>
#include <tuple>

using namespace std;

using Point = pair<double, double>;
using Segment = pair<Point, Point>;

optional<Point> get_line_segment_intersection(const Segment &seg1, const Segment &seg2) {
    auto [x1, y1] = seg1.first;
    auto [x2, y2] = seg1.second;
    auto [x3, y3] = seg2.first;
    auto [x4, y4] = seg2.second;

    double dx1 = x2 - x1, dy1 = y2 - y1;
    double dx2 = x4 - x3, dy2 = y4 - y3;
    double determinant = dx1 * dy2 - dx2 * dy1;

    if (abs(determinant) < 1e-10) {
        return nullopt;
    }

    double t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant;
    double t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant;

    double tolerance = 1e-10;

    if (0 - tolerance <= t1 && t1 <= 1 + tolerance && 0 - tolerance <= t2 && t2 <= 1 + tolerance) {
        double x = x1 + t1 * dx1;
        double y = y1 + t1 * dy1;
        return make_pair(round(x * 1e7) / 1e7, round(y * 1e7) / 1e7);
    }

    return nullopt;
}

TEST_CASE("test_intersecting_lines") {
    auto result = get_line_segment_intersection({{1, 1}, {4, 4}}, {{1, 4}, {4, 1}});
    REQUIRE(result.has_value());
    REQUIRE(result.value() == make_pair(2.5, 2.5));
}

TEST_CASE("test_parallel_lines") {
    auto result = get_line_segment_intersection({{1, 1}, {4, 4}}, {{2, 2}, {5, 5}});
    REQUIRE_FALSE(result.has_value());
}

TEST_CASE("test_no_intersection") {
    auto result = get_line_segment_intersection({{1, 1}, {2, 2}}, {{3, 3}, {4, 4}});
    REQUIRE_FALSE(result.has_value());
}

TEST_CASE("test_intersection_in_middle") {
    auto result = get_line_segment_intersection({{0, 0}, {4, 4}}, {{0, 4}, {4, 0}});
    REQUIRE(result.has_value());
    REQUIRE(abs(result->first - 2.0) < 1e-7);
    REQUIRE(abs(result->second - 2.0) < 1e-7);
}

TEST_CASE("test_identical_segments") {
    auto result = get_line_segment_intersection({{1, 1}, {4, 4}}, {{1, 1}, {4, 4}});
    REQUIRE_FALSE(result.has_value());
}