/**
 * Converts a thread object to a JSON file represented as a Blob.
 * 
 * @param {Object} thread - The thread object to be converted.
 * @returns {Blob} - A Blob representing the JSON file.
 */
function convertThreadToJSONFile(thread) {
    const jsonString = JSON.stringify(thread);  // Convert the thread object to a JSON string
    const jsonBlob = encodeStringAsBlob(jsonString);  // Encode the JSON string as a Blob
    return jsonBlob;
}
