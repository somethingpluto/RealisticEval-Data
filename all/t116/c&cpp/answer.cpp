#include <cmath>
#include <vector>

std::vector<double> toroidalDiff(const std::pair<double, double>& thisPoint, const std::pair<double, double>& otherPoint, double width, double height) {
    double dx = thisPoint.first - otherPoint.first;
    double dy = thisPoint.second - otherPoint.second;

    // Handle wraparound for the x dimension
    if (std::abs(dx) > width / 2) {
        dx = dx > 0 ? dx - width : dx + width;
    }

    // Handle wraparound for the y dimension
    if (std::abs(dy) > height / 2) {
        dy = dy > 0 ? dy - height : dy + height;
    }

    return {dx, dy};
}