#include <iostream>
#include <cmath>
#include <stdexcept>

double calculateSteeringAngle(double angularVelocity, double speed, double wheelbase) {
    // Check for valid speed
    if (speed <= 0) {
        throw std::invalid_argument("Speed must be greater than zero.");
    }

    // Calculate steering angle in radians
    double steeringAngle = atan((angularVelocity * wheelbase) / speed);

    return steeringAngle; // Returns the steering angle in radians
}