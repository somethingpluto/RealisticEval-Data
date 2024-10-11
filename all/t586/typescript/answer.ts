/**
 * Detects whether the string is in SNAKE_CASE.
 *
 * @param {string} input - The string to check.
 * @returns {boolean} - True if the string is in SNAKE_CASE, otherwise false.
 */
function isSnakeCase(input: string): boolean {
    // Regular expression to match SNAKE_CASE
    const snakeCaseRegex = /^[a-z]+(_[a-z]+)*$/;
    return snakeCaseRegex.test(input);
}