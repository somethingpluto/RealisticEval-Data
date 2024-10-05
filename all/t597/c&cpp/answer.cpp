#include <iostream>
#include <cmath>
#include <tuple>

std::tuple<int, int, int> hueToRGB(float hue) {
    // Ensure the hue value is within the range [0, 360)
    hue = fmod(hue, 360.0f);
    if (hue < 0) {
        hue += 360.0f;
    }

    float r, g, b;

    // Calculate RGB values based on hue
    int sector = static_cast<int>(hue / 60);
    float fractional = (hue / 60) - sector;

    switch (sector) {
        case 0:
            r = 1.0f; g = fractional; b = 0.0f; // Red to Yellow
            break;
        case 1:
            r = 1.0f - fractional; g = 1.0f; b = 0.0f; // Yellow to Green
            break;
        case 2:
            r = 0.0f; g = 1.0f; b = fractional; // Green to Cyan
            break;
        case 3:
            r = 0.0f; g = 1.0f - fractional; b = 1.0f; // Cyan to Blue
            break;
        case 4:
            r = fractional; g = 0.0f; b = 1.0f; // Blue to Magenta
            break;
        case 5:
        default:
            r = 1.0f; g = 0.0f; b = 1.0f - fractional; // Magenta to Red
            break;
    }

    // Convert to 0-255 range
    int red = static_cast<int>(r * 255);
    int green = static_cast<int>(g * 255);
    int blue = static_cast<int>(b * 255);

    return std::make_tuple(red, green, blue);
}