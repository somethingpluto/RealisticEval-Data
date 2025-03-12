
import json

class BitSequenceEncoder(json.JSONEncoder):
    """
    Write a JSON decoding class that inherits from json.JSONEncoder. When encoding question into json format, the main functional bits of this class specifically handle keys identified as bits, and convert them to binary form if their value is an integer
    For example 'bits': 255 after encoder "bits": "11111111"

    """

    def encode(self, obj):
        if obj.get('bits') is not None:
            # Convert integer to binary form
            binary_value = int(obj.get('bits'), 2)
            # Convert binary form back to string
            return str(binary_value)
        else:
            return json.JSONEncoder.encode(obj, safe=False)

import unittest
import json

class TestBitSequenceEncoder(unittest.TestCase):
    def test_basic_encoding(self):
        """ Test encoding with simple dictionary containing 'bits'. """
        data = {'name': 'Processor', 'bits': 255}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"name": "Processor", "bits": "11111111"}')

    def test_nested_encoding(self):
        """ Test encoding with nested dictionary containing 'bits'. """
        data = {'component': {'name': 'ALU', 'bits': 128}, 'bits': 1}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"component": {"name": "ALU", "bits": "10000000"}, "bits": "00000001"}')

    def test_non_bits_key(self):
        """ Test encoding with dictionary not containing 'bits' key. """
        data = {'name': 'Processor', 'value': 123}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"name": "Processor", "value": 123}')

    def test_no_bits_conversion_needed(self):
        """ Test encoding with dictionary where 'bits' key needs no conversion. """
        data = {'name': 'Unit', 'bits': 'Already binary'}
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"name": "Unit", "bits": "Already binary"}')

    def test_complex_structure_with_bits(self):
        """ Test encoding a complex dictionary structure containing multiple 'bits' keys. """
        data = {
            'processor': {'bits': 3, 'type': 'A'},
            'memory': {'bits': 255, 'size': 16},
            'ports': {'count': 2, 'bits': 128}
        }
        result = json.dumps(data, cls=BitSequenceEncoder)
        self.assertEqual(result, '{"processor": {"bits": "00000011", "type": "A"}, "memory": {"bits": "11111111", "size": 16}, "ports": {"count": 2, "bits": "10000000"}}')

if __name__ == '__main__':
    unittest.main()