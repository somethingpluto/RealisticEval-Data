import unittest

class TestRemoveTripleBackticks(unittest.TestCase):

    def test_remove_triple_backticks_basic(self):
        # Test basic functionality
        input_strings = ['Here is ```code``` example', 'Another ```example``` here', 'No backticks here']
        expected_output = ['Here is code example', 'Another example here', 'No backticks here']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_strings_with_multiple_instances(self):
        # Test strings containing multiple instances of triple backticks
        input_strings = ['Multiple ```backticks``` in ```one``` string']
        expected_output = ['Multiple backticks in one string']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_empty_strings(self):
        # Test with empty strings
        input_strings = ['']
        expected_output = ['']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_no_triple_backticks(self):
        # Test strings that do not contain triple backticks
        input_strings = ['Just a normal string', 'Another normal string']
        expected_output = ['Just a normal string', 'Another normal string']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)

    def test_edge_cases(self):
        # Test edge cases like strings made entirely of triple backticks
        input_strings = ['```', '```more```', 'text``````']
        expected_output = ['', 'more', 'text']
        self.assertEqual(remove_triple_backticks(input_strings), expected_output)
def remove_triple_backticks(string_list):
    """
    Processes a list of strings, removing all occurrences of three consecutive backticks from each string.

    Args:
    string_list (list of str): The list of strings to process.

    Returns:
    list of str: A new list with all instances of three consecutive backticks removed from each string.
    """
    # Use list comprehension to process each string in the list by removing three consecutive backticks
    processed_list = [s.replace('```', '') for s in string_list]
    return processed_list