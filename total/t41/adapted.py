from bitarray import bitarray
import hashlib

def simple_hash(item, seed):
    result = int(hashlib.sha256(f"{item}{seed}".encode()).hexdigest(), 16)
    return result

class BloomFilter:
    def __init__(self, size, num_hash_functions, hash_f=simple_hash):
        self.size = size
        self.num_hash_functions = num_hash_functions
        self.bit_array = bitarray(size)
        self.bit_array.setall(False)
        self.hash_f = hash_f

    def add(self, item):
        for seed in range(self.num_hash_functions):
            index = self.hash_f(item, seed) % self.size
            self.bit_array[index] = True

    def __contains__(self, item):
        for seed in range(self.num_hash_functions):
            index = self.hash_f(item, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True

# Usage
b_filter = BloomFilter(1024, 5)
b_filter.add("test")
print("test" in b_filter)  # Expected True
print("hello" in b_filter)  # Expected False (most likely)
