#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::string format_str(const std::string& x) {
    // Convert x to string if it's not already a string (not necessary in C++).

    // Ensure there is a matching number of code block delimiters.
    // If the count of delimiters is odd, append an additional one to balance.
    size_t delimiter_count = 0;
    for (char c : x) {
        if (c == '`') {
            delimiter_count++;
        }
    }
    if (delimiter_count % 3 == 1) {
        x += "\n```";
    }

    // Format each line by prepending '> ' and join them with newlines.
    std::istringstream iss(x);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(iss, line)) {
        lines.push_back("> " + line);
    }

    // Join the formatted lines with newlines.
    std::ostringstream oss;
    for (size_t i = 0; i < lines.size(); ++i) {
        if (i > 0) {
            oss << "\n";
        }
        oss << lines[i];
    }

    // Return the final formatted string.
    return oss.str();
}
