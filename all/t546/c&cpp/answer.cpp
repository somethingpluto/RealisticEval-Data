#include <iostream>
#include <vector>
#include <string>
#include <sstream>

// Function to read TSV from standard input and pad rows
std::vector<std::vector<std::string>> read_tsv_from_stdin() {
    std::vector<std::vector<std::string>> data;
    std::string line;

    // Read lines from standard input
    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        std::vector<std::string> row;
        std::string value;

        // Split the line by tabs
        while (std::getline(iss, value, '\t')) {
            row.push_back(value);
        }

        data.push_back(row);
    }

    // Find the maximum number of columns in the input data
    size_t max_columns = 0;
    if (!data.empty()) {
        for (const auto& row : data) {
            max_columns = std::max(max_columns, row.size());
        }
    }

    // Pad all rows to ensure they have the same length
    std::vector<std::vector<std::string>> padded_data;
    for (auto& row : data) {
        row.resize(max_columns, "");
        padded_data.push_back(row);
    }

    return padded_data;
}

int main() {
    // Example usage
    auto padded_data = read_tsv_from_stdin();

    // Print the padded data
    for (const auto& row : padded_data) {
        for (const auto& value : row) {
            std::cout << value << "\t";
        }
        std::cout << std::endl;
    }

    return 0;
}