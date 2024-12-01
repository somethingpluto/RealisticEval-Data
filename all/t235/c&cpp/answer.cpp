#include <cmath>
#include <iostream>

// Function to calculate the bearing from one latitude and longitude to another
double calculate_bearing(double lat1, double lon1, double lat2, double lon2) {
    /**
     * Calculate the bearing from one latitude and longitude to another.
     *
     * Args:
     * lat1 (double): Latitude of the starting point in decimal degrees.
     * lon1 (double): Longitude of the starting point in decimal degrees.
     * lat2 (double): Latitude of the ending point in decimal degrees.
     * lon2 (double): Longitude of the ending point in decimal degrees.
     *
     * Returns:
     * double: Bearing in degrees from the starting point to the ending point, ranging from 0 to 360.
     */
    
    // Convert latitude and longitude from degrees to radians
    double lat1_rad = lat1 * M_PI / 180.0;
    double lon1_rad = lon1 * M_PI / 180.0;
    double lat2_rad = lat2 * M_PI / 180.0;
    double lon2_rad = lon2 * M_PI / 180.0;

    // Difference in longitude
    double delta_lon_rad = lon2_rad - lon1_rad;

    // Calculate the bearing components
    double x = std::sin(delta_lon_rad) * std::cos(lat2_rad);
    double y = std::cos(lat1_rad) * std::sin(lat2_rad) - (std::sin(lat1_rad) * std::cos(lat2_rad) * std::cos(delta_lon_rad));

    // Calculate the initial bearing in radians
    double initial_bearing_rad = std::atan2(x, y);

    // Convert the initial bearing from radians to degrees
    double initial_bearing_deg = initial_bearing_rad * 180.0 / M_PI;

    // Normalize the bearing to 0-360 degrees
    double compass_bearing = fmod((initial_bearing_deg + 360.0), 360.0);

    return compass_bearing;
}