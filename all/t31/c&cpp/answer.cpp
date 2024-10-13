#include <vector>
#include <tuple>
#include <iostream>

float calculateRedProportion(const std::vector<std::tuple<int, int, int>>& pixels) {
    if (pixels.empty()) {
        return 0.0f;
    }

    int totalRed = 0;
    int totalIntensity = 0;

    for (const auto& pixel : pixels) {
        int r, g, b;
        std::tie(r, g, b) = pixel;
        totalRed += r;
        totalIntensity += (r + g + b);
    }

    // Avoid division by zero
    if (totalIntensity == 0) {
        return 0.0f;
    }

    float redProportion = static_cast<float>(totalRed) / totalIntensity;
    return redProportion;
}

int main() {
    // Example usage
    std::vector<std::tuple<int, int, int>> pixels = {{255, 0, 0}, {0, 255, 0}, {0, 0, 255}};
    float result = calculateRedProportion(pixels);
    std::cout << "Red Proportion: " << result << std::endl;
    return 0;
}