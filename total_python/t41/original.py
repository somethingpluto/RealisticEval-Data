class BloomFilter:
    def __init__(self, size, num_hash_functions, hash_f=hash_f):
        self.size = size
        self.num_hash_functions = num_hash_functions
        self.bit_array = [False] * size
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