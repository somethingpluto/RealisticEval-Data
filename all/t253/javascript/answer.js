import json from 'json'
function log(item) {
    /**
     * Logs an item by printing it. Handles strings, numbers, arrays, and objects by printing
     * them directly or as a JSON-formatted string. Other types are reported as errors.
     *
     * @param {*} item - The item to be logged. Can be of any type.
     */
    // Handling for strings, numbers
    if (typeof item === 'string' || typeof item === 'number') {
        console.log(item);
    }
    // Handling for objects and arrays to convert to JSON string
    else if (Array.isArray(item) || typeof item === 'object' && item !== null) {
        try {
            console.log(JSON.stringify(item, null, 4));  // Pretty print JSON for better readability
        } catch (e) {
            console.log(`Error: Failed to serialize item to JSON. ${e.message}`);
        }
    } else {
        // Print an informative error message for unsupported types
        console.log(`Error: Unsupported type ${typeof item} for logging.`);
    }
}