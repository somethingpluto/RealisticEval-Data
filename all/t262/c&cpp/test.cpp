TEST_CASE("Test average_of_levels") {
    SECTION("Empty Tree") {
        TreeNode* root = nullptr;
        std::vector<double> expected = {};
        REQUIRE(average_of_levels(root) == expected);
    }

    SECTION("Single Node Tree") {
        TreeNode* root = new TreeNode(5);
        std::vector<double> expected = {5.0};
        REQUIRE(average_of_levels(root) == expected);
        delete root;
    }

    SECTION("Balanced Tree Two Levels") {
        TreeNode* root = new TreeNode(3);
        root->left = new TreeNode(9);
        root->right = new TreeNode(20);
        std::vector<double> expected = {3.0, 14.5};
        REQUIRE(average_of_levels(root) == expected);
        delete root->left;
        delete root->right;
        delete root;
    }

    SECTION("Unbalanced Tree") {
        TreeNode* root = new TreeNode(1);
        root->right = new TreeNode(2);
        root->right->right = new TreeNode(3);
        std::vector<double> expected = {1.0, 2.0, 3.0};
        REQUIRE(average_of_levels(root) == expected);
        delete root->right->right;
        delete root->right;
        delete root;
    }

    SECTION("Tree Multiple Levels") {
        TreeNode* root = new TreeNode(1);
        root->left = new TreeNode(2);
        root->right = new TreeNode(3);
        root->left->left = new TreeNode(4);
        root->left->right = new TreeNode(5);
        root->right->right = new TreeNode(8);
        std::vector<double> expected = {1.0, 2.5, 5.67};
        auto result = average_of_levels(root);
        REQUIRE(result.size() == expected.size());
        REQUIRE_THAT(result[0], Catch::Matchers::WithinAbs(expected[0], 0.01));
        REQUIRE_THAT(result[1], Catch::Matchers::WithinAbs(expected[1], 0.01));
        REQUIRE_THAT(result[2], Catch::Matchers::WithinAbs(expected[2], 0.01));
        delete root->left->left;
        delete root->left->right;
        delete root->right->right;
        delete root->left;
        delete root->right;
        delete root;
    }
}