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