#include <iostream>
#include <algorithm>
#include <cmath>

struct HSL {
    int h;
    int s;
    int l;
};

HSL rgbToHsl(int r, int g, int b) {
    // Convert RGB to the [0, 1] range.
    r /= 255.0;
    g /= 255.0;
    b /= 255.0;

    double max = std::max({r, g, b});
    double min = std::min({r, g, b});
    double h, s, l = (max + min) / 2;

    if (max == min) {
        h = s = 0; // achromatic
    } else {
        double d = max - min;
        s = (l > 0.5) ? d / (2 - max - min) : d / (max + min);

        if (max == r) {
            h = (g - b) / d + (g < b ? 6 : 0);
        } else if (max == g) {
            h = (b - r) / d + 2;
        } else {
            h = (r - g) / d + 4;
        }

        h /= 6;
    }

    // Convert hue to degrees
    h = std::round(h * 360);
    // Convert saturation and lightness to percentage
    s = std::round(s * 100);
    l = std::round(l * 100);

    return { static_cast<int>(h), static_cast<int>(s), static_cast<int>(l) };
}