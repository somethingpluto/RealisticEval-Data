#include <vector>

struct Coordinates {
    double x;
    double y;
};

/**
 * Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.
 *
 * @param t - A value between 0 and 1 representing the interpolation parameter.
 * @param points - A vector of control points defining the Bézier curve.
 * @returns The calculated Coordinates at the given parameter t.
 */
Coordinates getBezierPoint(double t, const std::vector<Coordinates>& points) {
    // If there's only one point, return it as the result
    if (points.size() == 1) {
        return points[0];
    }

    // Create a vector to hold the points for the next iteration
    std::vector<Coordinates> nextPoints;

    // Calculate the intermediate points for the next iteration
    for (size_t i = 0; i < points.size() - 1; i++) {
        double x = (1 - t) * points[i].x + t * points[i + 1].x;
        double y = (1 - t) * points[i].y + t * points[i + 1].y;
        nextPoints.push_back({x, y});
    }

    // Recursively call getBezierPoint with the new points
    return getBezierPoint(t, nextPoints);
}