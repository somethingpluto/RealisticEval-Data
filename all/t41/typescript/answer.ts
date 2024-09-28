import * as crypto from 'crypto';

class BitArray {
    private array: boolean[];

    constructor(size: number) {
        this.array = new Array(size).fill(false);
    }

    setAll(value: boolean): void {
        this.array.fill(value);
    }

    set(index: number, value: boolean): void {
        this.array[index] = value;
    }

    get(index: number): boolean {
        return this.array[index];
    }
}

class BloomFilter {
    private size: number;
    private hashCount: number;
    private bitArray: BitArray;

    constructor(size: number, hashCount: number) {
        this.size = size;
        this.hashCount = hashCount;
        this.bitArray = new BitArray(size);
    }

    private hashes(item: string): Iterable<number> {
        const encodedItem = Buffer.from(item, 'utf-8');
        const results: number[] = [];

        for (let i = 0; i < this.hashCount; i++) {
            const hash = crypto.createHash('sha256')
                               .update(encodedItem)
                               .digest('hex');
            const hashResult = parseInt(hash, 16) + i;
            const index = hashResult % this.size;
            results.push(index);
        }

        return results;
    }

    add(item: string): void {
        for (const hashValue of this.hashes(item)) {
            this.bitArray.set(hashValue, true);
        }
    }

    contains(item: string): boolean {
        for (const hashValue of this.hashes(item)) {
            if (!this.bitArray.get(hashValue)) {
                return false;
            }
        }
        return true;
    }
}

// Usage
const bloomFilter = new BloomFilter(1000, 5);
bloomFilter.add('apple');

if (bloomFilter.contains('apple')) {
  console.log('apple is probably in the set');
} else {
  console.log('apple is definitely not in the set');
}