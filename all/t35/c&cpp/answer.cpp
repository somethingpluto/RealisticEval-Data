#include <vector>
#include <tuple>

bool is_point_in_polygon(std::tuple<double, double> point, const std::vector<std::tuple<double, double>>& polygon) {
    double x = std::get<0>(point);
    double y = std::get<1>(point);
    bool inside = false;
    int n = polygon.size();
    double p1x = std::get<0>(polygon[0]);
    double p1y = std::get<1>(polygon[0]);

    for (int i = 0; i <= n; i++) {
        double p2x = std::get<0>(polygon[i % n]);
        double p2y = std::get<1>(polygon[i % n]);
        if (y > std::min(p1y, p2y)) {
            if (y <= std::max(p1y, p2y)) {
                if (x <= std::max(p1x, p2x)) {
                    if (p1y != p2y) {
                        double xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x;
                        if (p1x == p2x || x <= xinters) {
                            inside = !inside;
                        }
                    }
                }
            }
        }
        p1x = p2x;
        p1y = p2y;
    }

    return inside;
}