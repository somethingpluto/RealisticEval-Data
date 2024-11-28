#include <iostream>
#include <regex>
#include <vector>
#include <string>

// Function to find and return a list of all placeholders in the format {{ placeholder }} from the input text.
std::vector<std::string> find_placeholders(const std::string& text) {
    // Regular expression pattern to match placeholders in the specified format
    std::regex pattern(R"(\{\{\s*([\w]+)\s*\}\})");
    
    // Use std::sregex_iterator to find all matches in the input text
    std::sregex_iterator matches_begin = std::sregex_iterator(text.begin(), text.end(), pattern);
    std::sregex_iterator matches_end = std::sregex_iterator();
    
    // Extract the matched placeholders and store them in a vector
    std::vector<std::string> placeholders;
    for (std::sregex_iterator i = matches_begin; i != matches_end; ++i) {
        std::smatch match = *i;
        placeholders.push_back(match[1].str());  // Extract the placeholder part
    }
    
    return placeholders;
}