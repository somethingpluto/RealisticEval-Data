import json

class BitSequenceEncoder(json.JSONEncoder):
    """
    A JSON encoder class that converts integer values associated with keys identified as 'bits' into their binary string representation.
    """

    def default(self, obj):
        if isinstance(obj, dict):
            encoded_dict = {}
            for key, value in obj.items():
                if key == 'bits' and isinstance(value, int):
                    encoded_dict[key] = f"{value:08b}"  # Convert to 8-bit binary string
                else:
                    encoded_dict[key] = value
            return encoded_dict
        return super().default(obj)

    def encode(self, obj):
        return json.dumps(self.default(obj), cls=self.__class__, indent=self.indent)
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