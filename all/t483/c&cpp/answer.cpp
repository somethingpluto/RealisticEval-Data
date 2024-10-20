#include <iostream>
#include <regex>
#include <string>

bool is_valid_email(const std::string& email) {
    /**
     * Verifies if the provided string is a valid email address.
     *
     * Parameters:
     * email (std::string): The email address to validate.
     *
     * Returns:
     * bool: True if the email address is valid, False otherwise.
     */
    // Regular expression pattern for validating an email address
    std::regex email_pattern("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

    return std::regex_match(email, email_pattern);
}