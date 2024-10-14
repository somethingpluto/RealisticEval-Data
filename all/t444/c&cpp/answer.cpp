#include <iostream>
#include <string>
#include <vector>

std::string formatComment(const std::string& input, int maxLength = 60) {
    std::string result;
    std::string currentLine;

    for (char ch : input) {
        if (currentLine.length() + 2 > maxLength) { // Add 2 for "# " prefix
            result += "# " + currentLine + "\n";
            currentLine.clear();
        }
        currentLine += ch;
    }

    if (!currentLine.empty()) {
        result += "# " + currentLine + "\n";
    }

    return result;
}
