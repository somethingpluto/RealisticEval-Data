function convertToShortFormat(inputStr) {
    /**
     * Converts a string concatenated with underscores to a short format.
     *
     * @param {string} inputStr - The input string with segments separated by underscores.
     * @return {string} A short format string derived from the first characters of each segment.
     */
    // Split the input string by underscores
    const segments = inputStr.split('_');

    // Extract the first character from each segment and join them
    const shortFormat = segments.map(segment => segment[0]).join('');

    return shortFormat;
}