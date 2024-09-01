import unittest

class TestProcessCol(unittest.TestCase):
    def test_basic_split(self):
        input_data = ["John, Smith, 1990, (MD), PhD"]
        expected_output = [["John", "Smith", "1990", "(MD) PhD"]]
        result = processCol(input_data)
        self.assertEqual(result, expected_output)

    def test_nested_parentheses(self):
        input_data = ["Data (Analysis, Development (Python, Java)), 2020"]
        expected_output = [["Data (Analysis, Development (Python, Java))", "2020"]]
        result = processCol(input_data)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        input_data = []
        expected_output = []
        result = processCol(input_data)
        self.assertEqual(result, expected_output)

    def test_non_string_input(self):
        input_data = [123, "Tech, (2021), Innovation"]
        expected_output = [[], ["Tech", "(2021)", "Innovation"]]
        result = processCol(input_data)
        self.assertEqual(result, expected_output)

    def test_complex_case(self):
        input_data = ["Alice (BSc), 2005, Masters (Economics), 2010", "Bob, 2019, PhD (CS)"]
        expected_output = [["Alice (BSc)", "2005", "Masters (Economics)", "2010"], ["Bob", "2019", "PhD (CS)"]]
        result = processCol(input_data)
        self.assertEqual(result, expected_output)
import re

def processCol(col):
    # Process each element in the column 'col'
    col = [
        # Split the string based on commas that are not within parentheses
        re.split(r',(?!(?:[^()]*\([^()]*\))*[^()]*\))', x) if isinstance(x, str) else []
        for x in col
    ]

    # Iterate over each sublist in the column
    for x in col:
        # Process elements from the end to the beginning
        for i in range(len(x) - 1, 1, -1):
            # Check conditions to merge items
            if "(" in x[i] and "(" not in x[i-1] and not x[i].startswith("("):
                # Merge the current element with the previous one
                x[i-1] = f"{x[i-1]} ({x[i].split(' (', 1)[1]}"

        # Process elements from the beginning towards the end
        for i in range(1, len(x) - 1):
            # Search for patterns with parentheses and initials
            if re.search(r"\([a-zA-Z]+\.", x[i]):
                print(x[i])
                print(x[i-1])
                # Find patterns in the previous item
                search = list(re.finditer(r"([a-zA-Zß.][a-zA-Zß. ]+,\s)?\d{4},\s", x[i-1]))
                if search:
                    # Output the last found pattern
                    print(search[-1].group())
                    # Replace in the current item using the last found pattern
                    x[i] = re.sub(r"\(([a-zA-Z]+\.)", fr"({search[-1].group()}\1", x[i])
                    print(x[i])

    return col