#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/cycles.hpp>

using namespace std;

typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::directedS> Graph;
typedef boost::graph_traits<Graph>::vertex_descriptor Vertex;
typedef boost::graph_traits<Graph>::edge_descriptor Edge;

class Graph {
public:
    Graph(const vector<pair<int, int>>& edges) {
        for (const auto& edge : edges) {
            add_edge(edge.first, edge.second, g);
        }
    }

    map<int, vector<Graph>> cycles_by_size(bool filter_repeat_nodes = true) const {
        vector<set<Vertex>> all_cycles;
        boost::find_cycle(g, std::back_inserter(all_cycles));

        vector<set<Vertex>> cycles;
        for (const auto& cycle : all_cycles) {
            if (cycle.size() > 2) {
                cycles.push_back(cycle);
            }
        }

        if (filter_repeat_nodes) {
            vector<set<Vertex>> filtered_cycles;
            for (const auto& cycle : cycles) {
                set<Vertex> unique_cycle(cycle.begin(), cycle.end());
                if (unique_cycle.size() == cycle.size()) {
                    filtered_cycles.push_back(unique_cycle);
                }
            }
            cycles = filtered_cycles;
        }

        map<int, vector<Graph>> unique_cycles_by_size;
        for (const auto& cycle : cycles) {
            int size = cycle.size();
            Graph subgraph;
            for (const auto& vertex : cycle) {
                add_vertex(vertex, subgraph);
            }
            for (const auto& vertex : cycle) {
                for (auto adj_vertex : cycle) {
                    if (adj_vertex != vertex && boost::edge(vertex, adj_vertex, g).second) {
                        add_edge(vertex, adj_vertex, subgraph);
                    }
                }
            }
            unique_cycles_by_size[size].push_back(subgraph);
        }

        return unique_cycles_by_size;
    }

private:
    Graph g;
};