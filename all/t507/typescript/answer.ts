import { test } from 'node:re';

function isStrongPassword(password: string): boolean {
    /**
     * Check if the provided password is strong.
     *
     * A strong password must satisfy the following criteria:
     * - At least one lowercase letter
     * - At least one uppercase letter
     * - At least one number
     * - At least 8 characters long
     *
     * @param password - The password to check.
     * @returns true if the password is strong, false otherwise.
     */
    // Check password length
    if (password.length < 8) {
        return false;
    }

    // Check for at least one lowercase letter
    if (!test(/[a-z]/, password)) {
        return false;
    }

    // Check for at least one uppercase letter
    if (!test(/[A-Z]/, password)) {
        return false;
    }

    // Check for at least one number
    if (!test(/\d/, password)) {
        return false;
    }

    // If all checks passed, return true
    return true;
}