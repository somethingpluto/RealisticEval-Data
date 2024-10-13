import math  # Import the math library for the exp function

def gaussian_weight(intensity_diff: float, sigma_color: float) -> float:
    """
    Calculates the Gaussian weight based on the difference in intensity and a color standard deviation.

    The Gaussian weight is calculated using the formula:
    weight = exp(- (intensity_diff^2) / (2 * sigma_color^2))

    :param intensity_diff: The difference in intensity, which is used to compute the weight.
    :param sigma_color: The standard deviation for the color, affecting the spread of the weight.
    :return: The Gaussian weight as a float.
    """
    # Calculate the squared intensity difference
    squared_diff = intensity_diff ** 2
    # Calculate the denominator using sigma_color squared
    denominator = 2 * (sigma_color ** 2)
    # Calculate and return the Gaussian weight
    return math.exp(-squared_diff / denominator)