from math import sqrt

def calculate_distance(agent1: str, agent2: str, observations: dict) -> float:
    """
    Calculates the Euclidean distance between two agents based on their coordinates in the observations.

    Args:
        agent1 (str): String representation of agent1's identifier.
        agent2 (str): String representation of agent2's identifier.
        observations (dict): Dictionary containing observation question with agent identifiers as keys.Each value is a dictionary with 'x' and 'y' keys representing coordinates.

    Returns:
        float: Euclidean distance between the two agents.
    """
    
    x1 = observations[agent1]['x']
    y1 = observations[agent1]['y']
    x2 = observations[agent2]['x']
    y2 = observations[agent2]['y']
    
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
import unittest

import numpy as np


class TestCalculateDistance(unittest.TestCase):

    def test_same_point(self):
        # Both agents are at the same point
        observations = {
            "agent1": {"x": 0, "y": 0},
            "agent2": {"x": 0, "y": 0}
        }
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), 0.0)

    def test_horizontal_distance(self):
        # Agents are horizontally apart
        observations = {
            "agent1": {"x": 0, "y": 0},
            "agent2": {"x": 3, "y": 0}
        }
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), 3.0)

    def test_vertical_distance(self):
        # Agents are vertically apart
        observations = {
            "agent1": {"x": 0, "y": 0},
            "agent2": {"x": 0, "y": 4}
        }
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), 4.0)

    def test_diagonal_distance(self):
        # Agents are diagonally apart
        observations = {
            "agent1": {"x": 1, "y": 2},
            "agent2": {"x": 4, "y": 6}
        }
        expected_distance = np.sqrt((4 - 1) ** 2 + (6 - 2) ** 2)
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), expected_distance)

    def test_negative_coordinates(self):
        # Agents have negative coordinates
        observations = {
            "agent1": {"x": -1, "y": -1},
            "agent2": {"x": -4, "y": -5}
        }
        expected_distance = np.sqrt((-4 + 1) ** 2 + (-5 + 1) ** 2)
        self.assertAlmostEqual(calculate_distance("agent1", "agent2", observations), expected_distance)
if __name__ == '__main__':
    unittest.main()