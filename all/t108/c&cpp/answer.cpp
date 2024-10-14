#include <vector>
#include <string>
#include <algorithm>
#include <tuple>
#include <iostream>

struct ImageData {
    int score;
    std::string name;
    std::string id;
};

std::tuple<std::vector<int>, std::vector<std::string>, std::vector<std::string>> reorderData(
    const std::vector<int>& imageScores,
    const std::vector<std::string>& imageNames,
    const std::vector<std::string>& imageIDs) 
{
    std::vector<ImageData> imageData;

    for (size_t i = 0; i < imageScores.size(); ++i) {
        imageData.push_back({imageScores[i], imageNames[i], imageIDs[i]});
    }

    std::sort(imageData.begin(), imageData.end(), [](const ImageData& a, const ImageData& b) {
        return a.score < b.score;
    });

    std::vector<int> resultScores;
    std::vector<std::string> resultNames;
    std::vector<std::string> resultIDs;

    for (const auto& data : imageData) {
        resultScores.push_back(data.score);
        resultNames.push_back(data.name);
        resultIDs.push_back(data.id);
    }

    return {resultScores, resultNames, resultIDs};
}