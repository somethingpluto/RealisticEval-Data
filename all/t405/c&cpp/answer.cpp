#include <string>
#include <cctype>

std::string remove_parts_of_string(const std::string &str) {
    int start = -1;
    for (int i = 0; i < str.size(); ++i) {
        if (isupper(str[i])) {
            start = i;
            break;
        }
    }

    if (start == -1)
        return "";

    int end = -1;
    for (int i = start + 1; i < str.size(); ++i) {
        if (islower(str[i])) {
            end = i;
            break;
        }
    }

    if (end == -1)
        return "";

    return str.substr(start);
}