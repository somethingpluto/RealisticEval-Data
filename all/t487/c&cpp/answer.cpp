#include <iostream>
#include <regex>
#include <string>

// Function to check if the given text contains an email address
bool contains_email(const std::string& text) {
    // Define a regex pattern for validating an email address
    std::regex email_pattern(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");

    // Search for the email pattern in the text
    return std::regex_search(text, email_pattern);
}
