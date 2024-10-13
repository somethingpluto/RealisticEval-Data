#include <CImg/CImg.h>
#include <iostream>
#include <vector>

using namespace cimg_library;

void convertPngToIco(const std::string& pngFilePath, const std::string& icoFilePath, const std::vector<std::pair<int, int>>& iconSizes = {{32, 32}}) {
    /**
     * Convert a PNG image file to an ICO format file.
     *
     * Args:
     * pngFilePath (std::string): Path to the source PNG image file.
     * icoFilePath (std::string): Path to save the ICO file.
     * iconSizes (std::vector<std::pair<int, int>>): List of pairs specifying the sizes to include in the ICO file.
     */
    
    // Load the PNG image
    CImg<unsigned char> img(pngFilePath.c_str());
    
    // Create an ICO file
    CImgList<unsigned char> ico;
    
    // Add each size to the ICO file
    for (const auto& size : iconSizes) {
        CImg<unsigned char> resizedImg(size.first, size.second, 1, 3);
        img.resize(resizedImg, size.first, size.second, 0, 0, 3); // Resize the image
        ico.insert(resizedImg); // Insert the resized image into the ICO list
    }
    
    // Save the ICO file
    ico.save(icoFilePath.c_str(), "ICO");
}

int main() {
    // Example usage
    std::string pngFilePath = "path/to/source.png";
    std::string icoFilePath = "path/to/output.ico";
    std::vector<std::pair<int, int>> iconSizes = {{32, 32}};
    
    convertPngToIco(pngFilePath, icoFilePath, iconSizes);
    
    std::cout << "Conversion complete." << std::endl;
    
    return 0;
}