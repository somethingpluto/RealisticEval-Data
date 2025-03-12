
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
    # Check if all elements in gas and cost are non-negative
    if all(x < 0 for x in gas) or all(x < 0 for x in cost):
        return -1

    # Create a set to store the indices of the starting gas station
    start_gas_indices = set()

    # Loop through gas and cost
    for gas_index, gas in enumerate(gas):
        for cost_index, cost_value in enumerate(cost):
            # Check if the current gas station is the starting gas station
            if gas_index in start_gas_indices and cost_index == gas_index + 1:
                # If it is, return the index
                return gas_index
            # If not, add the current gas station to the set of starting gas stations
            start_gas_indices.add(gas_index)

    return -1

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