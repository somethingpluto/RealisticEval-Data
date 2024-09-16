from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    """
    Determines if there exists a starting gas station's index where you can travel
    around the circuit once in a clockwise direction.

    Args:
        gas (List[int]): List of integers representing the amount of gas at each station.
        cost (List[int]): List of integers representing the cost of gas to travel from each station to the next.

    Returns:
        int: The starting gas station's index if the circuit can be completed, otherwise -1.
    """