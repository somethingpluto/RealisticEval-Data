class Colors {
public:
    // Function to return text in red color
    static std::string red(const std::string& text);

    // Function to return text in green color
    static std::string green(const std::string& text);

    // Function to return text in blue color
    static std::string blue(const std::string& text);

    // Function to return text in yellow color
    static std::string yellow(const std::string& text);

    // Function to return text in magenta color
    static std::string magenta(const std::string& text);

    // Function to return text in cyan color
    static std::string cyan(const std::string& text);
};

// Implementation of each function (you can add actual implementation here)
std::string Colors::red(const std::string& text) {
    // Placeholder implementation
    return "\033[31m" + text + "\033[0m";
}

std::string Colors::green(const std::string& text) {
    // Placeholder implementation
    return "\033[32m" + text + "\033[0m";
}

std::string Colors::blue(const std::string& text) {
    // Placeholder implementation
    return "\033[34m" + text + "\033[0m";
}

std::string Colors::yellow(const std::string& text) {
    // Placeholder implementation
    return "\033[33m" + text + "\033[0m";
}

std::string Colors::magenta(const std::string& text) {
    // Placeholder implementation
    return "\033[35m" + text + "\033[0m";
}

std::string Colors::cyan(const std::string& text) {
    // Placeholder implementation
    return "\033[36m" + text + "\033[0m";
}