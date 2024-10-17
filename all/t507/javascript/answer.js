function isStrongPassword(password) {
    /**
     * Check if the provided password is strong.
     *
     * A strong password must satisfy the following criteria:
     * - At least one lowercase letter
     * - At least one uppercase letter
     * - At least one number
     * - At least 8 characters long
     *
     * @param {string} password - The password to check.
     * @returns {boolean} - True if the password is strong, False otherwise.
     */

    // Check password length
    if (password.length < 8) {
        return false;
    }

    // Check for at least one lowercase letter
    if (!/[a-z]/.test(password)) {
        return false;
    }

    // Check for at least one uppercase letter
    if (!/[A-Z]/.test(password)) {
        return false;
    }

    // Check for at least one number
    if (!/\d/.test(password)) {
        return false;
    }

    // If all checks passed, return true
    return true;
}