/**
 * Implements a Bloom filter class with an add method that adds an element to the Bloom filter.
 * Callers can check for the presence of an element directly.
 */
public class BloomFilter {

    /**
     * Constructs a Bloom filter with the specified size and number of hash functions.
     *
     * @param size       the size of the Bloom filter
     * @param hashCount  the number of hash functions to use
     */
    public BloomFilter(int size, int hashCount) {
        // Constructor implementation goes here
    }

    /**
     * Adds an item to the Bloom filter.
     *
     * @param item the item to add
     */
    public void add(String item) {
        // Add an item to the Bloom filter
        // Implementation goes here
    }

    /**
     * Checks if an item is possibly present in the Bloom filter.
     *
     * @param item the item to check
     * @return true if the item might be present, false otherwise
     */
    public boolean contains(String item) {
        // Check if the item is possibly present in the Bloom filter
        // Implementation goes here
    }

}