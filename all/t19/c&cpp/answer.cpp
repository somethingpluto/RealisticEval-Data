#include <iostream>
#include <string>
#include <regex>

bool contains_phone_number(const std::string& s) {
    // Regex pattern to identify phone numbers
    std::regex pattern(R"((\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4}))");

    // Use std::regex_search to find a match
    return std::regex_search(s, pattern);
}

int main() {
    std::string s1 = "This is a test string with a number +1-800-555-1234.";
    std::string s2 = "This string does not have a phone number.";

    if (contains_phone_number(s1)) {
        std::cout << "String 1 contains a phone number." << std::endl;
    } else {
        std::cout << "String 1 does not contain a phone number." << std::endl;
    }

    if (contains_phone_number(s2)) {
        std::cout << "String 2 contains a phone number." << std::endl;
    } else {
        std::cout << "String 2 does not contain a phone number." << std::endl;
    }

    return 0;
}