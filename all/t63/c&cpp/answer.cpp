#include <iostream>
#include <fstream>
#include <vector>

void dataframeToMarkdown(std::vector<std::pair<std::string, std::vector<std::string>>> data, const std::string& mdPath)
{
    // Open file in write mode
    std::ofstream mdFile(mdPath);

    if (!mdFile.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    // Write the header row
    mdFile << "|";
    for (const auto& column : data[0].second) {
        mdFile << " " << column << " |";
    }
    mdFile << "\n";

    // Write the separator row
    mdFile << "|";
    for (size_t i = 0; i < data[0].second.size(); ++i) {
        mdFile << " --- |";
    }
    mdFile << "\n";

    // Write the data rows
    for (const auto& row : data) {
        mdFile << "|";
        for (const auto& cell : row.second) {
            mdFile << " " << cell << " |";
        }
        mdFile << "\n";
    }

    // Close file
    mdFile.close();
}
