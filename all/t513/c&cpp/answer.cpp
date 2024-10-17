#include <iostream>
#include <string>
#include <cctype>
#include <regex>

// Function to convert a string to lowercase
std::string to_lower(const std::string& str) {
    std::string lower_str;
    for (char c : str) {
        lower_str += std::tolower(c);
    }
    return lower_str;
}

bool is_phrase_in_string_ignore_case(const std::string& phrase, const std::string& string) {
    /**
     * Check if the given phrase exists in the target string, ignoring case and allowing for variations in whitespace.
     *
     * Args:
     *     phrase (std::string): The phrase to search for in the string.
     *     string (std::string): The target string in which to search for the phrase.
     *
     * Returns:
     *     bool: True if the phrase is found as a whole word in the string, False otherwise.
     */

    // Convert both phrase and string to lower case
    std::string lower_phrase = to_lower(phrase);
    std::string lower_string = to_lower(string);

    // Escape special characters in the phrase
    std::string escaped_phrase;
    for (char c : lower_phrase) {
        if (std::ispunct(c)) {
            escaped_phrase += '\\';
        }
        escaped_phrase += c;
    }

    // Replace spaces in the phrase with \s+ to allow for any whitespace variations
    std::replace(escaped_phrase.begin(), escaped_phrase.end(), ' ', '\\');
    std::replace(escaped_phrase.begin(), escaped_phrase.end(), '+', ' ');

    // Construct the regex pattern with word boundaries
    std::string pattern = "\\b" + escaped_phrase + "\\b";

    // Search for the pattern in the target string
    return std::regex_search(lower_string, std::regex(pattern));
}
