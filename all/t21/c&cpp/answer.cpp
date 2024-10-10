#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector<std::string> compareFiles(const std::string& file1Path, const std::string& file2Path) {
    std::ifstream file1(file1Path);
    std::ifstream file2(file2Path);

    if (!file1.is_open() || !file2.is_open()) {
        throw std::runtime_error("Error opening file");
    }

    std::vector<std::string> diffs;
    std::string line1, line2;

    while (getline(file1, line1) && getline(file2, line2)) {
        if (line1 != line2) {
            diffs.push_back("- " + line1);
            diffs.push_back("+ " + line2);
        }
    }

    // Check for remaining lines in both files
    while (getline(file1, line1)) {
        diffs.push_back("- " + line1);
    }

    while (getline(file2, line2)) {
        diffs.push_back("+ " + line2);
    }

    return diffs;
}