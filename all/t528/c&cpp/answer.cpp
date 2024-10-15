#include <iostream>
#include <vector>
#include <string>
#include <filesystem>

namespace fs = std::filesystem;

/**
 * Recursively searches for Markdown files in the specified directory.
 *
 * @param dir - The directory path to search in.
 * @returns A vector of paths to Markdown files.
 */
std::vector<std::string> findMarkdownFiles(const fs::path& dir) {
    std::vector<std::string> markdownFiles;

    for (const auto& entry : fs::directory_iterator(dir)) {
        if (entry.is_directory()) {
            auto subFiles = findMarkdownFiles(entry.path());
            markdownFiles.insert(markdownFiles.end(), subFiles.begin(), subFiles.end());
        } else if (entry.path().extension() == ".md") {
            markdownFiles.push_back(entry.path().string());
        }
    }

    return markdownFiles;
}

int main() {
    std::string directory = "your_directory_path_here"; // Replace with your directory
    std::vector<std::string> markdownFiles = findMarkdownFiles(directory);

    for (const auto& file : markdownFiles) {
        std::cout << file << std::endl;
    }

    return 0;
}