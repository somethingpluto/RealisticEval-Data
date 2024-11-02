#include <iostream>
#include <algorithm>
#include <tuple>
#include <cmath>

std::tuple<double, double, double> rgb_to_hsv(double r, double g, double b) {
    r /= 255.0;
    g /= 255.0;
    b /= 255.0;
    double max_rgb = std::max({r, g, b});
    double min_rgb = std::min({r, g, b});
    double delta = max_rgb - min_rgb;
    double h = 0;
    if (delta == 0) {
        h = 0; // No hue
    } else if (max_rgb == r) {
        h = fmod((g - b) / delta, 6);
    } else if (max_rgb == g) {
        h = ((b - r) / delta) + 2;
    } else {
        h = ((r - g) / delta) + 4;
    }
    h *= 60;  
    if (h < 0) {
        h += 360;
    }
    double s = 0;
    if (max_rgb == 0) {
        s = 0;
    } else {
        s = delta / max_rgb;
    }
    double v = max_rgb;
    return std::make_tuple(h, s * 100, v * 100);
}
