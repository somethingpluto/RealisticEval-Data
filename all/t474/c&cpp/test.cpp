TEST_CASE("TestAreSiblings", "[are_siblings]") {
    const std::vector<int> tree = {1, 2, 3, 4, 5, 6, 7};

    SECTION("test_basic_case") {
        // Test with nodes 4 and 5, which are siblings
        bool result = are_siblings(tree, 4, 5);
        REQUIRE(result);
    }

    SECTION("test_non_sibling_case") {
        // Test with nodes 4 and 6, which are not siblings
        bool result = are_siblings(tree, 4, 6);
        REQUIRE_FALSE(result);
    }

    SECTION("test_root_node_case") {
        // Test with node 1 (root) and any other node, should return False
        bool result = are_siblings(tree, 1, 2);
        REQUIRE_FALSE(result);
    }

    SECTION("test_non_existent_values") {
        // Test with non-existent values
        bool result = are_siblings(tree, 8, 9);
        REQUIRE_FALSE(result);
    }

    SECTION("test_same_node_case") {
        // Test with the same node for both values
        bool result = are_siblings(tree, 4, 4);
        REQUIRE_FALSE(result);
    }
}