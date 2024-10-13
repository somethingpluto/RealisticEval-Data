#include <iostream>
#include <stdexcept>
#include <utility>

// Function to convert a floating-point number between 0 and 1 to a color from red to green in RGB format.
std::tuple<int, int, int> float_to_rgb(float value) {
    // Check if the value is within the valid range
    if (value < 0.0f || value > 1.0f) {
        throw std::invalid_argument("Value must be between 0 and 1 inclusive.");
    }

    // Calculate the red and green components
    int red = static_cast<int>((1.0f - value) * 255);
    int green = static_cast<int>(value * 255);

    // Blue component is always 0 for the red-to-green gradient
    int blue = 0;

    return std::make_tuple(red, green, blue);
}

int main() {
    try {
        float value = 0.5; // Example value
        auto rgb = float_to_rgb(value);
        std::cout << "RGB: (" << std::get<0>(rgb) << ", " << std::get<1>(rgb) << ", " << std::get<2>(rgb) << ")" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}