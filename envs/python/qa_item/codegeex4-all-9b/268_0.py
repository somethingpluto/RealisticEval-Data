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
    total_tank, curr_tank = 0, 0
    starting_station = 0
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        # If one couldn't get here
        if curr_tank < 0:
            # Pick up the next station as the starting one.
            starting_station = i + 1
            # Start with an empty tank.
            curr_tank = 0
    return starting_station if total_tank >= 0 else -1
import unittest


class TestCanCompleteCircuit(unittest.TestCase):

    def test_possible_single_station(self):
        gas = [5]
        cost = [4]
        expected = 0
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_impossible_single_station(self):
        gas = [4]
        cost = [5]
        expected = -1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_two_stations_possible(self):
        gas = [1, 2]
        cost = [2, 1]
        expected = 1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_circular_route_possible(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_circular_route_impossible(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

if __name__ == '__main__':
    unittest.main()