describe('BloomFilter', () => {
  let bloomFilter: BloomFilter;

  beforeEach(() => {
    bloomFilter = new BloomFilter(100, 5); // Initialize with size and hash count
  });

  it('should add an item to the bloom filter', () => {
    bloomFilter.add('item');
    expect(bloomFilter).toContain('item'); // Assuming 'contains' method is implemented
  });
});