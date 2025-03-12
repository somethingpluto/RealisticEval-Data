import { createHash } from 'crypto';

class BloomFilter {
  // ... (rest of the class remains unchanged)

  /**
   * Initializes the Bloom filter with a specified size and number of hash functions.
   * @param size The size of the bit array.
   * @param hashCount The number of hash functions to use.
   */
  constructor(size: number, hashCount: number) {
    if (size <= 0 || hashCount <= 0 || hashCount > size) {
      throw new Error('Invalid size or hash count');
    }
    this.size = size;
    this.hashCount = hashCount;
    this.bitArray = new Array(size).fill(false);
  }

  /**
   * Adds an item to the Bloom filter.
   * @param item The item to add.
   */
  add(item: string): void {
    if (item === null || item === undefined) {
      throw new Error('Item cannot be null or undefined');
    }
    for (let i = 0; i < this.hashCount; i++) {
      const hash = this.hashFunction(i, item);
      const index = hash % this.size;
      this.bitArray[index] = true;
    }
  }

  /**
   * Checks if an item is possibly in the Bloom filter.
   * @param item The item to check.
   * @returns true if the item might be in the Bloom filter, false otherwise.
   */
  contains(item: string): boolean {
    if (item === null || item === undefined) {
      throw new Error('Item cannot be null or undefined');
    }
    for (let i = 0; i < this.hashCount; i++) {
      const hash = this.hashFunction(i, item);
      const index = hash % this.size;
      if (!this.bitArray[index]) {
        return false;
      }
    }
    return true;
  }

  /**
   * Generates a hash for the given item and index.
   * @param index The index of the hash function.
   * @param item The item to hash.
   * @returns A hash value.
   */
  private hashFunction(index: number, item: string): number {
    const hash = createHash('sha256');
    hash.update(item);
    return parseInt(hash.digest('hex'), 16) % this.size;
  }
}
describe('BloomFilter', () => {
  let bf: BloomFilter;

  beforeEach(() => {
    // Initialize BloomFilter with reasonable size and hash count for testing
    bf = new BloomFilter(1000, 5);
  });

  it('adds elements and checks their presence', () => {
    // Test that added elements are reported as present
    const testItem = "hello world";
    bf.add(testItem);
    expect(bf.contains(testItem)).toBe(true);
  });

  it('checks absence of unadded elements', () => {
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

  it('handles hash collisions with similar items', () => {
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
