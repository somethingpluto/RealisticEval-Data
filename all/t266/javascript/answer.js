function handleNestedData(data) {
    /**
     * Handle nested question structures (e.g., objects, arrays, and enums),
     * decode bytes to UTF8-strings, and convert numbers to integers or floating point numbers.
     *
     * @param {Object} data - Question object
     * @return {Object} After converted question
     */

    if (typeof data === 'object' && data !== null) {
        for (let key in data) {
            if (data.hasOwnProperty(key)) {
                let value = data[key];

                // If value is an array, recursively call handleNestedData on each item
                if (Array.isArray(value)) {
                    data[key] = value.map(item => handleNestedData(item));
                }
                // If value is an object, recursively call handleNestedData
                else if (typeof value === 'object') {
                    data[key] = handleNestedData(value);
                }
                // If value is a number, convert it to integer or float depending on its precision
                else if (typeof value === 'number') {
                    data[key] = Number.isInteger(value) ? Math.floor(value) : parseFloat(value.toFixed(2));
                }
                // If value is a byte string, decode it to UTF-8 string
                else if (value instanceof Uint8Array) {
                    data[key] = new TextDecoder('utf-8').decode(value);
                }
            }
        }
    }

    return data;
}