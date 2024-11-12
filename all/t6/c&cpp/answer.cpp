#include <iostream>
#include <string>
#include <algorithm>

std::string simplify_windows_path(const std::string& path) {
    // Check if the path is a valid Windows path with a drive letter
    std::string simplified_path = path;
    
    // Find the drive letter and remove it (if present)
    size_t colon_pos = simplified_path.find(':');
    std::string simplified_drive = "";

    if (colon_pos != std::string::npos) {
        simplified_drive = simplified_path.substr(0, colon_pos) + "_";  // Add the underscore
        simplified_path = simplified_path.substr(colon_pos + 1);  // Remove the drive part
    }

    // Replace backslashes with underscores
    std::replace(simplified_path.begin(), simplified_path.end(), '\\', '_');

    // Strip trailing underscores
    if (!simplified_path.empty() && simplified_path.back() == '_') {
        simplified_path.pop_back();
    }

    // Concatenate the simplified drive and path
    return simplified_drive + simplified_path;
}