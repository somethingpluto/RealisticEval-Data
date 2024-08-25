import unittest


class TestHandleNestedData(unittest.TestCase):
    def test_simple_dictionary(self):
        data = {"name": b"Alice", "age": "30"}
        expected = {"name": "Alice", "age": 30}
        self.assertEqual(handle_nested_data(data), expected)

    def test_nested_dictionary(self):
        data = {"user": {"name": b"Bob", "details": {"age": "25", "height": "175.5"}}}
        expected = {"user": {"name": "Bob", "details": {"age": 25, "height": 175.5}}}
        self.assertEqual(handle_nested_data(data), expected)

    def test_list_of_mixed_data_types(self):
        data = ["100", b"200", 300.0, "400.5"]
        expected = [100, "200", 300.0, 400.5]
        self.assertEqual(handle_nested_data(data), expected)

    def test_incorrect_byte_decoding(self):
        data = {"invalid_bytes": b"\xff\xfe\xfd\xfc"}
        with self.assertRaises(UnicodeDecodeError):
            handle_nested_data(data)

    def test_complex_nested_structure(self):
        data = {
            "team": [
                {"name": b"Charlie", "scores": ["1000", "2000.2"]},
                {"name": b"Daisy", "skills": [b"Coding", "Design"], "age": "22"}
            ]
        }
        expected = {
            "team": [
                {"name": "Charlie", "scores": [1000, 2000.2]},
                {"name": "Daisy", "skills": ["Coding", "Design"], "age": 22}
            ]
        }
        self.assertEqual(handle_nested_data(data), expected)

def handle_nested_data(data):
    if isinstance(data, dict):
        # If it's a dictionary, apply the function recursively to each value
        return {key: handle_nested_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        # If it's a list, apply the function recursively to each item
        return [handle_nested_data(item) for item in data]
    elif isinstance(data, bytes):
        # If it's bytes, decode to a UTF-8 string
        return data.decode('utf-8')
    elif isinstance(data, (int, float)):
        # If it's already a number, return as is
        return data
    elif isinstance(data, str):
        # Try to convert strings that represent integers or floats to their numeric forms
        try:
            return int(data)
        except ValueError:
            try:
                return float(data)
            except ValueError:
                return data  # Return the original string if it's not a number
    return data  # Return the data as is for any other type