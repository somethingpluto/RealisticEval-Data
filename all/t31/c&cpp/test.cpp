#define CATCH_CONFIG_MAIN  
#include <catch2/catch.hpp>
#include <vector>
#include <tuple>

// Include your calculate_red_proportion function here or include its header
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

TEST_CASE("All red pixels") {
    std::vector<std::tuple<int, int, int>> pixels = {{255, 0, 0}, {255, 0, 0}, {255, 0, 0}};
    REQUIRE(calculate_red_proportion(pixels) == Approx(1.0));
}

TEST_CASE("No red pixels") {
    std::vector<std::tuple<int, int, int>> pixels = {{0, 255, 0}, {0, 0, 255}, {0, 255, 255}};
    REQUIRE(calculate_red_proportion(pixels) == Approx(0.0));
}

TEST_CASE("Empty pixel list") {
    std::vector<std::tuple<int, int, int>> pixels;
    REQUIRE(calculate_red_proportion(pixels) == Approx(0.0));
}

TEST_CASE("All black pixels") {
    std::vector<std::tuple<int, int, int>> pixels = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
    REQUIRE(calculate_red_proportion(pixels) == Approx(0.0));
}