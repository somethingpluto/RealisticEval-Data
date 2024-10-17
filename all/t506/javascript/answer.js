function snakeToCamel(snakeStr) {
    /**
     * Convert a snake_case string to CamelCase.
     *
     * @param {string} snakeStr - The snake_case string to convert.
     * @returns {string} The converted CamelCase string.
     */
    // Split the snake_case string into words
    const words = snakeStr.split('_');
    // Capitalize the first letter of each word and join them
    const camelCaseStr = words.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
    return camelCaseStr;
}