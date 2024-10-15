#include <iostream>
#include <regex>
#include <string>

bool isValidPassword(const std::string& password) {
    // Regular expression patterns for the required criteria
    std::regex hasNumber("[0-9]");                          // At least one number
    std::regex hasLowercase("[a-z]");                       // At least one lowercase letter
    std::regex hasUppercase("[A-Z]");                       // At least one uppercase letter
    std::regex hasPunctuation("[!@#$%^&*(),.?\":{}|<>]");   // At least one punctuation mark
    std::regex hasMinimumLength(".{8,}");                   // At least 8 characters

    // Check each condition
    bool isValid = std::regex_search(password, hasNumber) &&
                   std::regex_search(password, hasLowercase) &&
                   std::regex_search(password, hasUppercase) &&
                   std::regex_search(password, hasPunctuation) &&
                   std::regex_match(password, hasMinimumLength);

    return isValid;
}