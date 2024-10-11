function removeTripleBackticks(stringArray) {
    /**
     * Process an array of strings, removing the three consecutive backticks from each string.
     *
     * @param {string[]} stringArray - The array of strings to process.
     * @returns {string[]} A new array with all instances of three consecutive backticks removed from each string.
     */

    return stringArray.map(str => str.replace(/`{3}/g, ''));
}