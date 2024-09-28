#include <string>

std::string process_markdown(const std::string& s) {
    // Count occurrences of '*'
    int count = 0;
    for (char c : s) {
        if (c == '*') {
            count++;
        }
    }

    if (count <= 2) {
        return s;
    }

    // Find the first and last occurrence of '*'
    size_t first_star_index = s.find('*');
    size_t last_star_index = s.rfind('*');

    // Create a new string with '*' removed between first and last occurrence
    std::string result = s.substr(0, first_star_index + 1);
    for (size_t i = first_star_index + 1; i < last_star_index; ++i) {
        if (s[i] != '*') {
            result += s[i];
        }
    }
    result += s.substr(last_star_index);

    return result;
}