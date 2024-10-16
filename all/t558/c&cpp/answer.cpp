#include <iostream>
#include <cmath> // For M_PI and trigonometric functions

// Convert an angle from degrees to radians.
//
// Parameters:
//     degrees - The angle in degrees to convert.
//
// Returns:
//     The angle in radians.
double degrees_to_radians(double degrees) {
    double radians = degrees * (M_PI / 180.0);
    return radians;
}

// A simple check function to verify the correctness of the conversion.
void check_conversion() {
    double degrees = 180;
    double expected_radians = M_PI; // Expected result when converting 180 degrees to radians.
    double calculated_radians = degrees_to_radians(degrees);

    if (std::abs(calculated_radians - expected_radians) < 1e-6) {
        std::cout << "Conversion is correct." << std::endl;
    } else {
        std::cout << "Conversion is incorrect." << std::endl;
    }
}