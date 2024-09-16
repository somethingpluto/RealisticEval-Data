/**
 * Checks whether the username is a string of length 5 to 16 that contains only alphanumeric Spaces
 *
 * @param {string} username - The input string to validate as a username.
 * @returns {string|boolean} - Returns "Invalid Length, Must Be Between 5-16" if the input length
 *                             is not within the required range, "Name Can Only Contain Letters, Numbers, and White Space"
 *                             if the input contains invalid characters, true if the input is valid,
 *                             or "Invalid Input" in case of unexpected errors.
 */
function isValidUserName(username) {
    try {
        const trimmedName = username.trim();

        // Check if the trimmed input length is between 5 and 16 characters
        if (trimmedName.length < 5 || trimmedName.length > 16) {
            return "Invalid Length, Must Be Between 5-16";
        }

        // Regular expression to validate that the name contains only letters, numbers, and white space
        const validNameRegex = /^[a-zA-Z0-9\s]+$/;

        // Check if the name matches the allowed pattern
        if (!validNameRegex.test(trimmedName)) {
            return "Name Can Only Contain Letters, Numbers, and White Space";
        }

        return true;
    } catch {
        return "Invalid Input";
    }
}
