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
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        
        if tank < 0:
            start = i + 1
            tank = 0
    
    if total_gas < total_cost:
        return -1
    else:
        return start
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