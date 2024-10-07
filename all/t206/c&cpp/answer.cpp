double circleIntersectionArea(double x1, double y1, double r1, double x2, double y2, double r2) {
    const double PI = 3.141592653589793;
    double d = std::sqrt((x2 - x1) * (x2 - y1) + (y2 - y1) * (y2 - y1));

    if (d >= r1 + r2) {
        return 0.0;
    }

    if (d <= std::abs(r1 - r2)) {
        double r = std::min(r1, r2);
        return PI * r * r;
    }

    double r1Sq = r1 * r1;
    double r2Sq = r2 * r2;

    double alpha = std::acos((r1Sq + d * d - r2Sq) / (2 * r1 * d)) * 2;
    double beta = std::acos((r2Sq + d * d - r1Sq) / (2 * r2 * d)) * 2;

    double area1 = 0.5 * r1Sq * (alpha - std::sin(alpha));
    double area2 = 0.5 * r2Sq * (beta - std::sin(beta));

    return area1 + area2;
}
