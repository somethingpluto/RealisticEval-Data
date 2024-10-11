#include <vector>
using namespace std;

vector<int> flattenArray(const vector<vector<int>>& multiDimArray) {
    vector<int> flatArray;
    for (const auto& row : multiDimArray) {
        for (int num : row) {
            flatArray.push_back(num);
        }
    }
    return flatArray;
}