import sys
import unittest
from io import StringIO


class TestPrintFixedWidthTable(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_basic_table(self):
        data = {
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 30, 35],
            "City": ["New York", "Los Angeles", "Chicago"]
        }
        print_fixed_width_table(data)
        expected_output = "Name    Age City       \nAlice   25  New York   \nBob     30  Los Angeles \nCharlie 35  Chicago     \n"
        self.assertEqual(self.held_output.getvalue(), expected_output)

    def test_empty_table(self):
        data = {}
        print_fixed_width_table(data)
        expected_output = "\n"  # Just a newline for an empty table
        self.assertEqual(self.held_output.getvalue(), expected_output)

    def test_single_row(self):
        data = {
            "Product": ["Widget"],
            "Price": [19.99],
            "Quantity": [5]
        }
        print_fixed_width_table(data)
        expected_output = "Product Price Quantity\nWidget  19.99 5       \n"
        self.assertEqual(self.held_output.getvalue(), expected_output)

    def test_variable_length_columns(self):
        data = {
            "Country": ["USA", "Canada", "Mexico"],
            "Capital": ["Washington, D.C.", "Ottawa", "Mexico City"],
            "Population": [331002651, 37742154, 128932753]
        }
        print_fixed_width_table(data)
        expected_output = "Country Capital            Population\nUSA     Washington, D.C.  331002651\nCanada  Ottawa            37742154\nMexico  Mexico City      128932753\n"
        self.assertEqual(self.held_output.getvalue(), expected_output)

    def test_numeric_values(self):
        data = {
            "Year": [2020, 2021, 2022],
            "Revenue": [1000000, 1200000, 1300000],
            "Expenses": [800000, 900000, 950000]
        }
        print_fixed_width_table(data)
        expected_output = "Year Revenue  Expenses\n2020 1000000 800000 \n2021 1200000 900000 \n2022 1300000 950000 \n"
        self.assertEqual(self.held_output.getvalue(), expected_output)