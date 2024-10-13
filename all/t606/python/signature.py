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
