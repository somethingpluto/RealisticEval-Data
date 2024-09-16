//Dataset.cpp
#include "dataset/Dataset.hpp"
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>

Dataset::Dataset() {}


size_t Dataset::size() const {
    return this->features.size();
}


//written by ChatGPT
void Dataset::print() const {
    // Find the maximum width for the label column, including the "Labels" header
    int labelMaxWidth = std::max(static_cast<int>(std::to_string(*std::max_element(labels.begin(), labels.end())).size()), static_cast<int>(strlen("Labels")));

    // Find maximum width for each feature column, considering both data and header widths
    std::vector<int> featureMaxWidths(headers.size(), 0);
    for (size_t i = 0; i < headers.size(); ++i) {
        featureMaxWidths[i] = headers[i].size();
    }

    for (const auto& featureRow : features) {
        for (size_t i = 0; i < featureRow.size(); ++i) {
            featureMaxWidths[i] = std::max(featureMaxWidths[i], static_cast<int>(featureRow[i].size()));
        }
    }

    // Print headers
    std::cout << std::left << std::setw(labelMaxWidth) << "Labels" << " "; // Print label header
    for (size_t i = 0; i < headers.size(); ++i) {
        std::cout << std::left << std::setw(featureMaxWidths[i]) << headers[i] << " ";
    }
    std::cout << "\n";

    // Print data
    for (size_t i = 0; i < features.size(); ++i) {
        std::cout << std::left << std::setw(labelMaxWidth) << labels[i] << " ";
        for (size_t j = 0; j < features[i].size(); ++j) {
            std::cout << std::left << std::setw(featureMaxWidths[j]) << features[i][j] << " ";
        }
        std::cout << "\n";
    }
}