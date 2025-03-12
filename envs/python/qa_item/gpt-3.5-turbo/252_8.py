import json

class BitSequenceEncoder(json.JSONEncoder):
    def encode(self, obj):
        def convert_bits(item):
            if isinstance(item, dict):
                for key, value in item.items():
                    if key == 'bits' and isinstance(value, int):
                        item[key] = bin(value)[2:].zfill(8)
                    elif isinstance(value, (dict, list)):
                        convert_bits(value)
            elif isinstance(item, list):
                for i in range(len(item)):
                    convert_bits(item[i])
        
        convert_bits(obj)
        return json.dumps(obj)
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