#include <iostream>
#include <filesystem>
#include <vector>
#include <set>
#include <fstream>
#include <sstream>
#include <unordered_map>

// Function to read a CSV file and return its column names
std::vector<std::string> readCSVColumns(const std::string& filepath) {
    std::ifstream file(filepath);
    std::string line;
    std::getline(file, line); // Read the first line which contains headers
    std::istringstream ss(line);
    std::string column;
    std::vector<std::string> columns;

    while (std::getline(ss, column, ',')) {
        columns.push_back(column);
    }

    return columns;
}

std::set<std::string> findCommonColumns(const std::string& directory) {
    std::vector<std::set<std::string>> columnSets;
    
    for (const auto& entry : std::filesystem::directory_iterator(directory)) {
        if (entry.path().extension() == ".csv") {
            std::vector<std::string> columns = readCSVColumns(entry.path().string());
            columnSets.emplace_back(columns.begin(), columns.end());
        }
    }

    if (!columnSets.empty()) {
        std::set<std::string> commonColumns = columnSets[0];
        for (size_t i = 1; i < columnSets.size(); ++i) {
            std::set<std::string> tempSet;
            std::set_intersection(commonColumns.begin(), commonColumns.end(),
                                  columnSets[i].begin(), columnSets[i].end(),
                                  std::inserter(tempSet, tempSet.begin()));
            commonColumns = std::move(tempSet);
        }
        return commonColumns;
    } else {
        return {};
    }
}

int main() {
    std::string directory = "path/to/your/directory";
    std::set<std::string> commonColumns = findCommonColumns(directory);

    for (const auto& column : commonColumns) {
        std::cout << column << std::endl;
    }

    return 0;
}