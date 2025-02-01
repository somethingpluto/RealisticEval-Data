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
        this.bitArray = new Uint8Array(size / 8);
    }

    /**
     * Adds an item to the Bloom filter.
     * @param {string} item - The item to add.
     */
    add(item) {
        const hashes = this._hashes(item);
        for (const hash of hashes) {
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
        const hashes = this._hashes(item);
        for (const hash of hashes) {
            const index = hash % this.size;
            const byteIndex = Math.floor(index / 8);
            const bitIndex = index % 8;
            if ((this.bitArray[byteIndex] & (1 << bitIndex)) === 0) {
                return false;
            }
        }
        return true;
    }

    /**
     * Generates the hash values for the given item using the specified hash functions.
     * @param {string} item - The item to hash.
     * @returns {number[]} - An array of hash values.
     */
    _hashes(item) {
        const hashes = [];
        for (let i = 0; i < this.hashCount; i++) {
            const hash = murmurhash3(item, i);
            hashes.push(hash);
        }
        return hashes;
    }
}

// MurmurHash3 implementation (murmurhash3.js)
// This is a simplified version of the MurmurHash3 algorithm.
// For a complete implementation, please refer to the original source or a reliable library.
function murmurhash3(key, seed) {
    let c1 = 0xcc9e2d51;
    let c2 = 0x1b873593;
    let r1 = 15;
    let r2 = 13;
    let m = 5;
    let n = 0xe6546b64;
    let h = seed;
    let k = 0;
    let len = key.length;

    for (let i = 0; i + 4 <= len; i += 4) {
        k = (key.charCodeAt(i) & 0xff) | ((key.charCodeAt(i + 1) & 0xff) << 8) | ((key.charCodeAt(i + 2) & 0xff) << 16) | ((key.charCodeAt(i + 3) & 0xff) << 24);
        k = Math.imul(k, c1);
        k = (k << r1) | (k >>> (32 - r1));
        k = Math.imul(k, m);
        k = (k << r2) | (k >>> (32 - r2));
        h ^= k;
        h = (h << r1) | (h >>> (32 - r1));
        h = h * m + n;
    }

    switch (len & 3) {
        case 3:
            h ^= (key.charCodeAt(len - 1) & 0xff) << 16;
        case 2:
            h ^= (key.charCodeAt(len - 2) & 0xff) << 8;
        case 1:
            h ^= key.charCodeAt(len - 3) & 0xff;
            h = Math.imul(h, c1);
            h = (h << r1) | (h >>> (32 - r1));
            h = Math.imul(h, m);
            h = (h << r2) | (h >>> (32 - r2));
    }

    h ^= len;
    h ^= h >>> 16;
    h = Math.imul(h, 0x85ebca6b);
    h ^= h >>> 13;
    h = Math.imul(h, 0xc2b2ae35);
    h ^= h >>> 16;

    return h >>> 0;
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
