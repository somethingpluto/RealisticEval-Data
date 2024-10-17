#include <iostream>
#include <regex>
#include <string>

bool is_strong_password(const std::string& password) {
    /**
     * Check if the provided password is strong.
     *
     * A strong password must satisfy the following criteria:
     * - At least one lowercase letter
     * - At least one uppercase letter
     * - At least one number
     * - At least 8 characters long
     *
     * Parameters:
     * password (std::string): The password to check.
     *
     * Returns:
     * bool: True if the password is strong, False otherwise.
     */

    // Check password length
    if (password.length() < 8) {
        return false;
    }

    // Check for at least one lowercase letter
    if (!std::regex_search(password, std::regex("[a-z]"))) {
        return false;
    }

    // Check for at least one uppercase letter
    if (!std::regex_search(password, std::regex("[A-Z]"))) {
        return false;
    }

    // Check for at least one number
    if (!std::regex_search(password, std::regex("\\d"))) {
        return false;
    }

    // If all checks passed, return true
    return true;
}
