#include <string>
#include <filesystem>
#include <iostream>

// Function to rename file path by replacing colons with underscores
std::string renameFilePath(const std::string& path) {
    // Use std::filesystem to split the path into directory and filename
    std::filesystem::path fsPath(path);
    std::string directory = fsPath.parent_path().string();
    std::string filename = fsPath.filename().string();

    // Replace colons in the filename with underscores
    for (auto& ch : filename) {
        if (ch == ':') {
            ch = '_';
        }
    }

    // Reconstruct the full path with the sanitized filename
    std::filesystem::path newPath = std::filesystem::path(directory) / filename;

    return newPath.string();
}

int main() {
    std::string originalPath = "C:/some:path/with:colons/file.txt"; // Example path
    std::string modifiedPath = renameFilePath(originalPath);

    std::cout << "Original Path: " << originalPath << std::endl;
    std::cout << "Modified Path: " << modifiedPath << std::endl;

    return 0;
}