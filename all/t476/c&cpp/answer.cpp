#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Graph {
private:
    int V; // Number of vertices
    vector<int> *adj; // Adjacency lists

public:
    Graph(int V);
    void addEdge(int v, int w);
    bool dfsUtil(int v, stack<int>& Stack, vector<bool>& visited);
    vector<int> topologicalSort();
};

Graph::Graph(int V) {
    this->V = V;
    adj = new vector<int>[V];
}

void Graph::addEdge(int v, int w) {
    adj[v].push_back(w); // Add w to v’s list.
}

bool Graph::dfsUtil(int v, stack<int>& Stack, vector<bool>& visited) {
    // Mark the current node as visited.
    visited[v] = true;

    // Recur for all the vertices adjacent to this vertex.
    for (int i = 0; i != adj[v].size(); ++i) {
        if (!visited[adj[v][i]]) {
            if (!dfsUtil(adj[v][i], Stack, visited)) return false;
        }
    }

    // Push current vertex to stack which stores result
    Stack.push(v);

    return true;
}

vector<int> Graph::topologicalSort() {
    stack<int> Stack;
    vector<bool> visited(V, false);

    // Call the recursive helper function to store Topological Sort starting from all vertices one by one
    for (int i = 0; i < V; i++)
        if (!visited[i])
            if (!dfsUtil(i, Stack, visited))
                return {}; // Cycle detected, no topological sort possible

    vector<int> topoOrder;
    while (!Stack.empty()) {
        topoOrder.push_back(Stack.top());
        Stack.pop();
    }

    return topoOrder;
}
