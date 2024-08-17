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
