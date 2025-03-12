import json

def extract_json(response: str) -> str:
    """
    Extracts the first complete JSON object from a given string.
    """
    json_objects = []
    current_index = 0
    while current_index < len(response):
        open_brace_index = response.find('{', current_index)
        if open_brace_index == -1:
            break

        close_brace_index = response.find('}', open_brace_index)
        if close_brace_index == -1:
            break

        json_sub_string = response[open_brace_index:close_brace_index + 1]
        try:
            json.loads(json_sub_string)
            json_objects.append(json_sub_string)
            current_index = close_brace_index + 1
        except json.JSONDecodeError:
            current_index += 1

    if json_objects:
        return json_objects[0]
    else:
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