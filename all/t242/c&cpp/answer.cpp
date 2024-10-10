#include <vector>
#include <map>
#include <string>

std::map<std::string, std::vector<std::string>> classifyFilesByExtension(const std::vector<std::string>& fileNames) {
    std::map<std::string, std::vector<std::string>> classifiedFiles;

    for (const auto& fileName : fileNames) {
        size_t dotPos = fileName.find_last_of('.');
        if (dotPos != std::string::npos) {
            std::string extension = fileName.substr(dotPos + 1);
            classifiedFiles[extension].push_back(fileName);
        }
    }

    return classifiedFiles;
}