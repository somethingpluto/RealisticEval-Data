#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <tuple>
#include <algorithm>

// Helper function to split string by delimiter
std::vector<std::string> split(const std::string &str, char delim) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(str);
    while (std::getline(tokenStream, token, delim)) {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to strip leading and trailing whitespace
std::string strip(const std::string &str) {
    const char* whitespace = " \t\n\r\f\v";
    std::string::size_type front = str.find_first_not_of(whitespace);
    if (front == std::string::npos)
        return ""; // String is all whitespace
    std::string::size_type back = str.find_last_not_of(whitespace);
    return str.substr(front, back - front + 1);
}

// Function to parse Markdown table
std::vector<std::vector<std::string>> parse_markdown_table(const std::string &md_table) {
    // Split the input string into lines and strip whitespace
    std::vector<std::string> lines;
    std::istringstream f(md_table);
    std::string line;
    while (std::getline(f, line)) {
        lines.push_back(strip(line));
    }

    // Filter out the separator line for the header (which usually contains "---")
    lines.erase(std::remove_if(lines.begin(), lines.end(), [](const std::string &str) {
        return str.find("---") != std::string::npos;
    }), lines.end());

    // Initialize the list to store each row as a tuple
    std::vector<std::vector<std::string>> table_data;

    // Process each line
    for (const auto &line : lines) {
        // Strip leading and trailing spaces and pipes, then split by "|"
        std::string stripped_line = strip(strip(line), '|');
        std::vector<std::string> row = split(stripped_line, '|');

        // Process each cell, strip spaces and handle empty cells
        std::vector<std::string> tuple_row;
        for (auto &cell : row) {
            std::string trimmed_cell = strip(cell);
            if (trimmed_cell.empty()) {
                tuple_row.push_back("");
            } else {
                tuple_row.push_back(trimmed_cell);
            }
        }
        // Add the tuple to the list
        table_data.push_back(tuple_row);
    }

    return table_data;
}

int main() {
    std::string md_table = R"(
| Header1 | Header2 | Header3 |
| ------- | ------- | ------- |
| Cell1   | Cell2   | Cell3   |
| Cell4   | Cell5   | Cell6   |
| Cell7   | Cell8   | Cell9   |
)";

    std::vector<std::vector<std::string>> result = parse_markdown_table(md_table);

    // Print the result
    for (const auto &row : result) {
        for (const auto &cell : row) {
            std::cout << cell << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}