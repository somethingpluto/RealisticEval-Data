function handleNestedData(data) {
    if (typeof data === 'object' && data !== null) {
        if (Array.isArray(data)) {
            // If it's an array, apply the function recursively to each item
            return data.map(item => handleNestedData(item));
        } else if (data.constructor === Object) {
            // If it's an object, apply the function recursively to each value
            const result = {};
            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    result[key] = handleNestedData(data[key]);
                }
            }
            return result;
        }
    } else if (typeof data === 'string') {
        // Try to parse the string as a number
        const num = Number(data);
        if (!isNaN(num)) {
            return num;
        }
        // Decode bytes if the string is in base64 format
        try {
            const buffer = Buffer.from(data, 'base64');
            return buffer.toString('utf8');
        } catch (error) {
            // Return the original string if it's not a valid base64 encoded string
            return data;
        }
    } else if (typeof data === 'number') {
        // If it's already a number, return as is
        return data;
    }
    // Return the input as is for any other type
    return data;
}