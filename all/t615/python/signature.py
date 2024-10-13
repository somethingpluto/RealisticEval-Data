from typing import List


def calculate(values: List[int], period: int) -> float:
    """Calculates the average of the last 'period' integers in the given list of values.

    Args:
        values (List[int]): The list of integers from which to calculate the average.
        period (int): The number of last elements to include in the average calculation.

    Returns:
        float: The average of the last 'period' integers, or math.nan if the input list
                does not contain enough elements or if the period is invalid (<= 0).
    """