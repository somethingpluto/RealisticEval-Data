import math

def calculate_steering_angle(angular_velocity: float, speed: float, wheelbase: float) -> float:
    """
    Calculates the steering angle based on the given angular velocity, speed, and wheelbase.

    The function uses the relationship between angular velocity, speed, and the steering angle
    to determine the appropriate steering angle required for the vehicle to achieve the desired
    angular velocity. The formula used is:

         ω = (v / L) * tan(δ)

    Rearranging gives us:

         δ = atan((ω * L) / v)

    Parameters:
    angular_velocity (float): The angular velocity of the vehicle in radians per second.
    speed (float): The forward speed of the vehicle in meters per second.
    wheelbase (float): The distance between the front and rear axles of the vehicle in meters.

    Returns:
    float: The steering angle in radians.

    Raises:
    ValueError: If speed is less than or equal to zero,
                since the vehicle cannot move at zero or negative speed.
    """
    if speed <= 0:
        raise ValueError("Speed must be greater than zero")

    steering_angle = math.atan((angular_velocity * wheelbase) / speed)
    return steering_angle
import math
import unittest


class Tester(unittest.TestCase):
    wheelbase = 2.5  # Setting wheelbase constant for all tests

    def test_normal_case(self):
        angular_velocity = 1.0  # radians/second
        speed = 10.0  # meters/second
        expected_angle = math.atan((angular_velocity * self.wheelbase) / speed)
        self.assertAlmostEqual(calculate_steering_angle(angular_velocity, speed, self.wheelbase), expected_angle)

    def test_zero_speed(self):
        angular_velocity = 1.0  # radians/second
        speed = 0.0  # meters/second
        with self.assertRaises(ValueError):
            calculate_steering_angle(angular_velocity, speed, self.wheelbase)

    def test_negative_speed(self):
        angular_velocity = 1.0  # radians/second
        speed = -5.0  # meters/second
        with self.assertRaises(Exception):
            calculate_steering_angle(angular_velocity, speed, self.wheelbase)

    def test_zero_angular_velocity(self):
        angular_velocity = 0.0  # radians/second
        speed = 10.0  # meters/second
        expected_angle = 0.0  # Steering angle should be zero
        self.assertAlmostEqual(calculate_steering_angle(angular_velocity, speed, self.wheelbase), expected_angle)

    def test_large_values(self):
        angular_velocity = 100.0  # radians/second
        speed = 1000.0  # meters/second
        expected_angle = math.atan((angular_velocity * self.wheelbase) / speed)
        self.assertAlmostEqual(calculate_steering_angle(angular_velocity, speed, self.wheelbase), expected_angle)

    def test_high_angular_velocity(self):
        angular_velocity = 10.0  # radians/second
        speed = 1.0  # meters/second
        expected_angle = math.atan((angular_velocity * self.wheelbase) / speed)
        self.assertAlmostEqual(calculate_steering_angle(angular_velocity, speed, self.wheelbase), expected_angle)

if __name__ == '__main__':
    unittest.main()