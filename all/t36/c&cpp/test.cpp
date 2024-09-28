#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>
#include <limits>

using namespace std;

const double INF = numeric_limits<double>::infinity();

// Assuming floydWarshallShortestPaths is defined somewhere
vector<vector<double>> floydWarshallShortestPaths(vector<vector<double>>& adjacencyMatrix);

TEST_CASE("Basic functionality") {
    vector<vector<double>> matrix = {
        {0, 3, INF, 7},
        {8, 0, 2, INF},
        {5, INF, 0, 1},
        {2, INF, INF, 0}
    };
    vector<vector<double>> expected = {
        {0, 3, 5, 6},
        {5, 0, 2, 3},
        {3, 6, 0, 1},
        {2, 5, 7, 0}
    };
    vector<vector<double>> result = floydWarshallShortestPaths(matrix);

    REQUIRE(result == expected);
}

TEST_CASE("Single vertex graph") {
    vector<vector<double>> matrix = {
        {0}
    };
    vector<vector<double>> expected = {
        {0}
    };
    vector<vector<double>> result = floydWarshallShortestPaths(matrix);

    REQUIRE(result == expected);
}

TEST_CASE("Two vertices graph") {
    vector<vector<double>> matrix = {
        {0, 1},
        {1, 0}
    };
    vector<vector<double>> expected = {
        {0, 1},
        {1, 0}
    };
    vector<vector<double>> result = floydWarshallShortestPaths(matrix);

    REQUIRE(result == expected);
}

TEST_CASE("Large infinite weights") {
    vector<vector<double>> matrix = {
        {0, INF},
        {INF, 0}
    };
    vector<vector<double>> expected = {
        {0, INF},
        {INF, 0}
    };
    vector<vector<double>> result = floydWarshallShortestPaths(matrix);

    REQUIRE(result == expected);
}

TEST_CASE("Negative cycle") {
    vector<vector<double>> matrix = {
        {0, 1, INF},
        {INF, 0, -1},
        {-1, INF, 0}
    };
    vector<vector<double>> expected = {
        {-1, 0, -1},
        {-2, -1, -2},
        {-2, -1, -2}
    };
    vector<vector<double>> result = floydWarshallShortestPaths(matrix);

    REQUIRE(result == expected);
}