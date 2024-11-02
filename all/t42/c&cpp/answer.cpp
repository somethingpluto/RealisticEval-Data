#include <iostream>
#include <regex>
#include <string>

std::string replace_phone_numbers(const std::string& text) {
    std::regex phone_pattern(R"(\b(?:\+\d{1,2}\s?)?(\d{1,4}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b)");
    std::string replaced_text = std::regex_replace(text, phone_pattern, "[PHONE_NUM]");
    return replaced_text;
}