/**
 * Checks whether the provided username is valid.
 * A valid username is defined as a string that:
 * - Has a length between 5 and 16 characters (inclusive).
 * - Contains only alphanumeric characters (letters and digits) and spaces.
 *
 * @param {string} username - The username to validate.
 * @returns {boolean} - Returns true if the username is valid; otherwise, false.
 */
function isValidUsername(username) {
    // Check if the input is a string
    if (typeof username !== 'string') {
        return false; // Return false if the input is not a string
    }

    // Trim any leading or trailing whitespace from the username
    username = username.trim();

    // Check the length of the username
    const length = username.length;
    if (length < 5 || length > 16) {
        return false; // Return false if length is not within the valid range
    }

    // Check if the username contains only alphanumeric characters and spaces
    const isValid = /^[a-zA-Z0-9 ]+$/.test(username);
    
    return isValid; // Return true if valid, false otherwise
}
