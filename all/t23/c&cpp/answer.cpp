#include <iostream>
#include <utility>
#include <cmath>

// Define a union type for the return value
union IntersectionResult {
    std::pair<double, double> point;
    bool isNone;

    IntersectionResult() : isNone(true) {}
    IntersectionResult(double x, double y) : point(x, y), isNone(false) {}

    // Destructor
    ~IntersectionResult() {}

    // Equality operator for checking if the result is None
    bool operator==(const std::pair<double, double>& p) const {
        return !isNone && point == p;
    }

    // Equality operator for checking if the result is None
    bool operator==(bool none) const {
        return isNone == none;
    }
};

IntersectionResult getLineSegmentIntersection(const std::pair<std::pair<double, double>, std::pair<double, double>>& seg1,
                                              const std::pair<std::pair<double, double>, std::pair<double, double>>& seg2) {
    // Unpack segment points
    auto [p1, p2] = seg1;
    auto [p3, p4] = seg2;

    double x1 = p1.first, y1 = p1.second;
    double x2 = p2.first, y2 = p2.second;
    double x3 = p3.first, y3 = p3.second;
    double x4 = p4.first, y4 = p4.second;

    // Compute direction vectors and determinant
    double dx1 = x2 - x1, dy1 = y2 - y1;
    double dx2 = x4 - x3, dy2 = y4 - y3;
    double determinant = dx1 * dy2 - dx2 * dy1;

    // Check for parallel lines or identical segments
    if (std::abs(determinant) < 1e-10) {
        return {};
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
        return {round(x * 1e7) / 1e7, round(y * 1e7) / 1e7};
    }

    return {};
}