#include <iostream>
#include <string>
#include <unordered_map>
#include <climits>

std::string find_min_window_substring(const std::string& source, const std::string& target) {
    if (source.empty() || target.empty()) {
        return "";
    }

    // Count the frequency of characters in the target string
    std::unordered_map<char, int> required_chars;
    for (char c : target) {
        ++required_chars[c];
    }

    // Counter to track characters in the current window of the source string
    std::unordered_map<char, int> window_chars;

    int left = 0;  // Left boundary of the window
    int min_length = INT_MAX;  // Initialize the minimum length as infinity
    std::string min_window = "";  // Initialize the minimum window string

    // Iterate over the source string with the right boundary of the window
    for (int right = 0; right < source.length(); ++right) {
        char char_right = source[right];
        if (required_chars.find(char_right) != required_chars.end()) {
            ++window_chars[char_right];
        }

        // Check if the current window contains all characters of the target string
        while (all_characters_match(required_chars, window_chars)) {
            int window_size = right - left + 1;
            if (window_size < min_length) {
                min_length = window_size;
                min_window = source.substr(left, window_size);
            }

            char char_left = source[left];
            if (required_chars.find(char_left) != required_chars.end()) {
                --window_chars[char_left];
            }
            ++left;
        }
    }

    return min_window;
}

bool all_characters_match(const std::unordered_map<char, int>& required_chars, const std::unordered_map<char, int>& window_chars) {
    for (const auto& pair : required_chars) {
        if (window_chars[pair.first] < pair.second) {
            return false;
        }
    }
    return true;
}