#include <iostream>
#include <cmath>
#include <string>
#include <optional>

std::string formatBytes(
    long long bytes,
    std::optional<int> decimals = std::nullopt,
    std::optional<std::string> sizeType = std::nullopt) {
    
    // Set default values
    int decimalPlaces = decimals.value_or(0);
    std::string unitType = sizeType.value_or("normal");
    
    const std::string accurateUnits[] = {"Bytes", "KiB", "MiB", "GiB", "TiB"};
    const std::string normalUnits[] = {"Bytes", "KB", "MB", "GB", "TB"};
    
    const std::string* sizeUnits = (unitType == "accurate") ? accurateUnits : normalUnits;
    
    if (bytes == 0) return "0 Byte";
    
    int unitIndex = static_cast<int>(std::floor(std::log(bytes) / std::log(1024)));
    double formattedSize = static_cast<double>(bytes) / std::pow(1024, unitIndex);
    
    char buffer[50];
    snprintf(buffer, sizeof(buffer), "%.*f %s", decimalPlaces, formattedSize, sizeUnits[unitIndex].c_str());
    
    return std::string(buffer);
}