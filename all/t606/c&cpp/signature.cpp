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
double calculateSteeringAngle(double angularVelocity, double speed, double wheelbase) {}