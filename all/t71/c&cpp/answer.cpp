#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdexcept>

// Function to read numerical columns from a file starting from the line after the last line containing '/'
std::vector<std::vector<double>> read_columns(const std::string& file_name) {
    // Initialize a variable to track the last slash line index
    int last_slash_index = -1;
    std::vector<std::string> lines;

    // Read all lines from the file
    std::ifstream file(file_name);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file");
    }
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    file.close();

    // Find the index of the last line that contains the "/" character
    for (int i = 0; i < lines.size(); ++i) {
        if (lines[i].find('/') != std::string::npos) {
            last_slash_index = i;
        }
    }

    // If no "/" character was found, raise an error
    if (last_slash_index == -1) {
        throw std::runtime_error("File does not contain '/' character");
    }

    // Read the remaining lines in the file, starting from the line after the last "/"
    std::vector<std::string> data_lines;
    for (int i = last_slash_index + 1; i < lines.size(); ++i) {
        std::string trimmed_line = lines[i];
        trimmed_line.erase(0, trimmed_line.find_first_not_of(" \t\n\r\f\v")); // Trim leading spaces
        trimmed_line.erase(trimmed_line.find_last_not_of(" \t\n\r\f\v") + 1); // Trim trailing spaces
        if (!trimmed_line.empty() && !trimmed_line.starts_with('!')) {
            data_lines.push_back(trimmed_line);
        }
    }

    // If no valid lines remain, return an empty vector
    if (data_lines.empty()) {
        return {};
    }

    // Get the row and column count by counting the number of columns in the first line
    int col_count = std::count(data_lines[0].begin(), data_lines[0].end(), ' ') + 1;

    // Create an empty vector of vectors of the required size
    std::vector<std::vector<double>> arr(data_lines.size(), std::vector<double>(col_count));

    // Loop through the lines in the file
    for (size_t i = 0; i < data_lines.size(); ++i) {
        std::istringstream iss(data_lines[i]);
        double num;
        int j = 0;
        while (iss >> num) {
            arr[i][j++] = num;
            if (iss.peek() == ' ') {
                iss.ignore();
            }
        }
    }

    // Return the array
    return arr;
}

int main() {
    try {
        std::vector<std::vector<double>> result = read_columns("example.txt");
        for (const auto& row : result) {
            for (double val : row) {
                std::cout << val << " ";
            }
            std::cout << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}