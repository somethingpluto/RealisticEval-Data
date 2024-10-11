#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>

std::pair<int, int> getMinSeqNumAndDistance(const std::string& filePath, const std::string& word1, const std::string& word2) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filePath << std::endl;
        return {0, std::numeric_limits<int>::max()};
    }

    std::string line;
    int lineNumber = 0;
    int minDistance = std::numeric_limits<int>::max();
    int minLineIndex = -1;

    while (getline(file, line)) {
        ++lineNumber;
        std::istringstream iss(line);
        std::string word;
        int lastIndex1 = -1, lastIndex2 = -1;

        while (iss >> word) {
            if (word == word1) {
                lastIndex1 = lineNumber;
            } else if (word == word2) {
                lastIndex2 = lineNumber;
            }
        }

        if (lastIndex1 != -1 && lastIndex2 != -1) {
            int distance = abs(lastIndex1 - lastIndex2);
            if (distance < minDistance) {
                minDistance = distance;
                minLineIndex = lineNumber;
            }
        }
    }

    if (minLineIndex == -1) {
        return {0, std::numeric_limits<int>::max()};
    }

    return {minLineIndex, minDistance};
}