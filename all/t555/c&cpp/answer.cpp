#include <cmath>
#include <vector>
#include <stdexcept>

/**
 * Converts a quaternion to a rotation angle in radians.
 *
 * @param quaternion A vector containing the quaternion components (w, x, y, z)
 * @return The rotation angle in radians
 */
double quaternion_to_angle(const std::vector<double>& quaternion) {
    // Ensure the quaternion is a valid 4-element vector
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

// Example usage
int main() {
    try {
        std::vector<double> quaternion = {0.7071068, 0.0, 0.0, 0.7071068};
        double angle = quaternion_to_angle(quaternion);
        std::cout << "Rotation angle: " << angle << " radians" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}