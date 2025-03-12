/**
 * Implement a Bloom filter class with an add method that adds an element to the Bloom filter.
 * Callers can check for the presence of an element directly using the `contains` method.
 */
class BloomFilter {
    /**
     * Constructs a new BloomFilter instance.
     * @param {number} size - The size of the Bloom filter.
     * @param {number} hashCount - The number of hash functions to use.
     */
    constructor(size, hashCount) {
        this.size = size;
        this.hashCount = hashCount;
        this.bitArray = new Uint8Array(Math.ceil(size / 8));
    }

    /**
     * Adds an item to the Bloom filter.
     * @param {string} item - The item to add.
     */
    add(item) {
        for (let i = 0; i < this.hashCount; i++) {
            const hash = this._hash(item, i);
            const index = hash % this.size;
            const byteIndex = Math.floor(index / 8);
            const bitIndex = index % 8;
            this.bitArray[byteIndex] |= (1 << bitIndex);
        }
    }

    /**
     * Checks if an item is possibly in the Bloom filter.
     * @param {string} item - The item to check.
     * @returns {boolean} - True if the item might be in the Bloom filter, false otherwise.
     */
    contains(item) {
        for (let i = 0; i < this.hashCount; i++) {
            const hash = this._hash(item, i);
            const index = hash % this.size;
            const byteIndex = Math.floor(index / 8);
            const bitIndex = index % 8;
            if (!(this.bitArray[byteIndex] & (1 << bitIndex))) {
                return false;
            }
        }
        return true;
    }

    /**
     * Generates a hash value for the given item using a simple hash function.
     * @param {string} item - The item to hash.
     * @param {number} seed - The seed for the hash function.
     * @returns {number} - The hash value.
     */
    _hash(item, seed) {
        let hash = 0;
        for (let i = 0; i < item.length; i++) {
            const char = item.charCodeAt(i);
            hash = (hash << 5) - hash + char;
            hash |= 0; // Convert to 32bit integer
            hash += seed;
            hash &= hash; // Convert to 32bit integer
        }
        return Math.abs(hash);
    }
}
describe('BloomFilter', () => {
    let bf;

    beforeEach(() => {
        // Initialize BloomFilter with reasonable size and hash count for testing
        bf = new BloomFilter(1000, 5);
    });

    it('adds elements and reports them as present', () => {
        // Test that added elements are reported as present
        const testItem = "hello world";
        bf.add(testItem);
        expect(bf.contains(testItem)).toBe(true);
    });

    it('reports unadded elements as absent', () => {
        // Test that an unadded element is not present
        expect(bf.contains("random item")).toBe(false);
    });

    it('checks for false positives', () => {
        // Adding some elements and check for a false positive
        const itemsToAdd = ["item1", "item2", "item3"];
        itemsToAdd.forEach(item => {
            bf.add(item);
        });
        // Check for an item not added, expecting a very low chance of false positive due to size and hash count
        expect(bf.contains("item4")).toBe(false);
    });

    it('handles hash collisions correctly', () => {
        // Test how the Bloom filter handles hash collisions by adding similar items
        bf.add("item123");
        bf.add("item124");
        expect(bf.contains("item123")).toBe(true);
        expect(bf.contains("item124")).toBe(true);
    });

    it('reports no items in an empty Bloom Filter', () => {
        // Ensure that an empty Bloom Filter reports no items
        expect(bf.contains("anything")).toBe(false);
    });
});
