TEST_CASE("Binary Tree Tests", "[binarytree]") {
    BinaryTree bt;
    bt.insert(50);
    bt.insert(30);
    bt.insert(70);
    bt.insert(20);
    bt.insert(40);
    bt.insert(60);
    bt.insert(80);

    SECTION("Inorder Traversal") {
        std::vector<int> expected = {20, 30, 40, 50, 60, 70, 80};
        REQUIRE(bt.inorderTraversal() == expected);
    }

    SECTION("Preorder Traversal") {
        std::vector<int> expected = {50, 30, 20, 40, 70, 60, 80};
        REQUIRE(bt.preorderTraversal() == expected);
    }

    SECTION("Postorder Traversal") {
        std::vector<int> expected = {20, 40, 30, 60, 80, 70, 50};
        REQUIRE(bt.postorderTraversal() == expected);
    }
}