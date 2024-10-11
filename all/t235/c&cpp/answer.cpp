#include <cmath>
#include <iostream>

double calculateBearing(double lat1, double lon1, double lat2, double lon2) {
    const double pi = 3.14159265358979323846;

    // Convert latitude and longitude from degrees to radians
    lat1 = lat1 * pi / 180.0;
    lon1 = lon1 * pi / 180.0;
    lat2 = lat2 * pi / 180.0;
    lon2 = lon2 * pi / 180.0;

    // Calculate the differences
    double dLon = lon2 - lon1;
    double y = sin(dLon) * cos(lat2);
    double x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dLon);

    // Calculate the initial bearing
    double initialBearing = atan2(y, x);

    // Normalize the bearing to be within the range [0, 2*pi)
    if (initialBearing < 0) {
        initialBearing += 2 * pi;
    }

    // Convert the bearing from radians to degrees
    return initialBearing * 180.0 / pi;
}