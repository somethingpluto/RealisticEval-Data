function cleanPattern(x, pattern) {
    /**
     * Extracts a numeric value from the input string based on the given regex pattern.
     *
     * @param {any} x The input from which to extract the value. It will be converted to a string.
     * @param {string} pattern The regular expression pattern to use for matching.
     * @returns {number|string} The extracted weight value if a match is found, otherwise an empty string.
     */

    // Convert input to string
    const inputString = String(x);

    // Create a RegExp object from the pattern
    const regex = new RegExp(pattern);

    // Search for the pattern in the input string
    const match = inputString.match(regex);

    if (match) {
        // Extract the weight value from the first matching group
        const weight = match[1];  // Can also use match[3] if needed

        try {
            // Convert the weight to a float and return it
            const weightValue = parseFloat(weight);
            if (!isNaN(weightValue)) {
                return weightValue;
            } else {
                console.warn(`Warning: Unable to convert '${weight}' to float.`);
                return '';
            }
        } catch (error) {
            // Handle cases where conversion to float fails
            console.warn(`Warning: Unable to convert '${weight}' to float.`);
            return '';
        }
    } else {
        return '';  // Return empty string if no match is found
    }
}