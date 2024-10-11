#include <iostream>
#include <string>

class Colors {
public:
    static std::string red(const std::string& text) {
        return "\033[31m" + text + "\033[0m";
    }

    static std::string green(const std::string& text) {
        return "\033[32m" + text + "\033[0m";
    }

    static std::string blue(const std::string& text) {
        return "\033[34m" + text + "\033[0m";
    }

    static std::string yellow(const std::string& text) {
        return "\033[33m" + text + "\033[0m";
    }

    static std::string magenta(const std::string& text) {
        return "\033[35m" + text + "\033[0m";
    }

    static std::string cyan(const std::string& text) {
        return "\033[36m" + text + "\033[0m";
    }
};