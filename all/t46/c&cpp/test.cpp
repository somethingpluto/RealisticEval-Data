TEST_CASE("TestBinaryTree", "[BinaryTree]") {
    TestBinaryTree test;

    SECTION("Test preorder traversal") {
        test.setup();
        std::vector<int> result = test.tree.preorder_traversal(test.tree.root);
        REQUIRE_THAT(result, Catch::Matchers::Equals(std::vector<int>({1, 2, 4, 5, 3})));
        test.teardown();
    }

    SECTION("Test inorder traversal") {
        test.setup();
        std::vector<int> result = test.tree.inorder_traversal(test.tree.root);
        REQUIRE_THAT(result, Catch::Matchers::Equals(std::vector<int>({4, 2, 5, 1, 3})));
        test.teardown();
    }

    SECTION("Test postorder traversal") {
        test.setup();
        std::vector<int> result = test.tree.postorder_traversal(test.tree.root);
        REQUIRE_THAT(result, Catch::Matchers::Equals(std::vector<int>({4, 5, 2, 3, 1})));
        test.teardown();
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