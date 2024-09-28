#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <vector>

// Include the BinaryTree and TreeNode classes here or make sure to include the corresponding header files.

// Test case setup using Catch2
TreeNode* setupBasicTree() {
    // Tree structure:
    //      1
    //     / \
    //    2   3
    //   / \
    //  4   5
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2, new TreeNode(4), new TreeNode(5));
    root->right = new TreeNode(3);
    return root;
}

/* Helper function to delete the tree to avoid memory leaks */
void deleteTree(TreeNode* node) {
    if (node) {
        deleteTree(node->left);
        deleteTree(node->right);
        delete node;
    }
}

TEST_CASE("BinaryTree Traversals") {
    BinaryTree tree(setupBasicTree());

    SECTION("Preorder Traversal") {
        std::vector<int> result = tree.preorderTraversal(tree.root);
        std::vector<int> expected = {1, 2, 4, 5, 3};
        REQUIRE(result == expected);
    }

    SECTION("Inorder Traversal") {
        std::vector<int> result = tree.inorderTraversal(tree.root);
        std::vector<int> expected = {4, 2, 5, 1, 3};
        REQUIRE(result == expected);
    }

    SECTION("Postorder Traversal") {
        std::vector<int> result = tree.postorderTraversal(tree.root);
        std::vector<int> expected = {4, 5, 2, 3, 1};
        REQUIRE(result == expected);
    }

    // Delete the constructed tree to avoid memory leaks
    deleteTree(tree.root);

    SECTION("Empty Tree Traversal") {
        BinaryTree emptyTree;
        REQUIRE(emptyTree.preorderTraversal(emptyTree.root).empty());
        REQUIRE(emptyTree.inorderTraversal(emptyTree.root).empty());
        REQUIRE(emptyTree.postorderTraversal(emptyTree.root).empty());
    }

    SECTION("Single Node Tree Traversal") {
        BinaryTree singleNodeTree(new TreeNode(10));
        std::vector<int> expected = {10};
        REQUIRE(singleNodeTree.preorderTraversal(singleNodeTree.root) == expected);
        REQUIRE(singleNodeTree.inorderTraversal(singleNodeTree.root) == expected);
        REQUIRE(singleNodeTree.postorderTraversal(singleNodeTree.root) == expected);

        // Delete the constructed node to avoid memory leaks
        delete singleNodeTree.root;
    }
}