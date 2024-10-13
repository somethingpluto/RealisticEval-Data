from typing import List


def calculate(values: List[int], period: int) -> float:
    # Check if the number of values is less than the specified period
    if values is None or len(values) < period or period <= 0:
        return float('nan')  # Return NaN for invalid input

    sum_values = 0.0  # Initialize the sum

    # Calculate the sum of the last 'period' values
    for i in range(len(values) - period, len(values)):
        sum_values += values[i]

    # Return the average of the last 'period' values
    return sum_values / period
