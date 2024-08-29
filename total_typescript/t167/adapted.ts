/**
 * Determines whether a given string (assumed to end with ".bit") is a valid 3-digit integer.
 *
 * The function removes the ".bit" suffix, checks if the remaining part is a number,
 * and verifies if it falls within the range of 0 to 999.
 *
 * @param {string} bitName - The string to validate.
 * @returns {boolean} True if the remaining part after removing ".bit" is a valid 3-digit integer, otherwise false.
 */
export function assert999(bitName: string): boolean {
    // Remove the ".bit" suffix from the string
    const numericString = bitName.replace(".bit", "");

    // Convert the remaining part to an integer
    const num = parseInt(numericString);

    // Regular expression to ensure the string is a 1 to 3 digit number
    const regex = /^[0-9]{1,3}$/;

    // Check if the string matches the regex and if the number is within the valid range
    return regex.test(numericString) && !isNaN(num) && num >= 0 && num <= 999;
}
