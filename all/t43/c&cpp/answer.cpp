#include <iostream>
#include <algorithm> // For std::max and std::min
#include <tuple>

// Function to convert RGB values to HSV values
std::tuple<double, double, double> rgb_to_hsv(double r, double g, double b) {
    // Normalize the RGB values by dividing by 255
    r /= 255.0;
    g /= 255.0;
    b /= 255.0;

    // Find the minimum and maximum values among R, G, and B
    double max_rgb = std::max({r, g, b});
    double min_rgb = std::min({r, g, b});
    double delta = max_rgb - min_rgb;

    // Calculate H (Hue)
    double h = 0;
    if (delta == 0) {
        h = 0;
    } else if (max_rgb == r) {
        h = ((g - b) / delta) % 6;
    } else if (max_rgb == g) {
        h = ((b - r) / delta) + 2;
    } else {
        h = ((r - g) / delta) + 4;
    }

    h *= 60;  // Convert to degrees on the color circle

    // Calculate S (Saturation)
    double s = 0;
    if (max_rgb == 0) {
        s = 0;
    } else {
        s = delta / max_rgb;
    }

    // V (Value) is equal to max_rgb
    double v = max_rgb;

    return std::make_tuple(h, s * 100, v * 100);
}

// Example usage
int main() {
    double r = 255, g = 0, b = 0;
    auto [h, s, v] = rgb_to_hsv(r, g, b);
    std::cout << "HSV: (" << h << ", " << s << ", " << v << ")" << std::endl;
    return 0;
}