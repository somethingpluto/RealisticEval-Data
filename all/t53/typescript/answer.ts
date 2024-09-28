/**
 * Computes and returns an approximate size of an object in bytes.
 *
 * @param obj The object to measure the memory size of.
 * @returns The size of the object in bytes (approximate).
 */
function sizeInBytes(obj: any): number {
  if (typeof obj === 'string') {
    // For strings, use Buffer to get byte length
    return Buffer.byteLength(obj, 'utf8');
  } else if (Array.isArray(obj)) {
    // Approximate size for arrays
    return obj.reduce((sum, item) => sum + sizeInBytes(item), 0);
  } else if (typeof obj === 'object' && obj !== null) {
    // Approximate size for objects
    return Object.keys(obj).reduce((sum, key) => sum + sizeInBytes(key) + sizeInBytes(obj[key]), 0);
  } else {
    // Fallback for other types like number, boolean, null
    return 0;
  }
}

// Example usage
const exampleObject = { key: 'value', anotherKey: 123 };
console.log(sizeInBytes(exampleObject));