#include <iostream>
#include <string>
#include <regex>

std::string compressFilename(const std::string& filename, int maxLength) {
    // Extract the file extension
    std::regex extensionRegex("\\.[^\\.]+$");
    std::smatch extensionMatch;

    std::string extension;
    if (std::regex_search(filename, extensionMatch, extensionRegex)) {
        extension = extensionMatch.str(0);
    }

    // Remove the extension from the filename for manipulation
    std::string basename = extension.empty() ? filename : filename.substr(0, filename.size() - extension.size());

    // Compress the basename if it's longer than maxLength
    std::string compressedBasename = basename.size() > maxLength ?
        basename.substr(0, maxLength - 3) + "***" : basename;

    // Reattach the extension and return
    return compressedBasename + extension;
}

int main() {
    std::string filename = "verylongfilename.txt";
    int maxLength = 10;
    
    std::string compressed = compressFilename(filename, maxLength);
    std::cout << "Compressed filename: " << compressed << std::endl;

    return 0;
}