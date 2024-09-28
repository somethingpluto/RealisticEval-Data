class BloomFilter {
    constructor(size, hashCount) {
        this.size = size;
        this.hashCount = hashCount;
        this.bitArray = new Array(size).fill(false);
    }

    _hashes(item) {
        const crypto = require('crypto');
        const hashes = [];
        const itemBuffer = Buffer.from(item, 'utf-8');
        for (let i = 0; i < this.hashCount; i++) {
            const hash = crypto.createHash('sha256').update(itemBuffer).digest('hex');
            const hashInt = parseInt(hash, 16) + i;
            hashes.push(hashInt % this.size);
        }
        return hashes;
    }

    add(item) {
        const hashValues = this._hashes(item);
        for (const hashValue of hashValues) {
            this.bitArray[hashValue] = true;
        }
    }

    contains(item) {
        const hashValues = this._hashes(item);
        return hashValues.every(hashValue => this.bitArray[hashValue]);
    }
}

// Usage Example:
const bloom = new BloomFilter(1000, 7);
bloom.add("Hello");
console.log(bloom.contains("Hello")); // true
console.log(bloom.contains("World")); // false