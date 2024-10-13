#include <iostream>
#include <regex>
#include <string>

// Function to check if the string contains a phone number
bool contains_phone_number(const std::string& s) {
    // Regex pattern to identify phone numbers
    std::regex pattern(R"((\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4}))");
    
    // Use std::regex_search to find a match
    return std::regex_search(s, pattern);
}

int main() {
    // Test the function with some example strings
    std::string test_strings[] = {"+1-800-555-1234", "555-555-1234", "555 555 1234", "No phone number here"};
    
    for (const auto& s : test_strings) {
        std::cout << "'" << s << "' contains a phone number: " 
                  << (contains_phone_number(s) ? "True" : "False") << std::endl;
    }
    
    return 0;
}