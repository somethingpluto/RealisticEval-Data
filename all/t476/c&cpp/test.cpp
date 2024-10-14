#define CATCH_CONFIG_MAIN
#include "catch.hpp"

TEST_CASE("Topological Sort DFS", "[topological_sort]") {
    SECTION("Empty graph") {
        std::vector<int> vertices = {};
        std::vector<std::pair<int, int>> edges = {};
        REQUIRE(topological_sort_dfs(vertices, edges).empty());
    }

    SECTION("Single node") {
        std::vector<int> vertices = {1};
        std::vector<std::pair<int, int>> edges = {};
        REQUIRE(topological_sort_dfs(vertices, edges) == std::vector<int>{1});
    }

    SECTION("Linear graph") {
        std::vector<int> vertices = {1, 2, 3, 4};
        std::vector<std::pair<int, int>> edges = {{1, 2}, {2, 3}, {3, 4}};
        REQUIRE(topological_sort_dfs(vertices, edges) == std::vector<int>{1, 2, 3, 4});
    }

    SECTION("Graph with cycle") {
        std::vector<int> vertices = {1, 2, 3};
        std::vector<std::pair<int, int>> edges = {{1, 2}, {2, 3}, {3, 1}};
        REQUIRE(topological_sort_dfs(vertices, edges).empty());
    }

    SECTION("Disconnected graph") {
        std::vector<int> vertices = {1, 2, 3, 4};
        std::vector<std::pair<int, int>> edges = {{1, 2}, {3, 4}};
        REQUIRE(topological_sort_dfs(vertices, edges) == std::vector<int>{1, 2, 3, 4});
    }
}
