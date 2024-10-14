from typing import List


def scale_to_range(input_array: List, input_min: float, input_max: float, output_min: float, output_max: float) -> List[
    float]:
    """
    Scales the values in an array from one range to another.
    Args:
        input_array (List): The array of input values to be scaled.
        input_min (float): The minimum value in the input range.
        input_max (float): The maximum value in the input range.
        output_min (float): The minimum value in the output range.
        output_max (float): The maximum value in the output range.

    Returns:
        List[float]: A new array with values scaled to the output range
    """
