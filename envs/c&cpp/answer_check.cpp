#define CATCH_CONFIG_MAIN
#include "./lib/catch.hpp"
#include <iostream>
#include <cmath>
#include <stdexcept>

/**
 * @brief Calculates the steering angle based on the given angular velocity, speed, and wheelbase.
 *
 * The function uses the relationship between angular velocity, speed, and the steering angle
 * to determine the appropriate steering angle required for the vehicle to achieve the desired
 * angular velocity. The formula used is:
 *
 *      ω = (v / L) * tan(δ)
 *
 * Rearranging gives us:
 *
 *      δ = atan((ω * L) / v)
 *
 * @param angularVelocity The angular velocity of the vehicle in radians per second.
 * @param speed The forward speed of the vehicle in meters per second.
 * @param wheelbase The distance between the front and rear axles of the vehicle in meters.
 *
 * @return The steering angle in radians.
 *
 * @throws std::invalid_argument if speed is less than or equal to zero,
 *                                since the vehicle cannot move at zero or negative speed.
 */
double calculateSteeringAngle(double angularVelocity, double speed, double wheelbase) {
    if (speed <= 0) {
        throw std::invalid_argument("Speed must be greater than zero.");
    }

    double steeringAngle = std::atan((angularVelocity * wheelbase) / speed);
    return steeringAngle;
}TEST_CASE("Calculate Steering Angle Tests") {
    const double wheelbase = 2.5; // Setting wheelbase constant for all tests

    SECTION("Normal case") {
        double angularVelocity = 1.0; // radians/second
        double speed = 10.0;          // meters/second
        double expectedAngle = atan((angularVelocity * wheelbase) / speed);
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }

    SECTION("Zero speed") {
        double angularVelocity = 1.0; // radians/second
        double speed = 0.0;           // meters/second
        REQUIRE_THROWS_AS(calculateSteeringAngle(angularVelocity, speed, wheelbase), std::invalid_argument);
    }

    SECTION("Negative speed") {
        double angularVelocity = 1.0; // radians/second
        double speed = -5.0;          // meters/second
        REQUIRE_THROWS_AS(calculateSteeringAngle(angularVelocity, speed, wheelbase), std::invalid_argument);
    }

    SECTION("Zero angular velocity") {
        double angularVelocity = 0.0; // radians/second
        double speed = 10.0;          // meters/second
        double expectedAngle = 0.0;   // Steering angle should be zero
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }

    SECTION("Large values") {
        double angularVelocity = 100.0; // radians/second
        double speed = 1000.0;          // meters/second
        double expectedAngle = atan((angularVelocity * wheelbase) / speed);
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }

    SECTION("High angular velocity") {
        double angularVelocity = 10.0; // radians/second
        double speed = 1.0;             // meters/second
        double expectedAngle = atan((angularVelocity * wheelbase) / speed);
        REQUIRE(calculateSteeringAngle(angularVelocity, speed, wheelbase) == Approx(expectedAngle));
    }
}