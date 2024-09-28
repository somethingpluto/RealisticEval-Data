#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Function to process a list of strings, removing all occurrences of three consecutive backticks from each string
std::vector<std::string> removeTripleBackticks(const std::vector<std::string>& stringList) {
    std::vector<std::string> processedList;

    for (const auto& s : stringList) {
        std::string processedString = s;
        // Replace occurrences of '