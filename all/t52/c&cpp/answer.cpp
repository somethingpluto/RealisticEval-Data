#include <iostream>
#include <filesystem>
#include <string>

// Use the filesystem namespace for convenience
namespace fs = std::filesystem;

std::string rename_file_path(const std::string& path) {
    /**
     * Renames a Windows file path by replacing colons in the filename with underscores.
     *
     * Parameters:
     *     path (std::string): The original file path.
     *
     * Returns:
     *     std::string: The modified file path with colons in the filename replaced by underscores.
     */
    
    // Split the path into directory and filename
    fs::path p = path;
    std::string directory = p.parent_path().string();
    std::string filename = p.filename().string();

    // Replace colons in the filename with underscores
    std::string sanitized_filename;
    for (char c : filename) {
        if (c == ':') {
            sanitized_filename += '_';
        } else {
            sanitized_filename += c;
        }
    }

    // Reconstruct the full path with the sanitized filename
    std::string new_path = fs::path(directory) / sanitized_filename;

    return new_path;
}