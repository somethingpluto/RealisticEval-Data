import functools

def compress_hash(hash_bytes: bytes) -> str:
    return functools.reduce(lambda x, y: str(int(x, 16) | int(y, 16))[2:].zfill(5), [hex(b)[2:] for b in hash_bytes], '')
import hashlib
import unittest


class TestCompressHash(unittest.TestCase):

    def test_length_of_result(self):
        """should return a string of length 5"""
        hash_bytes = hashlib.sha256(b'test').digest()
        result = compress_hash(hash_bytes)
        self.assertEqual(len(result), 5)

    def test_different_inputs(self):
        """should return different strings for different inputs"""
        hash1 = hashlib.sha256(b'test1').digest()
        hash2 = hashlib.sha256(b'test2').digest()
        result1 = compress_hash(hash1)
        result2 = compress_hash(hash2)
        self.assertNotEqual(result1, result2)

    def test_consistent_result_for_same_input(self):
        """should return a consistent result for the same input"""
        hash_bytes = hashlib.sha256(b'test').digest()
        result1 = compress_hash(hash_bytes)
        result2 = compress_hash(hash_bytes)
        self.assertEqual(result1, result2)

    def test_all_zeros(self):
        """should handle a hash of all zeros"""
        hash_bytes = bytes([0] * 32)  # 32 bytes of zeros
        result = compress_hash(hash_bytes)
        self.assertRegex(result, r'^[0-9a-zA-Z]{5}$')

    def test_all_ones(self):
        """should handle a hash of all ones"""
        hash_bytes = bytes([255] * 32)  # 32 bytes of 0xFF (255 in decimal)
        result = compress_hash(hash_bytes)
        self.assertRegex(result, r'^[0-9a-zA-Z]{5}$')

if __name__ == '__main__':
    unittest.main()