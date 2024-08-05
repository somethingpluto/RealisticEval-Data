import unittest

from total.t12.adapted import calculate_distance, analyze_spatial_distribution


class TestSpatialAnalysis(unittest.TestCase):
    def setUp(self):
        self.positions = {
            'agent1': {'x': 0, 'y': 0},
            'agent2': {'x': 3, 'y': 4},
            'agent3': {'x': 1, 'y': 1}
        }
        self.environment = type('env', (object,), {"agents": ['agent1', 'agent2', 'agent3']})

    def test_distance_calculation(self):
        self.assertEqual(calculate_distance('agent1', 'agent2', self.positions), 5)

    def test_spatial_distribution(self):
        result = analyze_spatial_distribution('agent1', self.positions, self.environment, 10, 4)
        self.assertEqual(result.tolist(), [1, 0, 1, 0])  # Assumes partition angles and positions of agents
