#include <iostream>
#include <vector>
#include <string>
#include <sstream>

std::vector<std::vector<std::string>> parse_markdown_table(const std::string& md_table) {
    // Split the input string into lines
    std::istringstream stream(md_table);
    std::string line;
    std::vector<std::vector<std::string>> table_data;

    // Read each line from the input string
    while (std::getline(stream, line)) {
        // Trim leading and trailing whitespace and check for separator line
        std::string trimmed_line = line;
        trimmed_line.erase(0, trimmed_line.find_first_not_of(" \t")); // trim leading whitespace
        trimmed_line.erase(trimmed_line.find_last_not_of(" \t") + 1); // trim trailing whitespace

        // Ignore the separator line (which usually contains "---")
        if (trimmed_line.find("---") != std::string::npos) {
            continue;
        }

        // Strip leading and trailing pipes, then split by "|"
        if (trimmed_line.front() == '|') {
            trimmed_line.erase(0, 1);
        }
        if (trimmed_line.back() == '|') {
            trimmed_line.erase(trimmed_line.size() - 1);
        }

        std::vector<std::string> row;
        std::istringstream row_stream(trimmed_line);
        std::string cell;

        // Process each cell
        while (std::getline(row_stream, cell, '|')) {
            // Trim leading and trailing spaces from each cell
            cell.erase(0, cell.find_first_not_of(" \t")); // trim leading whitespace
            cell.erase(cell.find_last_not_of(" \t") + 1); // trim trailing whitespace

            // Add the processed cell to the row
            row.push_back(cell.empty() ? "" : cell); // Handle empty cells
        }

        // Add the row to the table data
        table_data.push_back(row);
    }

    return table_data;
}
