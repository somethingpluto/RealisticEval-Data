#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

/**
 * @brief Finds the maximum difference between elements in the array
 * such that the smaller element appears before the larger one.
 *
 * @param l A vector of integers containing the elements.
 * @return The maximum difference.
 */
int findMaxDifference(const vector<int>& l) {
    int min_val = l[0];
    int max_diff = numeric_limits<int>::min();

    for (size_t i = 1; i < l.size(); ++i) {
        max_diff = max(max_diff, l[i] - min_val);
        min_val = min(min_val, l[i]);
    }

    return max_diff;
}

int main() {
    int n;
    cin >> n;
    vector<int> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    int max_diff = findMaxDifference(l);
    cout << max_diff << endl;
    return 0;
}
