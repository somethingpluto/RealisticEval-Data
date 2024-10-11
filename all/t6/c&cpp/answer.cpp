#include <iostream>
#include <string>

std::string simplify_windows_path(const std::string &path) {
    std::string simplified_path;
    for (char c : path) {
        if (c == '\\') {
            simplified_path += '_';
        } else {
            simplified_path += c;
        }
    }
    return simplified_path;
}