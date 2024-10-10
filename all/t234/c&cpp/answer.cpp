#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

bool hasMatchingRow(std::ifstream &fileHandler, const std::vector<std::string> &rowCandidate) {
    std::string line;
    while (std::getline(fileHandler, line)) {
        std::istringstream iss(line);
        std::vector<std::string> row;
        std::string cell;

        // Read each cell from the current line
        while (std::getline(iss, cell, ',')) {
            row.push_back(cell);
        }

        // Check if the first three cells match the candidate row
        if (row.size() >= 3 &&
            row[0] == rowCandidate[0] &&
            row[1] == rowCandidate[1] &&
            row[2] == rowCandidate[2]) {
            return true;
        }
    }

    return false;
}

void appendOrSkipRow(std::fstream &fileHandler, const std::vector<std::string> &rowCandidate) {
    // Move to the beginning of the file to check for duplicates
    fileHandler.seekg(0);

    // If no matching row exists, append the new row
    if (!hasMatchingRow(fileHandler, rowCandidate)) {
        fileHandler.seekp(0, std::ios_base::end); // Go to the end of the file
        for (size_t i = 0; i < rowCandidate.size(); ++i) {
            fileHandler << rowCandidate[i];
            if (i != rowCandidate.size() - 1) {
                fileHandler << ",";
            }
        }
        fileHandler << "\n";
    }
}