#include <iostream>
#include <string>
#include <regex>

bool contains_phone_number(const std::string& s) {
    // Regex pattern to identify phone numbers
    std::regex pattern(R"((\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4}))");

    // Use std::regex_search to find a match
    return std::regex_search(s, pattern);
}