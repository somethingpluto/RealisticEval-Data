#include <iostream>
#include <regex>
#include <string>

// Function to convert an input string with multiple separators to a comma-separated string
std::string convert_to_comma_separated(const std::string& input_string) {
    // The pattern includes *, ;, /, -, :
    std::regex pattern("[\\*;/\\-\\:]");  // Correctly escaped hyphen and included colon in the character class
    std::string comma_separated_string = std::regex_replace(input_string, pattern, ",");

    return comma_separated_string;
}

// Main function for testing
int main() {
    std::string input = "one*two/three-four;five:six";
    std::string output = convert_to_comma_separated(input);

    std::cout << "Input: " << input << std::endl;
    std::cout << "Output: " << output << std::endl;

    return 0;
}