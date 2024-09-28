#include <algorithm> // For std::max and std::min
#include <tuple>     // For std::tuple

std::tuple<double, double, double> rgbToHsv(int r, int g, int b) {
    // Normalize the RGB values by dividing by 255
    double r_norm = r / 255.0;
    double g_norm = g / 255.0;
    double b_norm = b / 255.0;

    // Find the minimum and maximum values among R, G, and B
    double max_rgb = std::max({r_norm, g_norm, b_norm});
    double min_rgb = std::min({r_norm, g_norm, b_norm});
    double delta = max_rgb - min_rgb;

    // Calculate H (Hue)
    double h;
    if (delta == 0) {
        h = 0;
    } else if (max_rgb == r_norm) {
        h = ((g_norm - b_norm) / delta);
        if (h < 0) h += 6; // Ensure it stays non-negative
    } else if (max_rgb == g_norm) {
        h = ((b_norm - r_norm) / delta) + 2;
    } else {
        h = ((r_norm - g_norm) / delta) + 4;
    }
    h *= 60; // Convert to degrees on the color circle

    // Calculate S (Saturation)
    double s = (max_rgb == 0) ? 0 : (delta / max_rgb);

    // V (Value) is equal to max_rgb
    double v = max_rgb;

    return std::make_tuple(h, s, v);
}