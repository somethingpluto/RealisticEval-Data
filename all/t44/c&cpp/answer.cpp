#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

// Helper function to split a string into lines
std::vector<std::string> splitLines(const std::string &str) {
    std::vector<std::string> lines;
    std::istringstream stream(str);
    std::string line;
    while (std::getline(stream, line)) {
        lines.push_back(line);
    }
    return lines;
}

// Function to display two strings side by side
std::string stringSideBySide(const std::string &string1, const std::string &string2, int columnWidth = 20) {
    std::vector<std::string> lines1 = splitLines(string1);
    std::vector<std::string> lines2 = splitLines(string2);

    size_t maxLength = std::max(lines1.size(), lines2.size());
    lines1.resize(maxLength, "");  // Pad lines1 with empty strings if necessary
    lines2.resize(maxLength, "");  // Pad lines2 with empty strings if necessary

    std::ostringstream resultStream;
    
    for (size_t i = 0; i < maxLength; ++i) {
        resultStream << std::left << std::setw(columnWidth) << lines1[i] 
                     << " | " 
                     << std::left << std::setw(columnWidth) << lines2[i] 
                     << '\n';
    }

    return resultStream.str();
}

int main() {
    std::string string1 = "This is the first string.\nIt has multiple lines.";
    std::string string2 = "Second string example.\nWith some lines too.";

    std::string result = stringSideBySide(string1, string2);
    std::cout << result;
    
    return 0;
}