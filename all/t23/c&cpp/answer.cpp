#include <tuple>
#include <optional>
#include <cmath>

// Type alias for optional tuple to handle the intersection or no intersection
using Intersection = std::optional<std::tuple<float, float>>;

Intersection check_segments_intersection(const std::pair<std::tuple<float, float>, std::tuple<float, float>>& seg1,
                                          const std::pair<std::tuple<float, float>, std::tuple<float, float>>& seg2) {
    // Unpack segment points
    auto [x1, y1] = seg1.first;
    auto [x2, y2] = seg1.second;
    auto [x3, y3] = seg2.first;
    auto [x4, y4] = seg2.second;

    // Compute direction vectors and determinant
    float dx1 = x2 - x1, dy1 = y2 - y1;
    float dx2 = x4 - x3, dy2 = y4 - y3;
    float determinant = dx1 * dy2 - dx2 * dy1;

    // Check for parallel lines or identical segments
    if (std::abs(determinant) < 1e-10f) {
        return std::nullopt;
    }

    // Calculate intersection parameters
    float t1 = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / determinant;
    float t2 = ((x3 - x1) * dy1 - (y3 - y1) * dx1) / determinant;

    // Allow for a small tolerance in the intersection check
    float tolerance = 1e-10f;

    // Check if intersection is within the bounds of the line segments
    if (0.0f - tolerance <= t1 && t1 <= 1.0f + tolerance && 0.0f - tolerance <= t2 && t2 <= 1.0f + tolerance) {
        float x = x1 + t1 * dx1;
        float y = y1 + t1 * dy1;
        return std::make_tuple(round(x * 1e7) / 1e7f, round(y * 1e7) / 1e7f);  // Round to 7 decimal places
    }

    return std::nullopt;
}