#include <iostream>
#include <vector>
#include <string>

std::string convert_file_size(long long size_bytes) {
    // Define the size units
    const std::vector<std::string> units = {"B", "KB", "MB", "GB", "TB"};

    // Handle the case when size is 0 bytes
    if (size_bytes == 0) {
        return "0B";
    }

    // Calculate the appropriate unit
    int index = 0;
    while (size_bytes >= 1024 && index < units.size() - 1) {
        size_bytes /= 1024;
        index++;
    }

    // Return the formatted size with the appropriate unit
    return std::to_string(static_cast<long>(size_bytes)) + units[index];
}