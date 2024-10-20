TEST_CASE("Test Floyd-Warshall Shortest Paths", "[floyd-warshall]") {
    SECTION("Basic functionality") {
        // Basic test case with a simple graph
        std::vector<std::vector<int>> matrix = {
            {0, 3, INT_MAX, 7},
            {8, 0, 2, INT_MAX},
            {5, INT_MAX, 0, 1},
            {2, INT_MAX, INT_MAX, 0}
        };
        std::vector<std::vector<int>> expected = {
            {0, 3, 5, 6},
            {5, 0, 2, 3},
            {3, 6, 0, 1},
            {2, 5, 7, 0}
        };
        auto result = floyd_warshall_shortest_paths(matrix);
        REQUIRE(result == expected);
    }

    SECTION("Single vertex graph") {
        // Test case with a single vertex graph (1x1 matrix)
        std::vector<std::vector<int>> matrix = {
            {0}
        };
        std::vector<std::vector<int>> expected = {
            {0}
        };
        auto result = floyd_warshall_shortest_paths(matrix);
        REQUIRE(result == expected);
    }

    SECTION("Two vertices graph") {
        // Test case with two vertices
        std::vector<std::vector<int>> matrix = {
            {0, 1},
            {1, 0}
        };
        std::vector<std::vector<int>> expected = {
            {0, 1},
            {1, 0}
        };
        auto result = floyd_warshall_shortest_paths(matrix);
        REQUIRE(result == expected);
    }

    SECTION("Large infinite weights") {
        // Test case with infinite weights
        std::vector<std::vector<int>> matrix = {
            {0, INT_MAX},
            {INT_MAX, 0}
        };
        std::vector<std::vector<int>> expected = {
            {0, INT_MAX},
            {INT_MAX, 0}
        };
        auto result = floyd_warshall_shortest_paths(matrix);
        REQUIRE(result == expected);
    }

    SECTION("Negative cycle") {
        // Test case with a negative cycle
        std::vector<std::vector<int>> matrix = {
            {0, 1, INT_MAX},
            {INT_MAX, 0, -1},
            {-1, INT_MAX, 0}
        };
        std::vector<std::vector<int>> expected = {
            {-1, 0, -1},
            {-2, -1, -2},
            {-2, -1, -2}
        };
        auto result = floyd_warshall_shortest_paths(matrix);
        REQUIRE(result == expected);
    }
}