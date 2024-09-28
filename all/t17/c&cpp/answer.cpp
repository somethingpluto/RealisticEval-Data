#include <cmath>
#include <iostream>

const double R = 6371.0; // Radius of the Earth in kilometers

double radians(double degrees) {
    return degrees * M_PI / 180.0;
}

double haversine_distance(double lat1, double lon1, double lat2, double lon2) {
    // Convert latitude and longitude from degrees to radians
    double lat1_rad = radians(lat1);
    double lon1_rad = radians(lon1);
    double lat2_rad = radians(lat2);
    double lon2_rad = radians(lon2);

    // Differences in coordinates
    double dlat = lat2_rad - lat1_rad;
    double dlon = lon2_rad - lon1_rad;

    // Haversine formula
    double a = std::sin(dlat / 2) * std::sin(dlat / 2) + 
               std::cos(lat1_rad) * std::cos(lat2_rad) * 
               std::sin(dlon / 2) * std::sin(dlon / 2);
    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));

    // Distance in kilometers
    double distance = R * c;

    return distance;
}

int main() {
    double lat1 = 52.2296756;
    double lon1 = 21.0122287;
    double lat2 = 41.8919300;
    double lon2 = 12.5113300;

    std::cout << "Distance: " << haversine_distance(lat1, lon1, lat2, lon2) << " km" << std::endl;

    return 0;
}