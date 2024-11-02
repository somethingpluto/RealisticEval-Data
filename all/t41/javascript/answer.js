import crypto from 'crypto'
class BloomFilter {
    constructor(size, hashCount) {
        this.size = size;
        this.hashCount = hashCount;
        this.bitArray = new Uint8Array(size / 8);
    }

    _hashes(item) {
        // Generate multiple hashes for an item
        const itemBuffer = Buffer.from(item, 'utf-8');
        for (let i = 0; i < this.hashCount; i++) {
            // Create a new hash for each hash count using a seed
            const hashResult = crypto.createHash('sha256').update(itemBuffer).digest('hex');
            const numericHashResult = parseInt(hashResult, 16) + i;
            yield numericHashResult % this.size;
        }
    }

    add(item) {
        // Add an item to the bloom filter
        for (const hashValue of this._hashes(item)) {
            const byteIndex = Math.floor(hashValue / 8);
            const bitIndex = hashValue % 8;
            this.bitArray[byteIndex] |= (1 << bitIndex);
        }
    }

    contains(item) {
        // Check if an item is in the bloom filter
        for (const hashValue of this._hashes(item)) {
            const byteIndex = Math.floor(hashValue / 8);
            const bitIndex = hashValue % 8;
            if ((this.bitArray[byteIndex] & (1 << bitIndex)) === 0) {
                return false;
            }
        }
        return true;
    }
}