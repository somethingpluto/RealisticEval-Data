function sizeInBytes(obj: any): number {
    /**
     * Computes and returns the size of an object in bytes in memory
     *
     * @param {any} obj - The object whose size is being computed.
     * @returns {number} The size of the object in bytes in memory.
     */
    
    // Note: In JavaScript/TypeScript, there's no built-in way to get the exact memory usage of an object,
    // so we're using Buffer.byteLength() as a proxy for string data sizes.

    if (typeof obj === 'string') {
        return Buffer.byteLength(obj);
    } else if (Buffer.isBuffer(obj)) {
        return obj.length;
    } else if (Array.isArray(obj)) {
        return obj.reduce((sum, item) => sum + sizeInBytes(item), 0);
    } else if (obj instanceof Object) {
        return Object.keys(obj).reduce((sum, key) => sum + sizeInBytes(key) + sizeInBytes(obj[key]), 0);
    } else {
        return 0; // For primitive types like numbers, booleans, null, undefined etc., their memory usage is negligible
    }
}