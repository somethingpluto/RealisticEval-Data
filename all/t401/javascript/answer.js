function findPlaceholders(text) {
    /**
     * Find and return an array of all placeholders in the format {{ placeholder }} from the input text.
     *
     * @param {string} text - The input string containing potential placeholders.
     * @returns {Array} - An array of matching placeholders.
     */

    // Regular expression to match placeholders
    const regex = /{{\s*[^{}]*\s*}}/g;

    // Find all matches using regex
    let matches;
    const result = [];

    while ((matches = regex.exec(text)) !== null) {
        result.push(matches[0].trim());
    }

    return result;
}