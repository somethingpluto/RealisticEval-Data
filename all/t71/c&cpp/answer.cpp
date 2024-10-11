#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

// Function to split string based on delimiter
std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

std::vector<std::vector<double>> readColumns(const std::string &fileName) {
    std::ifstream file(fileName);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file");
    }

    std::vector<std::vector<double>> data;
    bool foundSlash = false;

    std::string line;
    while (getline(file, line)) {
        if (line.find('/') != std::string::npos) {
            foundSlash = true;
            continue; // Skip lines until after the last line with '/'
        }

        if (!foundSlash) continue; // Ignore lines before the slash

        std::vector<std::string> tokens = split(line, ' ');
        std::vector<double> row;

        for (const auto &token : tokens) {
            try {
                double value = std::stod(token);
                row.push_back(value);
            } catch (...) {
                // Handle non-numeric values if necessary
                std::cerr << "Non-numeric value encountered in line: " << line << std::endl;
            }
        }

        data.push_back(row);
    }

    if (!foundSlash) {
        throw std::runtime_error("File does not contain any '/' character");
    }

    return data;
}
