function sortObjectsByKey(array, key) {
    if (!Array.isArray(array)) {
        throw new TypeError("The first argument must be an array.");
    }
    if (typeof key !== 'string') {
        throw new TypeError("The key must be a string.");
    }
    if (array.length === 0) {
        throw new Error("The array should not be empty.");
    }
    if (!array.every(obj => obj.hasOwnProperty(key))) {
        throw new Error(`The key "${key}" does not exist in one or more objects.`);
    }

    return array.slice().sort((a, b) => {
        const valueA = String(a[key]).toLowerCase(); // Convert to string to handle non-string fields
        const valueB = String(b[key]).toLowerCase();

        return valueA.localeCompare(valueB);
    });
}