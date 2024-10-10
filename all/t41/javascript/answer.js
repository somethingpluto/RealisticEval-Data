class BloomFilter {
    /**
     * Implement a bloom filter class with an add method that adds an element to the Bloom filter.
     * Callers can check for the presence of an element directly using the 'includes' method.
     */

    constructor(size, hashCount) {
        // Initialize the Bloom Filter
        this.size = size;
        this.hashCount = hashCount;
        this.filter = new Array(size).fill(false);
    }

    add(item) {
        // Add an item to the Bloom Filter
        for (let i = 0; i < this.hashCount; i++) {
            const index = this._hash(item, i);
            this.filter[index] = true;
        }
    }

    _hash(item, seed) {
        let hash = 0;
        for (let i = 0; i < item.length; i++) {
            hash = ((hash << 5) - hash + item.charCodeAt(i) + seed) | 0;
        }
        return Math.abs(hash % this.size);
    }

    includes(item) {
        for (let i = 0; i < this.hashCount; i++) {
            const index = this._hash(item, i);
            if (!this.filter[index]) {
                return false;
            }
        }
        return true;
    }
}