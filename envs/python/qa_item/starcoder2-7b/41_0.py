import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bytearray(size)

    def add(self, item):
        digests = []
        for i in range(self.hash_count):
            digest = hashlib.sha256(str(item).encode('utf-8')).hexdigest()
            digest = int(digest, 16) % self.size
            digests.append(digest)
            
        for digest in digests:
            self.bit_array[digest] = 1

    def __contains__(self, item):
        for i in range(self.hash_count):
            digest = hashlib.sha256(str(item).encode('utf-8')).hexdigest()
            digest = int(digest, 16) % self.size
            if self.bit_array[digest] == 0:
                return False
        return True
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
if __name__ == '__main__':
    unittest.main()