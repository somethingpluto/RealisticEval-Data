function containsEmail(text) {
    /**
     * Check if the given text contains an email address.
     *
     * @param {string} text - The string to search for an email address.
     * @returns {boolean} - True if an email address is found, False otherwise.
     */

    // Define a regex pattern for validating an email address
    const emailPattern = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;

    // Search for the email pattern in the text
    return emailPattern.test(text);
}