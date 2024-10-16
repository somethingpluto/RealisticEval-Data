/**
 * Detects whether the string is in PASCAL_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in PASCAL_CASE, otherwise false.
 */
function isPascalCase(input) {
    // Regular expression to match PASCAL_CASE
    const pascalCaseRegex = /^[A-Z][a-z]*(?:[A-Z][a-z]*)*$/;
    return pascalCaseRegex.test(input);
}