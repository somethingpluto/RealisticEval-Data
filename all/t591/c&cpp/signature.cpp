#include <iostream>
#include <string>
#include <unordered_map>

/**
* Please write a class that contains RGB representations of, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, WHITE, BLACK, ORANGE, PURPLE, PINK, BROWN, which can be obtained directly by the function
/
class Color {
public:
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
    std::tuple<int, int, int> getColor(ColorName colorName) {}

    // Function to get the color name as a string
    std::string getColorName(ColorName colorName) {}

private:
    // A map to store the RGB values of the colors
    std::unordered_map<ColorName, std::tuple<int, int, int>> colors;

    // Function to initialize the colors
    void initializeColors() {}
};
