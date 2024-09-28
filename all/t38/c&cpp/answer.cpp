#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>

std::string interpolateColorComponent(int c1, int c2, int steps, int i) {
    return std::to_string(static_cast<int>(c1 + (i * (c2 - c1) / steps)));
}

std::vector<std::string> interpolateColors(const std::string &color1, const std::string &color2, int steps) {
    int r1 = std::stoi(color1.substr(1, 2), nullptr, 16);
    int g1 = std::stoi(color1.substr(3, 2), nullptr, 16);
    int b1 = std::stoi(color1.substr(5, 2), nullptr, 16);
    int r2 = std::stoi(color2.substr(1, 2), nullptr, 16);
    int g2 = std::stoi(color2.substr(3, 2), nullptr, 16);
    int b2 = std::stoi(color2.substr(5, 2), nullptr, 16);
    std::vector<std::string> result;
    
    for (int i = 1; i < steps; ++i) {
        std::ostringstream color;
        color << "#" 
              << std::setw(2) << std::setfill('0') << std::hex << (int)(r1 + (i * (r2 - r1) / steps))
              << std::setw(2) << std::setfill('0') << std::hex << (int)(g1 + (i * (g2 - g1) / steps))
              << std::setw(2) << std::setfill('0') << std::hex << (int)(b1 + (i * (b2 - b1) / steps));
        result.push_back(color.str());
    }

    return result;
}

std::vector<std::string> rainbowHexGenerator(int num_intermediates, bool include_endpoints = false) {
    std::vector<std::string> rainbow_colors = {
        "#FF0000",  // Red
        "#FF7F00",  // Orange
        "#FFFF00",  // Yellow
        "#00FF00",  // Green
        "#0000FF",  // Blue
        "#4B0082",  // Indigo
        "#8A2BE2"   // Violet
    };

    std::vector<std::string> full_spectrum;
    int num_main_colors = rainbow_colors.size();

    for (int i = 0; i < num_main_colors - 1 + include_endpoints; ++i) {
        int next_index = (i + 1) % num_main_colors;  // Wrap around for endpoint inclusion
        std::string current_color = rainbow_colors[i];
        std::string next_color = rainbow_colors[next_index];
        full_spectrum.push_back(current_color);
        std::vector<std::string> intermediate_colors = interpolateColors(current_color, next_color, num_intermediates + 1);
        full_spectrum.insert(full_spectrum.end(), intermediate_colors.begin(), intermediate_colors.end());
    }

    // Append the last color only if endpoints are not included
    if (!include_endpoints) {
        full_spectrum.push_back(rainbow_colors.back());
    }

    return full_spectrum;
}

int main() {
    int num_intermediates = 5;
    bool include_endpoints = false;
    std::vector<std::string> spectrum = rainbowHexGenerator(num_intermediates, include_endpoints);
    for (const auto &color : spectrum) {
        std::cout << color << std::endl;
    }

    return 0;
}