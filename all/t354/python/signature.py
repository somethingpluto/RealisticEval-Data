def gaussian_weight(intensity_diff: float, sigma_color: float) -> float:
    """
    Calculate the Gaussian weight based on the difference in intensity and a color standard deviation.

    The Gaussian weight is calculated using the formula:
    weight = exp(- (intensity_diff^2) / (2 * sigma_color^2))

    Args:
        intensity_diff (float): The difference in intensity, which is used to compute the weight.
        sigma_color (float): The standard deviation for the color, affecting the spread of the weight.

    Returns:
        float: The Gaussian weight.
    """
