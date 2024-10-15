#include <iostream>
#include <vector>

double getArrayAverage(const std::vector<double>& array) {
    double sum = 0;
    for (size_t i = 0; i < array.size(); i++) {
        sum += array[i];
    }
    return sum / array.size();
}

int main() {
    std::vector<double> array = {1.0, 2.0, 3.0, 4.0, 5.0}; // Example array
    double average = getArrayAverage(array);
    std::cout << "Average: " << average << std::endl;
    return 0;
}