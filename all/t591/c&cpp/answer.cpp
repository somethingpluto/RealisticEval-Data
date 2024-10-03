#include <iostream>

// Struct to hold RGB values
struct RGB {
    int r;  // Red component
    int g;  // Green component
    int b;  // Blue component
};

// Enum class for colors
enum class Color {
    RED,
    GREEN,
    BLUE,
    YELLOW,
    MAGENTA,
    CYAN,
    WHITE,
    BLACK,
    ORANGE,
    PURPLE,
    PINK,
    BROWN
};

// Function to get the RGB values for each color
RGB getColorRGB(Color color) {
    switch (color) {
        case Color::RED:
            return {255, 0, 0};
        case Color::GREEN:
            return {0, 255, 0};
        case Color::BLUE:
            return {0, 0, 255};
        case Color::YELLOW:
            return {255, 255, 0};
        case Color::MAGENTA:
            return {255, 0, 255};
        case Color::CYAN:
            return {0, 255, 255};
        case Color::WHITE:
            return {255, 255, 255};
        case Color::BLACK:
            return {0, 0, 0};
        case Color::ORANGE:
            return {255, 165, 0};
        case Color::PURPLE:
            return {128, 0, 128};
        case Color::PINK:
            return {255, 192, 203};
        case Color::BROWN:
            return {165, 42, 42};
        default:
            return {0, 0, 0}; // Default to black for unknown colors
    }
}