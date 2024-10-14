TEST_CASE("TestGraphCycles", "[Graph]") {
    SECTION("test_empty_graph") {
        Graph g({});
        auto result = g.cycles_by_size();
        REQUIRE(result.empty());
    }

    SECTION("test_graph_no_cycles") {
        Graph g({{1, 2}, {2, 3}});
        auto result = g.cycles_by_size();
        REQUIRE(result.empty());
    }

    SECTION("test_simple_cycles") {
        Graph g({{1, 2}, {2, 3}, {3, 1}});
        auto result = g.cycles_by_size();
        REQUIRE(result.count(3) == 1);
        REQUIRE(result.at(3).size() == 1);
        REQUIRE(std::all_of(result.at(3).begin(), result.at(3).end(), [](const Graph& subgraph) {
            std::vector<Vertex> nodes(boost::num_vertices(subgraph));
            boost::iota(nodes, 0); // Initialize nodes with indices
            std::sort(nodes.begin(), nodes.end(), [&subgraph](Vertex u, Vertex v) {
                return boost::degree(u, subgraph) < boost::degree(v, subgraph);
            });
            return nodes == std::vector<Vertex>({1, 2, 3});
        }));
    }

    SECTION("test_multiple_cycles") {
        Graph g({{1, 2}, {2, 3}, {3, 1}, {3, 4}, {4, 1}});
        auto result = g.cycles_by_size();
        REQUIRE(result.count(3) == 1);
        REQUIRE(result.at(3).size() == 1);
        REQUIRE(result.count(4) == 1);
        REQUIRE(result.at(4).size() == 1);
    }
}
