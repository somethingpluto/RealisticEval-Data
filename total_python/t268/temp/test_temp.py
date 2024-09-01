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

from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    total_gas = total_cost = tank = start_index = 0

    for i in range(n):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:  # If tank becomes negative, update start_index and reset tank
            start_index = i + 1
            tank = 0

    return start_index if total_gas >= total_cost else -1
