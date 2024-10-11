#include <vector>
#include <queue>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

std::vector<double> averageOfLevels(TreeNode* root) {
    std::vector<double> result;
    if (!root)
        return result;

    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int size = q.size();
        double sum = 0;

        for (int i = 0; i < size; ++i) {
            TreeNode* node = q.front();
            q.pop();

            sum += node->val;

            if (node->left)
                q.push(node->left);
            if (node->right)
                q.push(node->right);
        }

        result.push_back(sum / size);
    }

    return result;
}