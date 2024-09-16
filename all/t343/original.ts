// Generated with ChatGPT
function deepEqual(obj1: any, obj2: any): boolean {
    // Check if the objects are of the same type
    if (typeof obj1 !== typeof obj2) {
        return false;
    }

    // If both objects are null or undefined, consider them equal
    if (obj1 === null || obj1 === undefined) {
        return obj2 === null || obj2 === undefined;
    }

    // If the objects are primitive types, compare them directly
    if (typeof obj1 !== 'object') {
        return obj1 === obj2;
    }

    // Get the keys of both objects
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);

    // If the objects have different number of keys, they are not equal
    if (keys1.length !== keys2.length) {
        return false;
    }

    // Recursively compare each key-value pair
    for (const key of keys1) {
        if (!deepEqual(obj1[key], obj2[key])) {
            return false;
        }
    }

    // All key-value pairs are equal
    return true;
}

export default deepEqual;