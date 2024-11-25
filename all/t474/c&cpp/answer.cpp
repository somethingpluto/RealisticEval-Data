#include <vector>
using namespace std;

bool are_siblings(vector<int>& tree, int val1, int val2) {
    // Check if both nodes are present in the tree.
    auto it1 = find(tree.begin(), tree.end(), val1);
    auto it2 = find(tree.begin(), tree.end(), val2);

    // If either of the node is not found return false.
    if(it1 == tree.end() || it2 == tree.end()) return false;

    // Get parent index.
    int parentIndex = (it1 - tree.begin() - 1) / 2;

    // Check if they have same parent.
    return parentIndex == (it2 - tree.begin() - 1) / 2;
}

