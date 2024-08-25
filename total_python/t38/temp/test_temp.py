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

    def test_no_intermediates(self):
        # Test with zero intermediates
        result = rainbowHexGenerator(0)
        expected = self.rainbow_colors
        self.assertEqual(result, expected, "Should return main rainbow colors without intermediates")

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


def rainbowHexGenerator(num_intermediates, include_endpoints=False):
    # List of main rainbow colors
    rainbow_colors = [
        "#FF0000",  # Red
        "#FF7F00",  # Orange
        "#FFFF00",  # Yellow
        "#00FF00",  # Green
        "#0000FF",  # Blue
        "#4B0082",  # Indigo
        "#8A2BE2"  # Violet
    ]

    # Generate intermediate colors between two hex colors
    def interpolate_colors(color1, color2, steps):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        return [
            "#{:02X}{:02X}{:02X}".format(
                int(r1 + (i * (r2 - r1) / steps)),
                int(g1 + (i * (g2 - g1) / steps)),
                int(b1 + (i * (b2 - b1) / steps))
            ) for i in range(1, steps)
        ]

    # Calculate the full spectrum of colors
    full_spectrum = []
    num_main_colors = len(rainbow_colors)
    for i in range(num_main_colors - 1 + include_endpoints):
        # Wrap around for the endpoint inclusion
        next_index = (i + 1) % num_main_colors
        current_color = rainbow_colors[i]
        next_color = rainbow_colors[next_index]
        full_spectrum.append(current_color)
        full_spectrum.extend(interpolate_colors(current_color, next_color, num_intermediates + 1))

    # Append the last color only if endpoints are not included
    if not include_endpoints:
        full_spectrum.append(rainbow_colors[-1])

    return full_spectrum