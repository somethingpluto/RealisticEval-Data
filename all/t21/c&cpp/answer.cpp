#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdexcept>

// Function to read the contents of a file and return it as a vector of strings (each line is a string)
std::vector<std::string> readFileLines(const std::string &filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        throw std::runtime_error("File not found: " + filePath);
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }
    file.close();
    return lines;
}

// Function to compare two files and return the differences in a format similar to "unified diff"
std::vector<std::string> compareFiles(const std::string &file1Path, const std::string &file2Path) {
    std::vector<std::string> lines1 = readFileLines(file1Path);
    std::vector<std::string> lines2 = readFileLines(file2Path);

    std::ostringstream diffStream;
    std::vector<std::string> diffLines;

    // Here a simple line-by-line comparison is made
    // This is a basic difference finder; for a full diff algorithm, you need a more sophisticated algorithm
    for (size_t i = 0; i < std::max(lines1.size(), lines2.size()); ++i) {
        if (i >= lines1.size()) {
            diffStream << "+ " << lines2[i] << "\n"; // Line only in file2
        } else if (i >= lines2.size()) {
            diffStream << "- " << lines1[i] << "\n"; // Line only in file1
        } else if (lines1[i] != lines2[i]) {
            diffStream << "- " << lines1[i] << "\n";
            diffStream << "+ " << lines2[i] << "\n";
        }
    }

    std::string diffLine;
    std::istringstream diffInputStream(diffStream.str());
    while (std::getline(diffInputStream, diffLine)) {
        std::cout << diffLine << std::endl; // Print each line
        diffLines.push_back(diffLine); // Store the output in a vector
    }

    return diffLines;
}

int main() {
    try {
        std::string file1 = "file1.txt";
        std::string file2 = "file2.txt";
        std::vector<std::string> differences = compareFiles(file1, file2);

        if (differences.empty()) {
            std::cout << "No differences found.\n";
        }
    } catch (const std::runtime_error &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}