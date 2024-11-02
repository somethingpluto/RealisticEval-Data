import { createHash } from 'crypto';
import BitArray from 'bitarray-js';

class BloomFilter {
  private size: number;
  private hashCount: number;
  private bitArray: BitArray;

  constructor(size: number, hashCount: number) {
    this.size = size;
    this.hashCount = hashCount;
    this.bitArray = new BitArray(size);
    this.bitArray.fill(false);
  }

  private *hashes(item: string): Generator<number> {
    // Generate multiple hashes for an item
    const itemBuffer = Buffer.from(item, 'utf-8');
    for (let i = 0; i < this.hashCount; i++) {
      // Create a new hash for each hash count using a seed
      const hashResult = createHash('sha256').update(itemBuffer).digest('hex');
      const hashInt = parseInt(hashResult, 16) + i;
      yield hashInt % this.size;
    }
  }

  add(item: string): void {
    // Add an item to the bloom filter
    for (const hashValue of this.hashes(item)) {
      this.bitArray.set(hashValue, true);
    }
  }

  contains(item: string): boolean {
    // Check if an item is in the bloom filter
    for (const hashValue of this.hashes(item)) {
      if (!this.bitArray.get(hashValue)) {
        return false;
      }
    }
    return true;
  }
}