#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <set>

// Function to filter content with context using C++
std::string filter_content_with_context(
    const std::string& content,
    const std::vector<std::string>& keywords,
    int lines_before = 1,
    int lines_after = 1
) {
    /**
     * Filters website content to include lines containing any of the specified keywords as whole words,
     * along with a specified number of lines before and after for context. This version uses regular expressions
     * to ensure exact, whole word matching and respects case sensitivity.
     *
     * Parameters:
     * - content (const std::string&): The full text content of the website.
     * - keywords (const std::vector<std::string>&): A list of strings to search for within the content.
     * - lines_before (int): Number of lines to include before a matching line.
     * - lines_after (int): Number of lines to include after a matching line.
     *
     * Returns:
     * std::string: A string containing the filtered content with additional context.
     */

    // Split the content into individual lines
    std::istringstream iss(content);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(iss, line)) {
        lines.push_back(line);
    }

    std::set<int> matched_lines;  // Use a set to avoid duplicate lines

    // Iterate over each line to find matches
    for (size_t i = 0; i < lines.size(); ++i) {
        for (const auto& keyword : keywords) {
            // Use a regular expression to find whole word matches with exact case
            std::regex word_regex("\\b" + std::regex_replace(keyword, std::regex("\\\\|\\^|\\$|\\.|\\||\\?|\\*|\\+|\\(|\\)|\\[|\\]|\\{|\\}|\\-"), "\\$&") + "\\b");
            if (std::regex_search(lines[i], word_regex)) {
                // Determine the range of lines to include for context
                int start = std::max(static_cast<int>(i - lines_before), 0);
                int end = std::min(static_cast<int>(i + lines_after + 1), static_cast<int>(lines.size()));
                for (int j = start; j < end; ++j) {
                    matched_lines.insert(j);  // Add the context lines to the set
                }
            }
        }
    }

    // Extract the matched lines and their context, sorted by their original order
    std::vector<std::string> filtered_lines;
    for (int i : matched_lines) {
        filtered_lines.push_back(lines[i]);
    }

    // Join the filtered lines back into a single string
    std::string filtered_content;
    for (const auto& filtered_line : filtered_lines) {
        if (!filtered_content.empty()) {
            filtered_content += "\n";
        }
        filtered_content += filtered_line;
    }

    return filtered_content;
}
