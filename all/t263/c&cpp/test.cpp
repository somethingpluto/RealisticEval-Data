TEST_CASE("TestMatrixTraversal", "[MatrixTraversal]") {
    MatrixTraversal mt;

    SECTION("Empty matrix") {
        // 异常值测试：空矩阵
        REQUIRE(spiral_traversal({}) == std::vector<int>{});
    }

    SECTION("Single element matrix") {
        // 基本逻辑功能测试：单元素矩阵
        std::vector<std::vector<int>> matrix = {{42}};
        REQUIRE(spiral_traversal(matrix) == std::vector<int>{42});
    }

    SECTION("Single row matrix") {
        // 边界值测试：单行矩阵
        std::vector<std::vector<int>> matrix = {{1, 2, 3, 4, 5}};
        REQUIRE(spiral_traversal(matrix) == std::vector<int>{1, 2, 3, 4, 5});
    }

    SECTION("Single column matrix") {
        // 边界值测试：单列矩阵
        std::vector<std::vector<int>> matrix = {{1}, {2}, {3}, {4}, {5}};
        REQUIRE(spiral_traversal(matrix) == std::vector<int>{1, 2, 3, 4, 5});
    }

    SECTION("General case") {
        // 基本逻辑功能测试：多行多列矩阵
        std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        REQUIRE(spiral_traversal(matrix) == std::vector<int>{1, 2, 3, 6, 9, 8, 7, 4, 5});
    }
}