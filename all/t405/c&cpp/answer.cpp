#include <iostream>
#include <vector>
#include <string>
#include <cctype> // For isupper() and islower()

// Function to find the index of the first character that satisfies the predicate
int find_index(const std::string& str, bool (*predicate)(int)) {
    for (size_t i = 0; i < str.length(); ++i) {
        if (predicate(str[i])) {
            return static_cast<int>(i);
        }
    }
    return -1; // Return -1 if no matching character is found
}

// Function to remove parts of the string based on the criteria
std::vector<std::string> remove_parts_of_string(const std::vector<std::string>& strings) {
    std::vector<std::string> results;
    for (const auto& string : strings) {
        std::string modifiedString = string;

        // Remove all characters before the first uppercase letter
        int upperIndex = find_index(modifiedString, ::isupper);
        if (upperIndex != -1) {
            modifiedString = modifiedString.substr(upperIndex);
        }

        // Remove all characters before the first lowercase letter
        int lowerIndex = find_index(modifiedString, ::islower);
        if (lowerIndex != -1) {
            modifiedString = modifiedString.substr(lowerIndex - 1);
        }

        results.push_back(modifiedString);
    }

    return results;
}