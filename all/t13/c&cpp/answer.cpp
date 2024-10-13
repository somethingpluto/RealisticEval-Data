#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <sstream>
#include <algorithm>

// Function to parse a Markdown formatted table into a vector of tuples
std::vector<std::tuple<std::string, std::string, std::string>> parse_markdown_table(const std::string& md_table) {
    // Split the input string into lines and strip whitespace
    std::istringstream iss(md_table);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(iss, line)) {
        // Trim leading and trailing whitespace
        auto start = line.find_first_not_of(" \n\r\t");
        auto end = line.find_last_not_of(" \n\r\t");
        if (start == std::string::npos || end == std::string::npos) continue;
        line = line.substr(start, end - start + 1);

        // Filter out the separator line for the header (which usually contains "---")
        if (line.find("---") == std::string::npos) {
            lines.push_back(line);
        }
    }

    // Initialize the vector to store each row as a tuple
    std::vector<std::tuple<std::string, std::string, std::string>> table_data;

    // Process each line
    for (const auto& line : lines) {
        // Strip leading and trailing spaces and pipes, then split by "|"
        std::istringstream row_stream(line);
        std::vector<std::string> row;
        std::string cell;
        while (std::getline(row_stream, cell, '|')) {
            // Trim leading and trailing spaces
            auto start = cell.find_first_not_of(" \n\r\t");
            auto end = cell.find_last_not_of(" \n\r\t");
            if (start == std::string::npos || end == std::string::npos) continue;
            cell = cell.substr(start, end - start + 1);
            row.push_back(cell);
        }

        // Create a tuple and add it to the vector
        if (row.size() >= 3) {
            table_data.emplace_back(row[0], row[1], row[2]);
        }
    }

    return table_data;
}

// Helper function to trim whitespace from both ends of a string
std::string trim(const std::string& str) {
    auto start = str.find_first_not_of(" \n\r\t");
    auto end = str.find_last_not_of(" \n\r\t");
    return (start == std::string::npos) ? "" : str.substr(start, end - start + 1);
}

int main() {
    std::string md_table = R"(
| Column1 | Column2 | Column3 |
| --- | --- | --- |
| Value1 | Value2 | Value3 |
| Value4 | Value5 | Value6 |
)";

    auto result = parse_markdown_table(md_table);

    // Print the result
    for (const auto& row : result) {
        std::cout << "(" << std::get<0>(row) << ", " << std::get<1>(row) << ", " << std::get<2>(row) << ")" << std::endl;
    }

    return 0;
}