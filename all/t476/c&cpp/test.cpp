TEST_CASE("Test topological_sort_dfs", "[topological_sort_dfs]") {
    SECTION("test_simple_chain") {
        std::vector<int> vertices = {1, 2, 3};
        std::vector<std::pair<int, int>> edges = {{1, 2}, {2, 3}};
        REQUIRE(topological_sort_dfs(vertices, edges) == std::vector<int>({1, 2, 3}));
    }

    SECTION("test_disconnected_graph") {
        std::vector<int> vertices = {1, 2, 3, 4};
        std::vector<std::pair<int, int>> edges = {{1, 2}};
        auto result = topological_sort_dfs(vertices, edges);
        REQUIRE(std::find(result.begin(), result.end(), 1) < std::find(result.begin(), result.end(), 2));
        REQUIRE(std::find(result.begin(), result.end(), 3) != result.end());
        REQUIRE(std::find(result.begin(), result.end(), 4) != result.end());
    }

    SECTION("test_complex_graph") {
        std::vector<int> vertices = {1, 2, 3, 4, 5, 6};
        std::vector<std::pair<int, int>> edges = {{1, 2}, {1, 3}, {2, 4}, {3, 4}, {4, 5}, {6, 1}};
        auto result = topological_sort_dfs(vertices, edges);
        REQUIRE(std::find(result.begin(), result.end(), 1) < std::find(result.begin(), result.end(), 2));
        REQUIRE(std::find(result.begin(), result.end(), 1) < std::find(result.begin(), result.end(), 3));
        REQUIRE(std::find(result.begin(), result.end(), 2) < std::find(result.begin(), result.end(), 4));
        REQUIRE(std::find(result.begin(), result.end(), 3) < std::find(result.begin(), result.end(), 4));
        REQUIRE(std::find(result.begin(), result.end(), 4) < std::find(result.begin(), result.end(), 5));
        REQUIRE(std::find(result.begin(), result.end(), 6) < std::find(result.begin(), result.end(), 1));
    }

    SECTION("test_single_vertex") {
        std::vector<int> vertices = {1};
        std::vector<std::pair<int, int>> edges = {};
        REQUIRE(topological_sort_dfs(vertices, edges) == std::vector<int>({1}));
    }
}