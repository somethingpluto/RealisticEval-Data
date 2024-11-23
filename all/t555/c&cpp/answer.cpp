#include <cmath>
#include <vector>
#include <stdexcept>

double quaternion_to_angle(const std::vector<double>& quaternion) {
    if (quaternion.size() != 4) {
        throw std::invalid_argument("Quaternion must have 4 components (w, x, y, z)");
    }

    double w = quaternion[0];
    double x = quaternion[1];
    double y = quaternion[2];
    double z = quaternion[3];

    // Calculate the angle in radians
    double angle = 2 * std::acos(w);

    return angle;
}