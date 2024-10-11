#include <tuple>
#include <stdexcept>
#include <iostream>

std::tuple<int, int, int> floatToRGB(float value) {
    if (value < 0.0f || value > 1.0f) {
        throw std::out_of_range("Value must be between 0 and 1 inclusive.");
    }

    // Calculate the red and green components
    int red = static_cast<int>((1.0f - value) * 255);
    int green = static_cast<int>(value * 255);

    // Blue component is always 0 for the red-to-green gradient
    int blue = 0;

    return std::make_tuple(red, green, blue);
}