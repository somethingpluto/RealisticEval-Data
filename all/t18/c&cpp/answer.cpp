#include <iostream>
#include <stdexcept>
#include <utility>

// Function to convert a floating-point number between 0 and 1 to a color from red to green in RGB format.
std::tuple<int, int, int> float_to_rgb(float value) {
    if (value < 0.0f || value > 1.0f) {
        throw std::invalid_argument("Value must be between 0 and 1 inclusive.");
    }
    int red = static_cast<int>((1.0f - value) * 255);
    int green = static_cast<int>(value * 255);
    int blue = 0;
    return std::make_tuple(red, green, blue);
}
