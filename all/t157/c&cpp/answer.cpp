#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>

std::string bytesToSize(long long bytes) {
    const std::string sizes[] = {"Bytes", "KB", "MB", "GB", "TB"};
    
    if (bytes == 0) return "0 Byte";

    int i = static_cast<int>(std::floor(std::log(bytes) / std::log(1024)));
    double size = bytes / std::pow(1024, i);

    std::ostringstream out;
    out << std::fixed << std::setprecision(2) << size << " " << sizes[i];
    return out.str();
}