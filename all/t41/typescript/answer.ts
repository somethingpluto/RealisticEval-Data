class BloomFilter {
    private size: number;
    private hashCount: number;
    private bitArray: boolean[];

    constructor(size: number, hashCount: number) {
        this.size = size;
        this.hashCount = hashCount;
        this.bitArray = new Array(this.size).fill(false);
    }

    public add(item: string): void {
        // Add an item to the bloom filter
        const hashes = this.generateHashes(item);
        for (const hash of hashes) {
            this.bitArray[hash % this.size] = true;
        }
    }

    public has(item: string): boolean {
        // Check if an item might be in the bloom filter
        const hashes = this.generateHashes(item);
        return hashes.every(hash => this.bitArray[hash % this.size]);
    }

    private generateHashes(item: string): number[] {
        // Generate hash values for the item
        const hashes: number[] = [];
        for (let i = 0; i < this.hashCount; i++) {
            hashes.push(this.hashFunction(item, i));
        }
        return hashes;
    }

    private hashFunction(item: string, seed: number): number {
        // Simple hash function using a seed
        let hash = 0;
        for (let i = 0; i < item.length; i++) {
            hash = (hash * 31 + item.charCodeAt(i)) ^ seed;
        }
        return Math.abs(hash);
    }
}