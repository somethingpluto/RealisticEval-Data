/**
 * Detects whether the string is in KEBAB_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in KEBAB_CASE, otherwise false.
 */
function isKebabCase(input) {
    // Regular expression to match KEBAB_CASE
    const kebabCaseRegex = /^[a-z]+(-[a-z]+)*$/;
    return kebabCaseRegex.test(input);
}