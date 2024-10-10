#include <iostream>
#include <string>

std::string convertFileSize(int sizeBytes)
{
    if (sizeBytes == 0)
        return "0B";
    
    std::string units[] = {"B", "KB", "MB", "GB", "TB"};
    int unitIndex = 0;

    while (sizeBytes >= 1024 && unitIndex + 1 < sizeof(units)/sizeof(std::string))
    {
        sizeBytes /= 1024;
        unitIndex++;
    }

    return std::to_string(sizeBytes) + units[unitIndex];
}