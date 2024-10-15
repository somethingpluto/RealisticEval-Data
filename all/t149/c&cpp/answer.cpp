#include <iostream>
#include <cmath>

struct RGB {
    int r;
    int g;
    int b;
};

RGB hslToRgb(double hue, double saturation, double lightness) {
    double r, g, b;

    if (saturation == 0) {
        // Achromatic case (saturation = 0), r, g, and b are the same.
        r = g = b = lightness; // all equal to lightness
    } else {
        // Chromatic case (saturation != 0)
        auto hueToRgb = [](double p, double q, double t) -> double {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1.0 / 6.0) return p + (q - p) * 6 * t;
            if (t < 1.0 / 2.0) return q;
            if (t < 2.0 / 3.0) return p + (q - p) * (2.0 / 3.0 - t) * 6;
            return p;
        };

        double q = lightness < 0.5 ? lightness * (1 + saturation) : lightness + saturation - lightness * saturation;
        double p = 2 * lightness - q;
        r = hueToRgb(p, q, hue / 360 + 1.0 / 3.0);
        g = hueToRgb(p, q, hue / 360);
        b = hueToRgb(p, q, hue / 360 - 1.0 / 3.0);
    }

    // Convert r, g, b from [0, 1] range to [0, 255] range
    return {static_cast<int>(std::round(r * 255)), 
            static_cast<int>(std::round(g * 255)), 
            static_cast<int>(std::round(b * 255))};
}