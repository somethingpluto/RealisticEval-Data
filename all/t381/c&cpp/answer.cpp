#include <iostream>
#include <string>
#include <stdexcept>

std::pair<std::string, std::string> extract_email_details(const std::string& email) {
    /**
     * Extracts the username and mailbox suffix from an email address.
     *
     * @param email: The email address to extract details from.
     * @return: A pair (username, domain) where:
     *      username is the part before '@'
     *      domain is the part after '@'
     *
     * Example:
     *      extract_email_details("xxx@gmail.com") returns ("xxx", "gmail.com")
     */
    
    // Check if '@' is in the email
    size_t at_pos = email.find('@');
    if (at_pos == std::string::npos) {
        throw std::invalid_argument("Invalid email address. Email must contain an '@' character.");
    }

    // Extract the username and domain
    std::string username = email.substr(0, at_pos);
    std::string domain = email.substr(at_pos + 1);

    return {username, domain};
}