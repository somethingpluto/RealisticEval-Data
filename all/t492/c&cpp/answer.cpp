#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

void save_content_to_file(const std::string& content, const std::string& path) {
    /**
     * Saves the provided content to a specified file after cleaning up
     * redundant whitespace.
     *
     * Args:
     *     content (std::string): The text content to be saved to the file.
     *     path (std::string): The file path where the content will be saved.
     *
     * Returns:
     *     None
     */

    // Remove redundant whitespace from the content.
    // Split the content into lines, strip leading/trailing whitespace,
    // and filter out empty lines.
    std::istringstream iss(content);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(iss, line)) {
        line = std::string(line.begin(), line.end() - 1); // Remove trailing newline
        if (!line.empty()) {
            // Strip leading and trailing whitespace
            auto start = line.find_first_not_of(" \t\n\r\f\v");
            auto end = line.find_last_not_of(" \t\n\r\f\v");
            if (start != std::string::npos && end != std::string::npos) {
                line = line.substr(start, end - start + 1);
                lines.push_back(line);
            }
        }
    }

    // Join the lines back together with newlines.
    std::string cleanedContent;
    for (const auto& l : lines) {
        if (!cleanedContent.empty()) {
            cleanedContent += "\n";
        }
        cleanedContent += l;
    }

    // Replace multiple spaces with a single space.
    std::istringstream iss2(cleanedContent);
    std::string finalContent;
    std::string word;
    while (iss2 >> word) {
        if (!finalContent.empty()) {
            finalContent += " ";
        }
        finalContent += word;
    }

    // Write the cleaned content to the specified file.
    std::ofstream file(path);
    if (file.is_open()) {
        file << finalContent;
        file.close();
    } else {
        std::cerr << "Unable to open file: " << path << std::endl;
    }
}
