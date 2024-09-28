#include <iostream>
#include <string>

std::string simplify_windows_path(const std::string& path) {
    // Find the position of the drive letter and colon
    size_t pos = path.find(':');
    std::string simplified_drive;
    std::string path_without_drive;

    if (pos != std::string::npos) {
        // Replace the drive letter and colon, e.g., 'D:' with 'D_'
        simplified_drive = path.substr(0, pos) + "_";
        path_without_drive = path.substr(pos + 1);
    } else {
        path_without_drive = path;
    }

    // Replace backslashes with underscores
    for (auto& ch : path_without_drive) {
        if (ch == '\\') {
            ch = '_';
        }
    }

    // Remove any leading or trailing underscores
    if (!path_without_drive.empty() && path_without_drive.front() == '_') {
        path_without_drive.erase(0, 1);
    }
    if (!path_without_drive.empty() && path_without_drive.back() == '_') {
        path_without_drive.pop_back();
    }

    // Concatenate the simplified drive and the remaining path
    std::string final_path = simplified_drive + path_without_drive;

    return final_path;
}

int main() {
    std::string path = "D:\\Folder\\Subfolder\\File.txt";
    std::string simplified_path = simplify_windows_path(path);
    std::cout << "Simplified path: " << simplified_path << std::endl;

    return 0;
}