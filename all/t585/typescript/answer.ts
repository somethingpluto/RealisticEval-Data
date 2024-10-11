/**
 * Detects whether the string is in CAMEL_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in CAMEL_CASE, otherwise false.
 */
function isCamelCase(input: string): boolean {
    // Regular expression to match CAMEL_CASE
    const camelCaseRegex = /^[a-z]+([A-Z][a-z]*)*$/;
    return camelCaseRegex.test(input);
}