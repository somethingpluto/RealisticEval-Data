import unittest
import json


class TestBitSequenceEncoder(unittest.TestCase):
    def test_single_bit_conversion(self):
        # Test a single dictionary entry with 'bits' key
        data = {'bits': 2}
        expected_output = '{"bits": "00000010"}'
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, expected_output)

    def test_nested_bit_conversion(self):
        # Test nested dictionaries with 'bits' key
        data = {'level1': {'level2': {'bits': 255}}}
        expected_output = '{"level1": {"level2": {"bits": "11111111"}}}'
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, expected_output)

    def test_no_bit_key(self):
        # Test dictionaries without 'bits' key
        data = {'name': 'test', 'value': 123}
        expected_output = '{"name": "test", "value": 123}'
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, expected_output)

    def test_mixed_contents(self):
        # Test dictionaries with mixed contents
        data = {'name': 'test', 'bits': 5, 'details': {'bits': 0}}
        expected_output = '{"name": "test", "bits": "00000101", "details": {"bits": "00000000"}}'
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, expected_output)

    def test_list_handling(self):
        # Test lists containing dictionaries with 'bits' key
        data = [{'bits': 1}, {'bits': 16}]
        expected_output = '[{"bits": "00000001"}, {"bits": "00010000"}]'
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, expected_output)

import json


class BitSequenceEncoder(json.JSONEncoder):
    """
    Custom JSON encoder class that converts dictionary entries with the key 'bits'
    into a binary string format.

    This encoder transforms only those entries in a dictionary where the key is 'bits',
    formatting their values as 8-bit binary strings. Other entries are left unchanged.
    """

    def default(self, obj):
        """
        Overridden method from json.JSONEncoder to provide custom encoding logic.

        Args:
            obj (any): The object to encode.

        Returns:
            any: The encoded object or super().default(obj) for types unsupported by this encoder.
        """

        # Helper function to recursively convert dictionary entries
        def convert_bits(item):
            if isinstance(item, dict):
                # Transform the dictionary, applying binary formatting if the key is 'bits'
                return {k: (f'{v:08b}' if k == 'bits' else convert_bits(v)) for k, v in item.items()}
            elif isinstance(item, list):
                # Apply conversion to each element in the list
                return [convert_bits(v) for v in item]
            else:
                # Return the item unchanged if it's not a dictionary or list
                return item

        # Use the helper function to process the top-level object
        return convert_bits(obj)
