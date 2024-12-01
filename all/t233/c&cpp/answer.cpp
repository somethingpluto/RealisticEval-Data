#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::string remove_comments(const std::string& input) {
    std::istringstream iss(input);
    std::vector<std::string> lines;
    std::string line;
    
    // Split the string into lines
    while (std::getline(iss, line)) {
        lines.push_back(line);
    }
    
    std::vector<std::string> cleanedLines;
    
    // Remove the comment part from each line
    for (const auto& l : lines) {
        size_t commentPos = l.find('#');
        if (commentPos != std::string::npos) {
            cleanedLines.push_back(l.substr(0, commentPos));
        } else {
            cleanedLines.push_back(l);
        }
    }
    
    std::ostringstream oss;
    
    // Join the lines back into a single string
    for (size_t i = 0; i < cleanedLines.size(); ++i) {
        if (i > 0) {
            oss << '\n';
        }
        oss << cleanedLines[i];
    }
    
    return oss.str();
}