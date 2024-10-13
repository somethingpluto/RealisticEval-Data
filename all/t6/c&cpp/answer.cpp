#include <iostream>
#include <string>
#include <algorithm>

// Function to split the drive from the path
std::pair<std::string, std::string> splitdrive(const std::string& path) {
    size_t pos = path.find(':');
    if (pos == std::string::npos) {
        return {"", path};
    }
    return {path.substr(0, pos + 1), path.substr(pos + 1)};
}

// Function to simplify the Windows path
std::string simplifyWindowsPath(const std::string& path) {
    // Split the drive letter and the rest of the path
    auto [drive, pathWithoutDrive] = splitdrive(path);
    
    // Simplify the drive letter by replacing ':' with '_'
    std::string simplifiedDrive = drive;
    simplifiedDrive.erase(std::remove(simplifiedDrive.begin(), simplifiedDrive.end(), ':'), simplifiedDrive.end());
    simplifiedDrive += '_';

    // Replace backslashes with underscores and strip any trailing backslash
    std::string simplifiedPath = pathWithoutDrive;
    std::replace(simplifiedPath.begin(), simplifiedPath.end(), '\\', '_');
    simplifiedPath.erase(std::find_if(simplifiedPath.rbegin(), simplifiedPath.rend(), [](char ch) { return ch != '_'; }).base(), simplifiedPath.end());

    // Concatenate the simplified drive and the remaining path
    std::string finalPath = simplifiedDrive + simplifiedPath;

    return finalPath;
}