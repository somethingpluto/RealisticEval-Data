TEST_CASE("Average of Levels", "[averageOfLevels]") {
    // Test case 1: Empty tree
    REQUIRE(averageOfLevels(nullptr).empty());

    // Test case 2: Single node tree
    TreeNode root1(3);
    REQUIRE(averageOfLevels(&root1) == std::vector<double>({3.0}));

    // Test case 3: Tree with multiple levels
    TreeNode root2(3);
    root2.left = new TreeNode(9);
    root2.right = new TreeNode(20);
    root2.right->left = new TreeNode(15);
    root2.right->right = new TreeNode(7);
    REQUIRE(averageOfLevels(&root2) == std::vector<double>({3.0, 14.5, 11.0}));
}