describe('BloomFilter', () => {
    let bloomFilter;

    beforeEach(() => {
        bloomFilter = new BloomFilter(100, 2); // Initialize with a size of 100 and 2 hash functions
    });

    test('should add items to the bloom filter', () => {
        bloomFilter.add('apple');
        expect(bloomFilter.contains('apple')).toBe(true);
    });

    test('should not contain items not added to the bloom filter', () => {
        expect(bloomFilter.contains('banana')).toBe(false);
    });

    test('should handle collisions correctly', () => {
        bloomFilter.add('apple');
        bloomFilter.add('apples');
        expect(bloomFilter.contains('apple')).toBe(true);
        expect(bloomFilter.contains('apples')).toBe(true);
    });
});