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
