#include <iostream>
#include <cmath>
#include <optional>
#include <tuple>

using namespace std;

using Point = pair<double, double>;
using Segment = pair<Point, Point>;

optional<Point> get_line_segment_intersection(const Segment &seg1, const Segment &seg2) {
    // Unpack segment points
    auto [x1, y1] = seg1.first;
    auto [x2, y2] = seg1.second;
    auto [x3, y3] = seg2.first;
    auto [x4, y4] = seg2.second;

    // Compute direction vectors and determinant
    double dx1 = x2 - x1, dy1 = y2 - y1;
    double dx2 = x4 - x3, dy2 = y4 - y3;
    double determinant = dx1 * dy2 - dx2 * dy1;

    // Check for parallel lines or identical segments
    if (abs(determinant) < 1e-10) {
        return nullopt;
    }

    // Calculate intersection parameters
    double t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant;
    double t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant;

    // Allow for a small tolerance in the intersection check
    double tolerance = 1e-10;

    // Check if intersection is within the bounds of the line segments
    if (0 - tolerance <= t1 && t1 <= 1 + tolerance && 0 - tolerance <= t2 && t2 <= 1 + tolerance) {
        double x = x1 + t1 * dx1;
        double y = y1 + t1 * dy1;
        return make_pair(round(x * 1e7) / 1e7, round(y * 1e7) / 1e7);
    }

    return nullopt;
}
