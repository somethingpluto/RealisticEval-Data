#include <vector>
#include <stdexcept>

std::vector<double> scaleToRange(const std::vector<double>& inputArray, double inputMin, double inputMax, double outputMin, double outputMax) {
    // Ensure all values in inputArray are within the input range
    for (double value : inputArray) {
        if (value < inputMin || value > inputMax) {
            throw std::invalid_argument("Value " + std::to_string(value) + " in inputArray is outside the range [" + std::to_string(inputMin) + ", " + std::to_string(inputMax) + "].");
        }
    }

    double scale = (outputMax - outputMin) / (inputMax - inputMin);
    std::vector<double> outputArray;

    for (double value : inputArray) {
        outputArray.push_back((value - inputMin) * scale + outputMin);
    }

    return outputArray;
}