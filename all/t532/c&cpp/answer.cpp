#include <iostream>
#include <vector>
#include <string>

std::vector<int> countLetterChanges(const std::string& inputString) {
    std::vector<int> counts;
    int currentCount = 1;

    for (size_t i = 1; i < inputString.length(); i++) {
        if (inputString[i] != inputString[i - 1]) {
            counts.push_back(currentCount);
            currentCount = 1;
        } else {
            currentCount++;
        }
    }

    counts.push_back(currentCount);
    return counts;
}

int main() {
    std::string input = "aaabbc"; // Example input
    std::vector<int> result = countLetterChanges(input);
    
    for (int count : result) {
        std::cout << count << " ";
    }
    
    return 0;
}