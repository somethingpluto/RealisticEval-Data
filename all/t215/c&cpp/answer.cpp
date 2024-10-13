#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>

// Function to replace words in a file based on a dictionary map
std::string replaceWordsInFile(const std::string& filePath, const std::unordered_map<std::string, std::string>& replacementDict) {
    try {
        // Read the content of the file
        std::ifstream file(filePath);
        if (!file.is_open()) {
            throw std::runtime_error("The file was not found.");
        }

        std::string text((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        file.close();

        // Replace words according to the replacement dictionary
        for (const auto& pair : replacementDict) {
            size_t startPos = 0;
            while ((startPos = text.find(pair.first, startPos)) != std::string::npos) {
                text.replace(startPos, pair.first.length(), pair.second);
                startPos += pair.second.length();
            }
        }

        return text;

    } catch (const std::exception& e) {
        return "Error: " + std::string(e.what());
    }
}

int main() {
    // Example usage
    std::unordered_map<std::string, std::string> replacementDict = {
        {"old_word", "new_word"},
        {"another_old", "another_new"}
    };

    std::string filePath = "example.txt";
    std::string modifiedText = replaceWordsInFile(filePath, replacementDict);

    std::cout << modifiedText << std::endl;

    return 0;
}