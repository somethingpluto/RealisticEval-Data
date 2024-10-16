#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::string fixIndentation(const std::string& code) {
    std::istringstream stream(code);
    std::string line;
    std::ostringstream fixedCode;
    int currentIndentLevel = 0;
    const int spacesPerIndent = 4;

    while (std::getline(stream, line)) {
        std::string trimmedLine = line;
        
        // Trim leading whitespace
        size_t start = trimmedLine.find_first_not_of(" \t");
        if (start != std::string::npos) {
            trimmedLine = trimmedLine.substr(start);
        } else {
            trimmedLine.clear();  // Line is empty or whitespace only
        }

        if (trimmedLine.empty()) {
            fixedCode << "\n";
            continue;
        }

        // Adjust current indentation level
        if (trimmedLine.rfind("elif", 0) == 0 || trimmedLine.rfind("else", 0) == 0 ||
            trimmedLine.rfind("except", 0) == 0 || trimmedLine.rfind("finally", 0) == 0) {
            currentIndentLevel -= 1;
        } else if (trimmedLine.rfind("return", 0) == 0 || trimmedLine.rfind("break", 0) == 0 ||
                   trimmedLine.rfind("continue", 0) == 0 || trimmedLine.rfind("pass", 0) == 0) {
            currentIndentLevel -= 1;
        }

        // Add appropriate indentation
        fixedCode << std::string(currentIndentLevel * spacesPerIndent, ' ') << trimmedLine << "\n";

        // Increase indent level after lines ending with a colon
        if (trimmedLine.back() == ':') {
            currentIndentLevel += 1;
        } else if (trimmedLine.rfind("return", 0) == 0 || trimmedLine.rfind("break", 0) == 0 ||
                   trimmedLine.rfind("continue", 0) == 0 || trimmedLine.rfind("pass", 0) == 0) {
            currentIndentLevel -= 1;
        }
    }

    return fixedCode.str();
}

int main() {
    std::string code = "def my_function():\n    if condition:\n        return True\n    else:\n        return False\n";
    std::string fixedCode = fixIndentation(code);
    std::cout << "Fixed Code:\n" << fixedCode;

    return 0;
}
