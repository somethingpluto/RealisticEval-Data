import math  # Include math for the exp function


def spatial_weight(spatial_diff: float, sigma_space: float) -> float:
    """
    Calculates the spatial weight based on the difference in spatial coordinates and a space standard deviation.

    The spatial weight is calculated using the formula:
    weight = exp(- (spatial_diff^2) / (2 * sigma_space^2))

    :param spatial_diff: The difference in spatial coordinates, which is used to compute the weight.
    :param sigma_space: The standard deviation for spatial distance, affecting the spread of the weight.
    :return: The spatial weight as a float.
    :raises ValueError: If sigma_space is less than or equal to zero.
    """

    # Validate that sigma_space is greater than zero to avoid division by zero
    if sigma_space <= 0.0:
        raise ValueError("sigma_space must be greater than zero.")

    # Calculate the squared spatial difference
    squared_diff = spatial_diff ** 2

    # Calculate the denominator using sigma_space squared
    denominator = 2 * (sigma_space ** 2)

    # Calculate and return the spatial weight
    return math.exp(-squared_diff / denominator)