#include <iostream>
#include <string>
#include <unordered_map>
#include <climits>

std::string min_window(const std::string& s, const std::string& t) {
    // If the length of s is less than t, return an empty string
    if (s.length() < t.length()) {
        return "";
    }

    // Count characters in t
    std::unordered_map<char, int> substring_counter;
    for (char c : t) {
        substring_counter[c]++;
    }

    // Counter for the current window
    std::unordered_map<char, int> counter;

    // Initialize pointers and variables for the minimum window
    int l = 0, r = 0;
    int min_length = INT_MAX;
    std::string min_string = "";

    // Iterate over s using the right pointer
    for (r = 0; r < s.length(); ++r) {
        char char_r = s[r];
        // If the character is in the substring_counter, update the current counter
        if (substring_counter.find(char_r) != substring_counter.end()) {
            counter[char_r]++;
        }

        // Check if the current window contains all characters in t
        while (counter.size() == substring_counter.size() &&
               std::all_of(substring_counter.begin(), substring_counter.end(),
                           [&counter](const std::pair<char, int>& p) { return counter[p.first] >= p.second; })) {

            // Update the minimum window if a smaller one is found
            if (r - l + 1 < min_length) {
                min_length = r - l + 1;
                min_string = s.substr(l, r - l + 1);
            }

            // Move the left pointer to try to shrink the window
            char char_l = s[l];
            if (substring_counter.find(char_l) != substring_counter.end()) {
                counter[char_l]--;
                if (counter[char_l] == 0) {
                    counter.erase(char_l);
                }
            }
            l++;
        }
    }

    // Return the minimum window found or an empty string if none exists
    return min_string;
}