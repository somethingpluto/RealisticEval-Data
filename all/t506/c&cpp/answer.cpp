#include <iostream>
#include <string>
#include <sstream>
#include <vector>

// Function to convert a snake_case string to CamelCase.
std::string snake_to_camel(const std::string& snake_str) {
    std::istringstream iss(snake_str); // Use istringstream to split the string
    std::vector<std::string> words;
    std::string word;

    // Split the snake_case string into words
    while (std::getline(iss, word, '_')) {
        words.push_back(word);
    }

    // Capitalize the first letter of each word and join them
    std::string camel_case_str;
    for (const auto& w : words) {
        if (!w.empty()) {
            w[0] = toupper(w[0]); // Capitalize the first character
            camel_case_str += w;
        }
    }

    return camel_case_str;
}
