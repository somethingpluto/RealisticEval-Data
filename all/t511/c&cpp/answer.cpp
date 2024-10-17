#include <iostream>
#include <string>
#include <stdexcept>

// Function to convert a hexadecimal color code to an ANSI escape code
std::string hex_to_ansi(const std::string& hex_color) {
    // Check if the input is a valid hex color
    if (hex_color.length() != 7 || hex_color[0] != '#') {
        throw std::invalid_argument("Invalid hex color format. Use '#RRGGBB'.");
    }

    // Extract the red, green, and blue components from the hex string
    int r = std::stoi(hex_color.substr(1, 2), nullptr, 16);
    int g = std::stoi(hex_color.substr(3, 2), nullptr, 16);
    int b = std::stoi(hex_color.substr(5, 2), nullptr, 16);

    // Create the ANSI escape code
    std::string ansi_code = "\x1b[38;2;" + std::to_string(r) + ";" + std::to_string(g) + ";" + std::to_string(b) + "m";

    return ansi_code;
}
