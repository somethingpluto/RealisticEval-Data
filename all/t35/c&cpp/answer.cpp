#include <iostream>
#include <vector>
#include <utility>

bool is_point_in_polygon(const std::pair<double, double>& point, const std::vector<std::pair<double, double>>& polygon) {
    double x = point.first;
    double y = point.second;
    bool inside = false;
    size_t n = polygon.size();
    std::pair<double, double> p1 = polygon[0];

    for (size_t i = 0; i < n + 1; ++i) {
        std::pair<double, double> p2 = polygon[i % n];
        if (y > std::min(p1.second, p2.second)) {
            if (y <= std::max(p1.second, p2.second)) {
                if (x <= std::max(p1.first, p2.first)) {
                    if (p1.second != p2.second) {
                        double xinters = (y - p1.second) * (p2.first - p1.first) / (p2.second - p1.second) + p1.first;
                        if (p1.first == p2.first || x <= xinters) {
                            inside = !inside;
                        }
                    } else if (p1.first == p2.first && x <= p1.first) {
                        inside = !inside;
                    }
                }
            }
        }
        p1 = p2;
    }

    return inside;
}