#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>
#include <string>

// Function to remove triple backticks from strings
std::vector<std::string> removeTripleBackticks(const std::vector<std::string>& stringList) {
    std::vector<std::string> processedList;

    for (const auto& s : stringList) {
        std::string processedString = s;
        size_t pos;
        while ((pos = processedString.find("