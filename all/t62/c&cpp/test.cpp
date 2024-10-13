// Test cases using Catch2
TEST_CASE("Test empty tree", "[BinaryTree]") {
    BinaryTree bt;
    REQUIRE(bt.inorder_traversal() == std::vector<int>());
    REQUIRE(bt.preorder_traversal() == std::vector<int>());
    REQUIRE(bt.postorder_traversal() == std::vector<int>());
}

TEST_CASE("Test single node tree", "[BinaryTree]") {
    BinaryTree bt;
    bt.insert(10);
    REQUIRE(bt.inorder_traversal() == std::vector<int>({10}));
    REQUIRE(bt.preorder_traversal() == std::vector<int>({10}));
    REQUIRE(bt.postorder_traversal() == std::vector<int>({10}));
}

TEST_CASE("Test balanced tree", "[BinaryTree]") {
    BinaryTree bt;
    std::vector<int> elements = {8, 3, 10, 1, 6, 9, 14};
    for (int elem : elements) {
        bt.insert(elem);
    }
    REQUIRE(bt.inorder_traversal() == std::vector<int>({1, 3, 6, 8, 9, 10, 14}));
    REQUIRE(bt.preorder_traversal() == std::vector<int>({8, 3, 1, 6, 10, 9, 14}));
    REQUIRE(bt.postorder_traversal() == std::vector<int>({1, 6, 3, 9, 14, 10, 8}));
}

TEST_CASE("Test left-heavy tree", "[BinaryTree]") {
    BinaryTree bt;
    for (int i = 10; i >= 1; --i) {
        bt.insert(i);
    }
    REQUIRE(bt.inorder_traversal() == std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
    REQUIRE(bt.preorder_traversal() == std::vector<int>({10, 9, 8, 7, 6, 5, 4, 3, 2, 1}));
    REQUIRE(bt.postorder_traversal() == std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
}

TEST_CASE("Test right-heavy tree", "[BinaryTree]") {
    BinaryTree bt;
    for (int i = 1; i <= 10; ++i) {
        bt.insert(i);
    }
    REQUIRE(bt.inorder_traversal() == std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
    REQUIRE(bt.preorder_traversal() == std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
    REQUIRE(bt.postorder_traversal() == std::vector<int>({10, 9, 8, 7, 6, 5, 4, 3, 2, 1}));
}