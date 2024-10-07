#include <iostream>
#include <string>

std::string extractStringFromBraces(const std::string& input) {
    // Find the position of the first opening brace
    size_t openingBracePos = input.find('{');

    // Check if an opening brace was found
    if (openingBracePos == std::string::npos) {
        return "No opening brace found.";
    }

    // Find the position of the first closing brace after the opening brace
    size_t closingBracePos = input.find('}', openingBracePos);

    // Check if a closing brace was found
    if (closingBracePos == std::string::npos) {
        return "No closing brace found.";
    }

    // Extract the string between the braces (including the braces)
    return input.substr(openingBracePos, closingBracePos - openingBracePos + 1);
}