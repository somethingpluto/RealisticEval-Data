#include <vector>
#include <functional>

struct Match {
    int element;
    size_t index;
};

std::vector<Match> findMatchingElements(const std::vector<int>& arr, std::function<bool(int)> comparisonFn) {
    std::vector<Match> result;

    for (size_t i = 0; i < arr.size(); i++) {
        if (comparisonFn(arr[i])) {
            result.push_back({arr[i], i});
        }
    }

    return result;
}