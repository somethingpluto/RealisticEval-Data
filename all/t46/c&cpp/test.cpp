TEST_CASE("Preorder Traversal", "[tree]") {
    // Create a simple binary tree:     1
    //                               / \
    //                              2   3
    //                             /
    //                            4
    TreeNode* node4 = new TreeNode(4);
    TreeNode* node2 = new TreeNode(2, node4);
    TreeNode* node3 = new TreeNode(3);
    TreeNode* root = new TreeNode(1, node2, node3);

    BinaryTree bt(root);
    std::vector<int> result;
    bt.preorderTraversal(root, result);

    REQUIRE(result == std::vector<int>{1, 2, 4, 3});

    // Clean up memory
    delete node4;
    delete node2;
    delete node3;
    delete root;
}

TEST_CASE("Inorder Traversal", "[tree]") {
    // Same tree structure as above
    TreeNode* node4 = new TreeNode(4);
    TreeNode* node2 = new TreeNode(2, node4);
    TreeNode* node3 = new TreeNode(3);
    TreeNode* root = new TreeNode(1, node2, node3);

    BinaryTree bt(root);
    std::vector<int> result;
    bt.inorderTraversal(root, result);

    REQUIRE(result == std::vector<int>{4, 2, 1, 3});

    // Clean up memory
    delete node4;
    delete node2;
    delete node3;
    delete root;
}

TEST_CASE("Postorder Traversal", "[tree]") {
    // Same tree structure as above
    TreeNode* node4 = new TreeNode(4);
    TreeNode* node2 = new TreeNode(2, node4);
    TreeNode* node3 = new TreeNode(3);
    TreeNode* root = new TreeNode(1, node2, node3);

    BinaryTree bt(root);
    std::vector<int> result;
    bt.postorderTraversal(root, result);

    REQUIRE(result == std::vector<int>{4, 2, 3, 1});

    // Clean up memory
    delete node4;
    delete node2;
    delete node3;
    delete root;
}