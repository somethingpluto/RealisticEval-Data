import hashlib

class BloomFilter:
    """
    Implement a bloom filter class with an add method that adds an element to the Bloom filter.
    Callers can check for the presence of an element directly using the in keyword.
    """

    def __init__(self, size, hash_count):
        """
        Initialize the Bloom filter with a given size and number of hash functions.

        :param size: The size of the bit array.
        :param hash_count: The number of hash functions to use.
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [False] * size

    def _hash(self, item, seed):
        """
        Generate a hash value for the given item using the specified seed.

        :param item: The item to hash.
        :param seed: The seed for the hash function.
        :return: The hash value.
        """
        hash_obj = hashlib.sha256()
        hash_obj.update(str(item).encode('utf-8'))
        hash_obj.update(str(seed).encode('utf-8'))
        return int(hash_obj.hexdigest(), 16) % self.size

    def add(self, item):
        """
        Add an item to the Bloom filter.

        :param item: The item to add.
        """
        for seed in range(self.hash_count):
            index = self._hash(item, seed)
            self.bit_array[index] = True

    def __contains__(self, item):
        """
        Check if an item is in the Bloom filter.

        :param item: The item to check.
        :return: True if the item is possibly in the filter, False if it is definitely not.
        """
        for seed in range(self.hash_count):
            index = self._hash(item, seed)
            if not self.bit_array[index]:
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