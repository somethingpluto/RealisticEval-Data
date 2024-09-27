import unittest
from unittest.mock import patch, mock_open


class TestCountContainedRanges(unittest.TestCase):

    def test_cases(self):
        test_data = {
            "case1": ("1-5\n2-3\n4-6\n", 2),  # 1-5 contains 2-3 and 4-6 is outside
            "case2": ("1-10\n2-5\n3-4\n8-9\n", 4),  # 1-10 contains 2-5, 3-4, and 8-9
            "case3": ("5-10\n1-4\n11-15\n", 0),  # No ranges contain each other
            "case4": ("1-5\n1-5\n2-3\n", 3),  # 1-5 contains 2-3, and each 1-5 contains the other
            "case5": ("1-3\n2-4\n3-5\n", 2)  # 2-4 contains 1-3, and 3-5 contains 3-5
        }

        for case, (mock_data, expected_count) in test_data.items():
            with self.subTest(case=case):
                with patch("builtins.open", mock_open(read_data=mock_data)):
                    result = count_contained_ranges("dummy_path.txt")
                    self.assertEqual(result, expected_count)