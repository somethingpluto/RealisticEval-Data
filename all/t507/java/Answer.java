package org.real.temp;

public class Answer {

    /**
     * Check if the provided password is strong.
     *
     * A strong password must satisfy the following criteria:
     * - At least one lowercase letter
     * - At least one uppercase letter
     * - At least one number
     * - At least 8 characters long
     *
     * @param password The password to check.
     * @return true if the password is strong, false otherwise.
     */
    public static boolean isStrongPassword(String password) {
        // Check password length
        if (password.length() < 8) {
            return false;
        }

        // Check for at least one lowercase letter
        if (!password.matches(".*[a-z].*")) {
            return false;
        }

        // Check for at least one uppercase letter
        if (!password.matches(".*[A-Z].*")) {
            return false;
        }

        // Check for at least one number
        if (!password.matches(".*\\d.*")) {
            return false;
        }

        // If all checks passed, return true
        return true;
    }

    public static void main(String[] args) {
        // Example usage
        String password = "StrongP@ssw0rd";
        System.out.println(isStrongPassword(password)); // Expected output: true
    }
}