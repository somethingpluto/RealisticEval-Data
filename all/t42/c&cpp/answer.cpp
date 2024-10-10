#include <iostream>
#include <regex>
#include <string>

std::string replace_phone_numbers(const std::string& text) {
    // Define the regex pattern for phone numbers
    std::regex phone_pattern(R"((\d{3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}))");
    
    // Replace phone numbers with "[PHONE_NUM]"
    std::string result = std::regex_replace(text, phone_pattern, "[PHONE_NUM]");
    
    return result;
}