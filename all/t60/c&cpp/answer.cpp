#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <filesystem>

namespace fs = std::filesystem;

std::vector<std::string> findCommonColumns(const std::string& directory) {
    if (!fs::exists(directory) || !fs::is_directory(directory)) {
        throw std::invalid_argument("Invalid directory");
    }

    std::set<std::string> commonColumns;
    bool firstFile = true;

    for (const auto& entry : fs::directory_iterator(directory)) {
        if (entry.is_regular_file() && entry.path().extension() == ".csv") {
            std::ifstream file(entry.path());
            if (!file.is_open()) {
                throw std::runtime_error("Failed to open file: " + entry.path().string());
            }

            std::string line;
            if (std::getline(file, line)) { // Read the header line
                std::istringstream iss(line);
                std::string column;
                while (std::getline(iss, column, ',')) {
                    if (firstFile) {
                        commonColumns.insert(column);
                    } else {
                        commonColumns.erase(column);
                    }
                }
            }
            file.close();
        }
    }

    if (firstFile) {
        throw std::runtime_error("No CSV files found in the directory");
    }

    return std::vector<std::string>(commonColumns.begin(), commonColumns.end());
}