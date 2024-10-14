#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

// Function to split a string by a delimiter
std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to extract paragraphs and lines from the given text
std::map<std::string, std::vector<std::string>> extract_paragraphs_and_lines(const std::string &text) {
    // Split the text into paragraphs
    std::vector<std::string> paragraphs = split(text, '\n');

    // Split each paragraph into lines
    std::vector<std::string> all_lines;
    for (const auto &paragraph : paragraphs) {
        std::vector<std::string> lines = split(paragraph, '\n');
        all_lines.insert(all_lines.end(), lines.begin(), lines.end());
    }

    // Filter out empty paragraphs and lines
    std::vector<std::string> filtered_paragraphs;
    std::vector<std::string> filtered_lines;

    for (const auto &paragraph : paragraphs) {
        if (!paragraph.empty()) {
            filtered_paragraphs.push_back(paragraph);
        }
    }

    for (auto &line : all_lines) {
        if (!line.empty()) {
            filtered_lines.push_back(line);
        }
    }

    // Return the extracted paragraphs and lines in a map
    return {
        {"paragraphs", filtered_paragraphs},
        {"lines", filtered_lines}
    };
}