from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    total_gas = 0
    total_cost = 0
    start = 0
    max_total_gas = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        total_cost += cost[i]

        if total_gas < 0:
            total_gas = 0
            start = (i + 1) % len(gas)

        max_total_gas = max(max_total_gas, total_gas)

    return -1 if max_total_gas < total_cost else start
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