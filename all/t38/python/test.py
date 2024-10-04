import unittest


class TestRainbowHexGenerator(unittest.TestCase):
    def setUp(self):
        self.rainbow_colors = [
            "#FF0000",  # Red
            "#FF7F00",  # Orange
            "#FFFF00",  # Yellow
            "#00FF00",  # Green
            "#0000FF",  # Blue
            "#4B0082",  # Indigo
            "#8A2BE2"  # Violet
        ]

    def test_one_intermediate(self):
        # Test with one intermediate color between each main color
        result = rainbowHexGenerator(1)
        # Check if the length is correct (7 main + 6 intermediates)
        self.assertEqual(len(result), 13, "Should have 13 colors with one intermediate")

    def test_include_endpoints(self):
        # Test including the endpoint (wrap-around) interpolation
        result = rainbowHexGenerator(1, include_endpoints=True)
        # Check if the length is correct (7 main + 7 intermediates including wrap-around)
        self.assertEqual(len(result), 14, "Should have 14 colors with wrap-around interpolation")

    def test_high_number_of_intermediates(self):
        # Test with a high number of intermediates to check gradient smoothness
        result = rainbowHexGenerator(10)
        # Check if the length is correct (7 main + 60 intermediates)
        self.assertEqual(len(result), 67, "Should have 67 colors with 10 intermediates each")

