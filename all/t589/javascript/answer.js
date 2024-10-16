function extractJson(response) {
    const startPos = response.indexOf('{'); // Find the position of the first '{'
    if (startPos === -1) // If not found, return an empty string
        return "";

    let braceCount = 0; // To track the balance of braces
    let endPos = startPos; // Initialize endPos to startPos

    for (let i = startPos; i < response.length; i++) {
        if (response[i] === '{') {
            braceCount++; // Increment for every '{'
        } else if (response[i] === '}') {
            braceCount--; // Decrement for every '}'
        }

        // If braceCount returns to zero, we found the complete JSON object
        if (braceCount === 0) {
            endPos = i; // Set endPos to the current position
            break; // Break out of the loop
        }
    }

    // If braceCount is not zero, it means there was an imbalance (unmatched braces)
    if (braceCount !== 0) {
        return ""; // Return empty string if JSON is incomplete
    }

    // Extract and return the substring that represents the JSON object
    return response.substring(startPos, endPos + 1);
}