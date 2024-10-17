function camelToSnake(camelStr) {
    /**
     * Convert a CamelCase string to snake_case.
     *
     * @param {string} camelStr - The CamelCase string to convert.
     * @returns {string} The converted snake_case string.
     */
    // Use regular expression to insert underscores before each uppercase letter,
    // and then convert the whole string to lowercase
    const snakeCaseStr = camelStr.replace(/(?<!^)(?=[A-Z])/g, '_').toLowerCase();
    return snakeCaseStr;
}