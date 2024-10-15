#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::string isBackgroundTooDarkOrBright(const std::string& backgroundColor) {
    // Extract RGB values from the background color string
    std::istringstream ss(backgroundColor);
    std::string token;
    std::vector<int> rgb;
    
    while (std::getline(ss, token, ',')) {
        rgb.push_back(std::stoi(token));
    }
    
    // Calculate perceived brightness
    int r = rgb[0];
    int g = rgb[1];
    int b = rgb[2];
    double brightness = (r * 299 + g * 587 + b * 114) / 1000.0;

    // Define thresholds
    const double darkThreshold = 125.0;
    const double brightThreshold = 200.0;

    // Determine brightness level
    if (brightness < darkThreshold) {
        return "dark";
    } else if (brightness > brightThreshold) {
        return "bright";
    } else {
        return "normal";
    }
}

int main() {
    std::string backgroundColor = "100,150,200"; // Example RGB
    std::cout << isBackgroundTooDarkOrBright(backgroundColor) << std::endl;
    return 0;
}