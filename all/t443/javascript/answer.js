function compressWhitespace(inputString) {
    /**
     * Compress multiple consecutive whitespace characters in a string into a single space.
     *
     * @param {string} inputString - The string to be processed.
     * @returns {string} - The processed string with compressed whitespace.
     */
    // Split the input string by whitespace and join with a single space
    return inputString.split(/\s+/).join(' ');
}