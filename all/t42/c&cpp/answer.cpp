#include <iostream>
#include <regex>
#include <string>

std::string replacePhoneNumbers(const std::string &text) {
    // Define a regex pattern to match phone numbers
    std::regex phonePattern(R"(\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b)");

    // Replace all matches in the text with [PHONE_NUM]
    std::string replacedText = std::regex_replace(text, phonePattern, "[PHONE_NUM]");

    return replacedText;
}

int main() {
    std::string text = "Contact me at +1-800-555-1234 or (123) 456 7890.";
    std::string result = replacePhoneNumbers(text);
    std::cout << result << std::endl;  // Output should be "Contact me at [PHONE_NUM] or [PHONE_NUM]."
    return 0;
}