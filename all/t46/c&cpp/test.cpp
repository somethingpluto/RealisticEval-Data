TEST_CASE("TestBinaryTree", "[BinaryTree]") {
    BinaryTree tree;

    SECTION("Test preorder traversal") {
        std::vector<int> result = tree.preorder_traversal(tree.root);
        REQUIRE_THAT(result, Catch::Matchers::Equals(std::vector<int>({1, 2, 4, 5, 3})));
    }

    SECTION("Test inorder traversal") {
        std::vector<int> result = tree.inorder_traversal(tree.root);
        REQUIRE_THAT(result, Catch::Matchers::Equals(std::vector<int>({4, 2, 5, 1, 3})));
    }

    SECTION("Test postorder traversal") {
        std::vector<int> result =tree.postorder_traversal(tree.root);
        REQUIRE_THAT(result, Catch::Matchers::Equals(std::vector<int>({4, 5, 2, 3, 1})));
    }

    SECTION("Test empty tree") {
        BinaryTree empty_tree;
        REQUIRE_THAT(empty_tree.preorder_traversal(empty_tree.root), Catch::Matchers::Equals(std::vector<int>({})));
        REQUIRE_THAT(empty_tree.inorder_traversal(empty_tree.root), Catch::Matchers::Equals(std::vector<int>({})));
        REQUIRE_THAT(empty_tree.postorder_traversal(empty_tree.root), Catch::Matchers::Equals(std::vector<int>({})));
    }

    SECTION("Test single node tree") {
        BinaryTree single_node_tree(new TreeNode(10));
        REQUIRE_THAT(single_node_tree.preorder_traversal(single_node_tree.root), Catch::Matchers::Equals(std::vector<int>({10})));
        REQUIRE_THAT(single_node_tree.inorder_traversal(single_node_tree.root), Catch::Matchers::Equals(std::vector<int>({10})));
        REQUIRE_THAT(single_node_tree.postorder_traversal(single_node_tree.root), Catch::Matchers::Equals(std::vector<int>({10})));
    }
}