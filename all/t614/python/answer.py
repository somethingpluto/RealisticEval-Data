from typing import List


def calculate_average_difference(numbers: List[int]) -> float:
    # Check if the list is valid (at least 2 numbers)
    if not numbers or len(numbers) < 2:
        return 0.0  # Not enough data to calculate differences

    # Calculate differences from the previous data
    differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]

    # Calculate the average of the differences
    return sum(differences) / len(differences)