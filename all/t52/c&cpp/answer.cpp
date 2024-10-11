#include <string>
#include <algorithm>

std::string rename_file_path(const std::string& path) {
    std::string result = path;
    std::replace(result.begin(), result.end(), ':', '_');
    return result;
}