#include <cmath>
#include <iostream>

double haversine_distance(double lat1, double lon1, double lat2, double lon2) {
    const double R = 6371.0;
    double lat1_rad = lat1 * M_PI / 180.0;
    double lon1_rad = lon1 * M_PI / 180.0;
    double lat2_rad = lat2 * M_PI / 180.0;
    double lon2_rad = lon2 * M_PI / 180.0;
    double dlat = lat2_rad - lat1_rad;
    double dlon = lon2_rad - lon1_rad;
    double a = std::sin(dlat / 2) * std::sin(dlat / 2) +
               std::cos(lat1_rad) * std::cos(lat2_rad) * std::sin(dlon / 2) * std::sin(dlon / 2);
    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));

    double distance = R * c;

    return distance;
}