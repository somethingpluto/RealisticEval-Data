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

/**
 * Calculate the intersection point of two line segments, if it exists.
 *
 * @param seg1 Coordinates of the first line segment, defined as ((x1, y1), (x2, y2)).
 * @param seg2 Coordinates of the second line segment, defined as ((x3, y3), (x4, y4)).
 * @return The (x, y) coordinates of the intersection point if the line segments intersect,
 *         otherwise an empty IntersectionResult indicating no intersection.
 */
IntersectionResult getLineSegmentIntersection(const std::pair<std::pair<double, double>, std::pair<double, double>>& seg1,
                                              const std::pair<std::pair<double, double>, std::pair<double, double>>& seg2) {}