#include <iostream>
#include <algorithm>

std::tuple<int, int, int> rgbToHsv(int r, int g, int b) {
    // Normalize RGB values to [0, 1]
    double maxVal = std::max({r / 255.0, g / 255.0, b / 255.0});
    double minVal = std::min({r / 255.0, g / 255.0, b / 255.0});
    double delta = maxVal - minVal;

    int h, s;
    if (delta == 0) {
        h = 0; // Undefined hue
        s = 0;
    } else {
        s = static_cast<int>(delta * 100);

        if (maxVal == r / 255.0)
            h = static_cast<int>((60 * fmod((g / 255.0 - b / 255.0) / delta, 6)));
        else if (maxVal == g / 255.0)
            h = static_cast<int>((60 * ((b / 255.0 - r / 255.0) / delta + 2)));
        else
            h = static_cast<int>((60 * ((r / 255.0 - g / 255.0) / delta + 4)));

        if (h < 0)
            h += 360;
    }

    int v = static_cast<int>(maxVal * 100);

    return {h, s, v};
}