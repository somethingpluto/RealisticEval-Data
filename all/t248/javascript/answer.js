function sanitizeData(data, keyToRemove = null) {
    // Check if keyToRemove is null or undefined and set it as an empty array if true
    if (!keyToRemove) {
        keyToRemove = [];
    }

    // Create a new object to store the sanitized data
    let sanitizedData = {};

    // Iterate over each key-value pair in the original data
    for(let key in data) {
        // If the current key is not in the keyToRemove array, add it to the sanitizedData object
        if(!keyToRemove.includes(key)) {
            sanitizedData[key] = data[key];
        }
    }

    return sanitizedData;
}