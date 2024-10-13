import math


def calculate_steering_angle(angular_velocity: float, speed: float, wheelbase: float) -> float:
    if speed <= 0:
        raise ValueError("Speed must be greater than zero.")

    # Calculate steering angle in radians
    steering_angle = math.atan((angular_velocity * wheelbase) / speed)

    return steering_angle  # Returns the steering angle in radians
