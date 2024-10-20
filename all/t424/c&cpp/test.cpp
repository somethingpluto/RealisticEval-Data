TEST_CASE("Test Dijkstra Algorithm") {
    // Sample graphs for testing
    unordered_map<char, vector<pair<char, int>>> graph1 = {
        {'A', {{'B', 1}, {'C', 4}}},
        {'B', {{'A', 1}, {'C', 2}, {'D', 5}}},
        {'C', {{'A', 4}, {'B', 2}, {'D', 1}}},
        {'D', {{'B', 5}, {'C', 1}}}
    };

    unordered_map<char, vector<pair<char, int>>> graph2 = {
        {'A', {{'B', 2}}},
        {'B', {{'A', 2}, {'C', 3}}},
        {'C', {{'B', 3}, {'D', 1}}},
        {'D', {{'C', 1}}}
    };

    unordered_map<char, vector<pair<char, int>>> graph_with_isolated_node = {
        {'A', {{'B', 1}}},
        {'B', {{'A', 1}}},
        {'C', {}}  // Isolated node
    };

    unordered_map<char, vector<pair<char, int>>> graph_with_negative_weight = {
        {'A', {{'B', 2}, {'C', 1}}},
        {'B', {{'D', 3}}},
        {'C', {{'B', -1}, {'D', 4}}},
        {'D', {}}
    };

    SECTION("Test shortest paths in a normal graph") {
        unordered_map<char, int> expected = {{'A', 0}, {'B', 1}, {'C', 3}, {'D', 4}};
        unordered_map<char, int> result = dijkstra(graph1, 'A');
        REQUIRE(result == expected);
    }

    SECTION("Test shortest paths in a different normal graph") {
        unordered_map<char, int> expected = {{'A', 0}, {'B', 2}, {'C', 5}, {'D', 6}};
        unordered_map<char, int> result = dijkstra(graph2, 'A');
        REQUIRE(result == expected);
    }

    SECTION("Test shortest paths with an isolated node") {
        unordered_map<char, int> expected = {{'A', 0}, {'B', 1}, {'C', INT_MAX}};
        unordered_map<char, int> result = dijkstra(graph_with_isolated_node, 'A');
        REQUIRE(result == expected);
    }

    SECTION("Test when starting at an isolated node") {
        unordered_map<char, int> expected = {{'C', 0}, {'A', INT_MAX}, {'B', INT_MAX}};
        unordered_map<char, int> result = dijkstra(graph_with_isolated_node, 'C');
        REQUIRE(result == expected);
    }


}
