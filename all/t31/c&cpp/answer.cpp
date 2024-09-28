#include <vector>
#include <tuple>

double calculate_red_proportion(const std::vector<std::tuple<int, int, int>>& pixels) {
    if (pixels.empty()) {
        return 0.0;
    }

    int total_red = 0;
    int total_intensity = 0;

    for (const auto& pixel : pixels) {
        int r, g, b;
        std::tie(r, g, b) = pixel;

        total_red += r;
        total_intensity += (r + g + b);
    }

    // Avoid division by zero
    if (total_intensity == 0) {
        return 0.0;
    }

    double red_proportion = static_cast<double>(total_red) / total_intensity;
    return red_proportion;
}