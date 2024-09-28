const BloomFilter = require('./path/to/BloomFilter');  // Adjust the path as necessary

describe('BloomFilter', () => {
    let bf;

    beforeEach(() => {
        // Initialize BloomFilter with reasonable size and hash count for testing
        bf = new BloomFilter(1000, 5);
    });

    test('should report added elements as present', () => {
        const testItem = "hello world";
        bf.add(testItem);
        expect(bf.contains(testItem)).toBe(true);
    });

    test('should report an unadded element as absent', () => {
        expect(bf.contains("random item")).toBe(false);
    });

    test('should have a very low false positive rate', () => {
        const itemsToAdd = ["item1", "item2", "item3"];
        itemsToAdd.forEach(item => bf.add(item));
        // Check for an item not added, expecting a very low chance of false positive due to size and hash count
        expect(bf.contains("item4")).toBe(false);
    });

    test('should handle hash collisions', () => {
        bf.add("item123");
        bf.add("item124");
        expect(bf.contains("item123")).toBe(true);
        expect(bf.contains("item124")).toBe(true);
    });

    test('should report no items present in an empty BloomFilter', () => {
        expect(bf.contains("anything")).toBe(false);
    });
});