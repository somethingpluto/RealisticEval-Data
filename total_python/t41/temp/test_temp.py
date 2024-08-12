import unittest


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        # Initialize BloomFilter with reasonable size and hash count for testing
        self.bf = BloomFilter(1000, 5)

    def test_add_and_check_presence(self):
        # Test that added elements are reported as present
        test_item = "hello world"
        self.bf.add(test_item)
        self.assertIn(test_item, self.bf)

    def test_check_absence(self):
        # Test that an unadded element is not present
        self.assertNotIn("random item", self.bf)

    def test_false_positives(self):
        # Adding some elements and check for a false positive
        items_to_add = ["item1", "item2", "item3"]
        for item in items_to_add:
            self.bf.add(item)
        # Check for an item not added, expecting a very low chance of false positive due to size and hash count
        self.assertNotIn("item4", self.bf)

    def test_collision_handling(self):
        # Test how the Bloom filter handles hash collisions by adding similar items
        self.bf.add("item123")
        self.bf.add("item124")
        self.assertIn("item123", self.bf)
        self.assertIn("item124", self.bf)

    def test_empty_bloom_filter(self):
        # Ensure that an empty Bloom Filter reports no items
        self.assertNotIn("anything", self.bf)
import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        # Generate multiple hashes for an item
        item = item.encode('utf-8')
        for i in range(self.hash_count):
            # Create a new hash for each hash count using a seed
            hash_result = hashlib.sha256(item).hexdigest()
            hash_result = int(hash_result, 16) + i
            yield hash_result % self.size

    def add(self, item):
        # Add an item to the bloom filter
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = True

    def __contains__(self, item):
        # Implement the in keyword functionality
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))