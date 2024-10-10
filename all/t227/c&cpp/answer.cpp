#include <iostream>
#include <unordered_set>
#include <fstream>
#include <vector>

using namespace std;

int countUniqueColors(const string& imagePath) {
    // TODO: Implement the logic to read the image and count unique colors
    // For simplicity, let's assume that we have already read the image into a vector of RGB values
    vector<vector<vector<int>>> image = readImage(imagePath);

    unordered_set<string> uniqueColors;
    for (const auto& row : image) {
        for (const auto& pixel : row) {
            string color = to_string(pixel[0]) + "," + to_string(pixel[1]) + "," + to_string(pixel[2]);
            uniqueColors.insert(color);
        }
    }

    return uniqueColors.size();
}

// This function reads the image and returns it as a vector of RGB values
vector<vector<vector<int>>> readImage(const string& imagePath) {
    // TODO: Implement the logic to read the image from the given path
    // For simplicity, let's assume that we have implemented this function elsewhere
    vector<vector<vector<int>>> image;
    return image;
}