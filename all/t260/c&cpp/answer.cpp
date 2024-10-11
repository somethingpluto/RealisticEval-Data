#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <boost/algorithm/string.hpp>

struct Row {
    std::vector<std::string> cells;
};

bool has_two_or_more_empty_columns(const Row& row) {
    int count = 0;
    for (const auto& cell : row.cells) {
        if (cell.empty()) {
            count++;
            if (count >= 2) {
                return true;
            }
        } else {
            count = 0;
        }
    }
    return false;
}

void process_csv(const std::string& file_path, const std::string& output_path) {
    std::ifstream file(file_path);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << file_path << std::endl;
        return;
    }

    std::ofstream output_file(output_path);
    if (!output_file.is_open()) {
        std::cerr << "Error opening output file: " << output_path << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        Row row;
        boost::split(row.cells, line, boost::is_any_of(","));
        if (!has_two_or_more_empty_columns(row)) {
            std::cout << line << std::endl; // Output to console
            output_file << line << std::endl; // Write to output file
        }
    }

    file.close();
    output_file.close();
}