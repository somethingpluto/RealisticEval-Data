function sizeInBytes(obj) {
    /**
     * Computes and returns the estimated size of an object in bytes.
     * 
     * Args:
     * obj (any): The object to measure the memory size of.
     * 
     * Returns:
     * int: The estimated size of the object in bytes.
     */
    if (typeof obj === 'number') {
        return 8; // Assuming 64-bit floating point number
    } else if (typeof obj === 'string') {
        return obj.length * 2; // Assuming 2 bytes per character
    } else if (typeof obj === 'boolean') {
        return 1; // Assuming 1 byte
    } else if (typeof obj === 'undefined' || obj === null) {
        return 0;
    } else if (Array.isArray(obj)) {
        let size = 8; // Array header size
        for (let item of obj) {
            size += sizeInBytes(item);
        }
        return size;
    } else if (typeof obj === 'object') {
        let size = 8; // Object header size
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                size += key.length * 2 + 2; // Key size + overhead
                size += sizeInBytes(obj[key]);
            }
        }
        return size;
    } else {
        throw new Error('Unsupported type');
    }
}