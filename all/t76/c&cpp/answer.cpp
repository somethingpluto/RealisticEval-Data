#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

std::string remove_common_indentation(const std::string& multiline_text) {
    /**
     * Removes the common leading indentation from each line in a given multi-line string,
     * preserving the relative indentation of the text.
     *
     * Args:
     *     multiline_text (const std::string&): The input string containing multiple lines.
     *
     * Returns:
     *     std::string: The sanitized string with common leading indentation removed.
     */

    // Split the input string into lines
    std::vector<std::string> lines;
    std::string current_line;
    std::istringstream iss(multiline_text);
    while (std::getline(iss, current_line, '\n')) {
        lines.push_back(current_line);
    }

    // Filter out lines that are empty or only whitespace
    std::vector<std::string> non_empty_lines;
    for (const auto& line : lines) {
        if (!line.empty() && line.find_first_not_of(" \t") != std::string::npos) {
            non_empty_lines.push_back(line);
        }
    }

    // Determine the minimum indentation of non-empty lines
    size_t min_indent = std::string::npos;
    for (const auto& line : non_empty_lines) {
        size_t first_non_space = line.find_first_not_of(" \t");
        if (first_non_space != std::string::npos) {
            min_indent = std::min(min_indent, first_non_space);
        }
    }

    // If there's no indentation or all lines are empty, return the original string
    if (min_indent == std::string::npos) {
        return multiline_text;
    }

    // Remove the common leading indentation from each line
    std::vector<std::string> sanitized_lines;
    for (const auto& line : lines) {
        if (line.length() > min_indent) {
            sanitized_lines.push_back(line.substr(min_indent));
        } else {
            sanitized_lines.push_back("");
        }
    }

    // Join the sanitized lines back into a single string
    std::string result;
    for (size_t i = 0; i < sanitized_lines.size(); ++i) {
        result += sanitized_lines[i];
        if (i < sanitized_lines.size() - 1) {
            result += "\n";
        }
    }

    return result;
}
