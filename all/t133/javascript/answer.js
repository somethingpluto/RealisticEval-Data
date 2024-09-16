/**
 * Tests whether the input string is a valid number between 5 and 18
 *
 * @param {string} inputNumber - The input string to validate.
 * @returns {string|boolean} - Returns "Not Numerical" if the input is not a number,
 *                             "Invalid Length, Must Be Between 5-18" if the input length
 *                             is not within the required range, true if the input is valid,
 *                             or "Invalid Input" in case of unexpected errors.
 */
function isValidNumber(inputNumber) {
    try {
        const trimmedNumber = inputNumber.trim();

        // Check if the trimmed input is a valid number
        if (isNaN(Number(trimmedNumber))) {
            return "Not Numerical";
        }

        // Check if the number length is between 5 and 18 characters
        if (trimmedNumber.length < 5 || trimmedNumber.length > 18) {
            return "Invalid Length, Must Be Between 5-18";
        }

        return true;
    } catch {
        return "Invalid Input";
    }
}
