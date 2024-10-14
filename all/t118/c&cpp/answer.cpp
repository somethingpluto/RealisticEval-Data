#include <cmath>
#include <iostream>
#include <tuple>

std::tuple<int, int, int> hslToRgb(double h, double s, double l) {
    // Convert saturation and lightness to the range of [0, 1]
    s /= 100;
    l /= 100;

    double c = (1 - std::abs(2 * l - 1)) * s; // Chroma
    double x = c * (1 - std::abs(fmod(h / 60.0, 2) - 1));
    double m = l - c / 2;
    double r = 0, g = 0, b = 0;

    if (h >= 0 && h < 60) {
        r = c; g = x; b = 0;
    } else if (h >= 60 && h < 120) {
        r = x; g = c; b = 0;
    } else if (h >= 120 && h < 180) {
        r = 0; g = c; b = x;
    } else if (h >= 180 && h < 240) {
        r = 0; g = x; b = c;
    } else if (h >= 240 && h < 300) {
        r = x; g = 0; b = c;
    } else if (h >= 300 && h < 360) {
        r = c; g = 0; b = x;
    }

    // Convert the RGB components to 0 - 255 range
    r = std::round((r + m) * 255);
    g = std::round((g + m) * 255);
    b = std::round((b + m) * 255);

    return std::make_tuple(static_cast<int>(r), static_cast<int>(g), static_cast<int>(b));
}