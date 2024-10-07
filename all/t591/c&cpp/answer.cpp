#include <iostream>
#include <string>
#include <unordered_map>

class Color {
public:
    // Enum to represent the color names
    enum ColorName {
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

    // Constructor
    Color() {
        initializeColors();
    }

    // Function to get the RGB value of a color by its name
    std::tuple<int, int, int> getColor(ColorName colorName) {
        return colors[colorName];
    }

    // Function to get the color name as a string
    std::string getColorName(ColorName colorName) {
        switch (colorName) {
            case RED: return "Red";
            case GREEN: return "Green";
            case BLUE: return "Blue";
            case YELLOW: return "Yellow";
            case MAGENTA: return "Magenta";
            case CYAN: return "Cyan";
            case WHITE: return "White";
            case BLACK: return "Black";
            case ORANGE: return "Orange";
            case PURPLE: return "Purple";
            case PINK: return "Pink";
            case BROWN: return "Brown";
            default: return "Unknown Color";
        }
    }

private:
    // A map to store the RGB values of the colors
    std::unordered_map<ColorName, std::tuple<int, int, int>> colors;

    // Function to initialize the colors
    void initializeColors() {
        colors[RED] = std::make_tuple(255, 0, 0);
        colors[GREEN] = std::make_tuple(0, 255, 0);
        colors[BLUE] = std::make_tuple(0, 0, 255);
        colors[YELLOW] = std::make_tuple(255, 255, 0);
        colors[MAGENTA] = std::make_tuple(255, 0, 255);
        colors[CYAN] = std::make_tuple(0, 255, 255);
        colors[WHITE] = std::make_tuple(255, 255, 255);
        colors[BLACK] = std::make_tuple(0, 0, 0);
        colors[ORANGE] = std::make_tuple(255, 165, 0);
        colors[PURPLE] = std::make_tuple(128, 0, 128);
        colors[PINK] = std::make_tuple(255, 192, 203);
        colors[BROWN] = std::make_tuple(165, 42, 42);
    }
};
