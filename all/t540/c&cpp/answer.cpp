#include <iostream>
#include <vector>

using namespace std;

/**
 * Generates all unique combinations of pairs from an array.
 *
 * @param array - The input vector from which combinations are generated.
 * @returns A vector of vectors, where each inner vector contains a unique pair of elements.
 */
vector<vector<int>> generateUniquePairs(const vector<int>& array) {
    vector<vector<int>> pairs;
    int length = array.size();

    for (int i = 0; i < length; i++) {
        for (int j = i + 1; j < length; j++) {
            pairs.push_back({array[i], array[j]});
        }
    }

    return pairs;
}

int main() {
    vector<int> inputArray = {1, 2, 3, 4}; // Example input
    vector<vector<int>> result = generateUniquePairs(inputArray);

    // Print the result
    for (const auto& pair : result) {
        cout << "(" << pair[0] << ", " << pair[1] << ")" << endl;
    }

    return 0;
}