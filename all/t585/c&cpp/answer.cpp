#include <iostream>
#include <regex>
#include <string>

/**
 * Detects whether the string is in CAMEL_CASE.
 *
 * @param input - The string to check.
 * @returns true if the string is in CAMEL_CASE, otherwise false.
 */
bool isCamelCase(const std::string& input) {
    // Regular expression to match CAMEL_CASE
    std::regex camelCaseRegex("^[a-z]+([A-Z][a-z]*)*$");
    return std::regex_match(input, camelCaseRegex);
}

int main() {
    std::string testString = "myVariableName";
    if (isCamelCase(testString)) {
        std::cout << testString << " is in CAMEL_CASE." << std::endl;
    } else {
        std::cout << testString << " is not in CAMEL_CASE." << std::endl;
    }
    return 0;
}