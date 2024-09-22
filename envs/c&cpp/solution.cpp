#include <string>

std::string getLastPartOfFilepath(const std::string& filePath) {
    size_t pos = filePath.find_last_of("/\\");
    return (pos != std::string::npos) ? filePath.substr(pos + 1) : filePath;
}