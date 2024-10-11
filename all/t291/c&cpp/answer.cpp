#include <iostream>
#include <fstream>
#include <string>

void prependToEachLine(const std::string& filePath, const std::string& prefix) {
    // Open the input file
    std::ifstream inFile(filePath);
    if (!inFile.is_open()) {
        std::cerr << "Error opening file: " << filePath << std::endl;
        return;
    }

    // Read the entire content of the file into a string
    std::string content((std::istreambuf_iterator<char>(inFile)), std::istreambuf_iterator<char>());
    inFile.close();

    // Prepend the prefix to each line
    size_t pos = 0;
    while ((pos = content.find('\n', pos)) != std::string::npos) {
        content.insert(pos, prefix);
        pos += prefix.length() + 1; // Move past the newline character
    }

    // Open the output file in write mode
    std::ofstream outFile(filePath);
    if (!outFile.is_open()) {
        std::cerr << "Error opening file for writing: " << filePath << std::endl;
        return;
    }

    // Write the modified content back to the file
    outFile << content;
    outFile.close();
}