function isValidEmail(email) {
    /**
     * Verifies if the provided string is a valid email address.
     *
     * @param {string} email - The email address to validate.
     * @returns {boolean} - True if the email address is valid, False otherwise.
     */
    // Regular expression pattern for validating an email address
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    return emailPattern.test(email);
}