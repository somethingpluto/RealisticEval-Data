#include <cmath>
#include <tuple>

double calculateEuclideanDistance(const std::tuple<double, double>& point1, const std::tuple<double, double>& point2) {
    double x1 = std::get<0>(point1);
    double y1 = std::get<1>(point1);
    double x2 = std::get<0>(point2);
    double y2 = std::get<1>(point2);

    return std::sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));
}