#include <cmath>
#include <iostream>

// Function to calculate the Haversine distance between two points on the Earth
double haversine_distance(double lat1, double lon1, double lat2, double lon2) {
    // Radius of the Earth in kilometers
    const double R = 6371.0;

    // Convert latitude and longitude from degrees to radians
    double lat1_rad = lat1 * M_PI / 180.0;
    double lon1_rad = lon1 * M_PI / 180.0;
    double lat2_rad = lat2 * M_PI / 180.0;
    double lon2_rad = lon2 * M_PI / 180.0;

    // Differences in coordinates
    double dlat = lat2_rad - lat1_rad;
    double dlon = lon2_rad - lon1_rad;

    // Haversine formula
    double a = std::sin(dlat / 2) * std::sin(dlat / 2) +
               std::cos(lat1_rad) * std::cos(lat2_rad) * std::sin(dlon / 2) * std::sin(dlon / 2);
    double c = 2 * std::atan2(std::sqrt(a), std::sqrt(1 - a));

    // Distance in kilometers
    double distance = R * c;

    return distance;
}

int main() {
    // Example usage
    double lat1 = 50.06638889; // Latitude of point A
    double lon1 = -5.71472222; // Longitude of point A
    double lat2 = 58.64388889; // Latitude of point B
    double lon2 = -3.07000000; // Longitude of point B

    double distance = haversine_distance(lat1, lon1, lat2, lon2);
    std::cout << "Distance between the two points: " << distance << " kilometers" << std::endl;

    return 0;
}