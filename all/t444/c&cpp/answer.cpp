#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::string format_comment(const std::string& string, int max_length = 60) {
    // Split the string into lines
    std::istringstream iss(string);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(iss, line, '\n')) {
        lines.push_back(line);
    }

    // Initialize a vector to store the formatted lines
    std::vector<std::string> formatted_lines;

    // Iterate through the lines
    for (const auto& line : lines) {
        // Split the line into words
        std::istringstream word_stream(line);
        std::string word;
        std::string current_line;

        while (word_stream >> word) {
            // If the current line plus the next word would be too long,
            // append the current line to the list of formatted lines and start a new line
            if (!current_line.empty() && current_line.length() + word.length() + 1 > max_length) {
                formatted_lines.push_back(current_line);
                current_line.clear();
            }

            // If the current line is empty, add the word to the line
            // Otherwise, add a space and the word to the line
            if (current_line.empty()) {
                current_line = word;
            } else {
                current_line += " " + word;
            }
        }

        // Add the remaining line to the list of formatted lines
        if (!current_line.empty()) {
            formatted_lines.push_back(current_line);
        }
    }

    // Join the formatted lines with newline characters and prefix each line with "# "
    std::ostringstream oss;
    for (const auto& formatted_line : formatted_lines) {
        oss << "# " << formatted_line << "\n";
    }

    return oss.str();
}
