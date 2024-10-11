#include <vector>
#include <functional>

class BloomFilter {
public:
    /**
     * Implement a bloom filter class with an add method that adds an element to the Bloom filter.
     * Callers can check for the presence of an element directly using the in keyword.
     */

    BloomFilter(size_t size, size_t hash_count);

    void add(const std::string& item);
};