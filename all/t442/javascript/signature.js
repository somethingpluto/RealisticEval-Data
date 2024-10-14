/**
 * Convert strings in nested structures (e.g., dictionaries, arrays) to numbers (integers or floating-point numbers) as much as possible.
 *
 * @param {Object|Array} data - The input data before conversion.
 * @returns {Object|Array} - The converted data after processing.
 */
function convertStringsToNumbers(data) {
    if (typeof data === 'object' && data !== null) {
        if (Array.isArray(data)) {
            // Handle array case
            return data.map(item => convertStringsToNumbers(item));
        } else if (data.constructor === Object) {
            // Handle object/dictionary case
            const result = {};
            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    result[key] = convertStringsToNumbers(data[key]);
                }
            }
            return result;
        }
    } else if (typeof data === 'string') {
        try {
            // Try converting to float first, then to int if possible
            const num = parseFloat(data);
            if (!isNaN(num)) {
                if (data.includes('.')) {
                    return num;
                } else {
                    return parseInt(data, 10);
                }
            }
        } catch (error) {
            // Return original string if conversion fails
        }
    }
    // Return data unchanged if it's not a string or object
    return data;
}
