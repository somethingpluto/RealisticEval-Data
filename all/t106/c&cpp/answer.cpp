#include <string>
#include <regex>

bool isBase64Image(const std::string& imageData) {
    // Check if the input is a non-empty string
    if (imageData.empty()) {
        return false;
    }

    // Regular expression to validate a Base64 image string
    std::regex base64ImagePattern(R"(data:image/(jpeg|png|gif|bmp|webp);base64,[A-Za-z0-9+/]+={0,2})");

    // Test the image data against the pattern
    return std::regex_match(imageData, base64ImagePattern);
}