#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <regex>

std::string removePunctuation(const std::string& str) {
    // Define a regex pattern that matches common punctuation characters.
    std::regex punctuationRegex(R"([\u2000-\u206F\u2E00-\u2E7F!"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~])");
    
    // Remove punctuation using regex
    std::string cleanedStr = std::regex_replace(str, punctuationRegex, "");
    
    // Convert to lowercase
    std::transform(cleanedStr.begin(), cleanedStr.end(), cleanedStr.begin(), ::tolower);
    
    // Trim whitespace from both ends
    cleanedStr.erase(cleanedStr.begin(), std::find_if(cleanedStr.begin(), cleanedStr.end(), [](unsigned char ch) {
        return !std::isspace(ch);
    }));
    cleanedStr.erase(std::find_if(cleanedStr.rbegin(), cleanedStr.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), cleanedStr.end());
    
    return cleanedStr;
}

int main() {
    std::string input = "Hello, World! This is a test: 123.";
    std::string output = removePunctuation(input);
    std::cout << "Cleaned String: '" << output << "'" << std::endl;
    return 0;
}