def extract_json(response: str) -> str:
    """
    Extracts the first complete JSON object from a given string.

    The function looks for the first occurrence of an opening curly brace '{'
    and searches for the corresponding closing curly brace '}'. It tracks
    the balance of braces to ensure that the JSON object is complete.

    If a complete JSON object is found, it returns the substring that
    represents that object. If no opening brace is found or if the braces
    are unbalanced (i.e., incomplete), it returns an empty string.

    Args:
        response: The input string from which to extract the JSON object.

    Returns:
        A string containing the first complete JSON object, or an
        empty string if no complete object is found.
    """
    start_index = response.find('{')
    if start_index == -1:
        return ""

    brace_count = 1
    end_index = start_index + 1

    while end_index < len(response):
        if response[end_index] == '{':
            brace_count += 1
        elif response[end_index] == '}':
            brace_count -= 1
            if brace_count == 0:
                return response[start_index:end_index + 1]
        end_index += 1

    return ""
import unittest


class TestExtractJson(unittest.TestCase):

    def test_extract_json_returns_empty_string_for_input_without_braces(self):
        input_str = "No braces here"
        self.assertEqual(extract_json(input_str), "")

    def test_extract_json_extracts_single_json_object(self):
        input_str = "Here is some text before { \"key\": \"value\" } and some text after."
        self.assertEqual(extract_json(input_str), "{ \"key\": \"value\" }")

    def test_extract_json_handles_nested_json_objects(self):
        input_str = "Some text { \"outer\": { \"inner\": \"value\" } } more text."
        self.assertEqual(extract_json(input_str), "{ \"outer\": { \"inner\": \"value\" } }")

    def test_extract_json_returns_empty_string_for_unmatched_braces(self):
        input_str = "Here is an incomplete JSON { \"key\": \"value\" "
        self.assertEqual(extract_json(input_str), "")

    def test_extract_json_returns_correct_json_when_multiple_braces_are_present(self):
        input_str = "Start { { \"key\": \"value\" } and some other text { \"another\": \"object\" }} end."
        self.assertEqual(extract_json(input_str),
                         "{ { \"key\": \"value\" } and some other text { \"another\": \"object\" }}")

    def test_extract_json_extracts_first_json_object_when_multiple_are_present(self):
        input_str = "Text before { \"first\": \"value1\" } text in between { \"second\": \"value2\" }"
        self.assertEqual(extract_json(input_str), "{ \"first\": \"value1\" }")
if __name__ == '__main__':
    unittest.main()