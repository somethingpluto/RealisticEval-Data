#include <iostream>
#include <string>

class Colors {
public:
    // Text in red color
    static std::string red(const std::string& text) {
        return "\033[91m" + text + "\033[0m";
    }

    // Text in green color
    static std::string green(const std::string& text) {
        return "\033[92m" + text + "\033[0m";
    }

    // Text in blue color
    static std::string blue(const std::string& text) {
        return "\033[94m" + text + "\033[0m";
    }

    // Text in yellow color
    static std::string yellow(const std::string& text) {
        return "\033[93m" + text + "\033[0m";
    }

    // Text in magenta color
    static std::string magenta(const std::string& text) {
        return "\033[95m" + text + "\033[0m";
    }

    // Text in cyan color
    static std::string cyan(const std::string& text) {
        return "\033[96m" + text + "\033[0m";
    }
};