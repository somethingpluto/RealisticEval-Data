import unittest
from io import StringIO
import sys
from typing import Any


def print_fixed_width_table(table: dict[str, list[Any]]) -> None:
    keys = list(table.keys())
    values = list(table.values())
    values = list(zip(*values))

    widths = []
    for i in range(len(keys)):
        widths.append(max(len(str(x[i])) for x in values + [keys]))

    print(" ".join("{:{}}".format(x, w) for x, w in zip(keys, widths)))

    for row in values:
        print(" ".join("{:{}}".format(x, w) for x, w in zip(row, widths)))


class TestPrintFixedWidthTable(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_basic_table(self):
        table = {
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [24, 30, 22],
            "City": ["New York", "Los Angeles", "Chicago"]
        }
        print_fixed_width_table(table)
        output = self.held_output.getvalue().strip()
        expected_output = (
            "Name     Age City       \n"
            "Alice    24  New York   \n"
            "Bob      30  Los Angeles \n"
            "Charlie  22  Chicago    "
        )
        self.assertEqual(output, expected_output)

    def test_varying_lengths(self):
        table = {
            "Product": ["Apples", "Oranges", "Bananas", "Strawberries"],
            "Price": [1.5, 2.0, 0.75, 3.5]
        }
        print_fixed_width_table(table)
        output = self.held_output.getvalue().strip()
        expected_output = (
            "Product      Price \n"
            "Apples       1.5   \n"
            "Oranges      2.0   \n"
            "Bananas      0.75  \n"
            "Strawberries 3.5   "
        )
        self.assertEqual(output, expected_output)

    def test_empty_table(self):
        table = {}
        print_fixed_width_table(table)
        output = self.held_output.getvalue().strip()
        expected_output = ""  # Should be empty since there's no data
        self.assertEqual(output, expected_output)

    def test_single_row(self):
        table = {
            "Name": ["Eve"],
            "Age": [28],
            "City": ["Seattle"]
        }
        print_fixed_width_table(table)
        output = self.held_output.getvalue().strip()
        expected_output = (
            "Name Age City  \n"
            "Eve  28  Seattle"
        )
        self.assertEqual(output, expected_output)

    def test_special_characters(self):
        table = {
            "Item": ["Café", "Müller", "Résumé"],
            "Count": [5, 10, 3]
        }
        print_fixed_width_table(table)
        output = self.held_output.getvalue().strip()
        expected_output = (
            "Item    Count\n"
            "Café    5    \n"
            "Müller  10   \n"
            "Résumé  3    "
        )
        self.assertEqual(output, expected_output)
