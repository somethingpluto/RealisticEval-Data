#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <cctype>

std::unordered_map<std::string, std::vector<std::string>> classifyFilesByExtension(const std::vector<std::string>& fileNames) {
    std::unordered_map<std::string, std::vector<std::string>> classifiedFiles;

    for (const auto& file : fileNames) {
        // Find the last dot in the filename
        size_t dotPos = file.find_last_of('.');
        
        // If there is no dot, consider the entire filename as the name and no extension
        if (dotPos == std::string::npos) {
            classifiedFiles["none"].push_back(file);
        } else {
            // Extract the extension
            std::string ext = file.substr(dotPos + 1);

            // Convert the extension to lowercase
            std::transform(ext.begin(), ext.end(), ext.begin(),
                           [](unsigned char c){ return std::tolower(c); });

            // Add the file to the corresponding list
            classifiedFiles[ext].push_back(file);
        }
    }

    return classifiedFiles;
}