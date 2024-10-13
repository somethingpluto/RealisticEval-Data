/**
 * Implement a Bloom filter class with an add method that adds an element to the Bloom filter.
 * Callers can check for the presence of an element directly using the in keyword.
 */
class BloomFilter {
public:
    /**
     * Constructor for the BloomFilter class.
     *
     * @param size The size of the bit array.
     * @param hash_count The number of hash functions to use.
     */
    BloomFilter(size_t size, size_t hash_count);

    /**
     * Add an item to the Bloom filter.
     *
     * @param item The item to add.
     */
    void add(const std::string& item);

private:
    size_t size;          // Size of the bit array
    size_t hash_count;    // Number of hash functions
    std::vector<bool> bit_array; // Bit array for the Bloom filter
};