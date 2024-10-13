#include <iostream>
#include <regex>
#include <string>

// Function to replace phone numbers in a given text
std::string replace_phone_numbers(const std::string& text) {
    // Define a regex pattern to match phone numbers
    // This pattern matches optional country codes, spaces, dashes, and brackets commonly found in phone numbers
    std::regex phone_pattern(R"(\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b)");

    // Replace all matches in the text with [PHONE_NUM]
    std::string replaced_text = std::regex_replace(text, phone_pattern, "[PHONE_NUM]");

    return replaced_text;
}

int main() {
    // Example usage
    std::string sample_text = "Call me at +1 555-1234 or (555) 555-1234.";
    std::string result = replace_phone_numbers(sample_text);
    std::cout << result << std::endl;

    return 0;
}